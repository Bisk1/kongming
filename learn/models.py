import random

from django.contrib.auth.models import User
from django.db import models

from exercises.models import Exercise
from lessons.models import Lesson

from enum import Enum


class Status(Enum):
    not_done = 'u'
    success = 's'
    failure = 'f'


class LessonAction(models.Model):
    total_exercises_number = models.IntegerField(default=0)
    current_exercise_number = models.IntegerField(default=0)
    fails = models.IntegerField(default=0)
    user = models.ForeignKey(User)
    lesson = models.ForeignKey(Lesson, null=True)
    status = models.CharField(null=True, default=None, max_length=1)

    @classmethod
    def create_lesson_action(cls, user, lesson):
        exercises = lesson.exercise_set
        new_lesson_action = cls(total_exercises_number=lesson.exercises_number, current_exercise_number=0,
                                fails=0, user=user, lesson=lesson)
        new_lesson_action.save()

        fixed_exercises_count = exercises.filter(number__isnull=False).count()
        random_exercises_count = lesson.exercises_number - fixed_exercises_count
        random_exercises = exercises.filter(number__isnull=True).order_by('?')[:random_exercises_count]
        #random_exercises = random.sample(random_exercises_candidates, random_choice_exercises_count)
        j = 0
        for i in range(1, lesson.exercises_number + 1):
            try:
                exercise = exercises.get(number=i)
            except Exercise.DoesNotExist:
                exercise = random_exercises[j]
                j += 1
            new_exercise_action = ExerciseAction(exercise=exercise, lesson_action=new_lesson_action, number=i)
            new_exercise_action.save()
        return new_lesson_action

    def has_next(self):
        """
        Check if lesson has next exercise
        """
        return self.current_exercise_number < self.total_exercises_number

    def next_exercise(self):
        """
        Get next lesson exercise
        """
        self.current_exercise_number += 1
        self.save()

    def get_exercise_action(self):
        return ExerciseAction.objects.get(lesson_action=self, number=self.current_exercise_number)

    def check_answer(self, proposition):
        response = self.get_exercise_action().check_answer(proposition)
        if not response['success']:
            self.fails += 1
            self.save()
        return self.add_lesson_specific_data(response)

    def prepare(self):
        response = self.get_exercise_action().prepare()
        return self.add_lesson_specific_data(response)

    def get_final_response(self):
        self.mark_status_as_success_if_not_failed()
        response = {'final': True}
        return self.add_lesson_specific_data(response)

    def add_lesson_specific_data(self, response):
        response['fails'] = self.fails
        response['current_exercise_number'] = self.current_exercise_number
        response['total_exercises_number'] = self.total_exercises_number
        return response

    def mark_status_as_failed(self):
        self.status = Status.failure
        self.save()

    def mark_status_as_success_if_not_failed(self):
        if self.status != Status.failure:
            self.status = Status.success
            self.save()


class ExerciseAction(models.Model):
    exercise = models.ForeignKey(Exercise)
    lesson_action = models.ForeignKey(LessonAction)
    result = models.CharField(default=Status.not_done.value, max_length=1)
    number = models.IntegerField()

    def check_answer(self, proposition):
        response = self.exercise.spec.check_answer(proposition)
        if response['success']:
            self.result = Status.success
        else:
            self.result = Status.failure
        return response

    def prepare(self):
        response = self.exercise.spec.prepare()
        response['exercise_type'] = self.exercise.content_type.name
        return response


