import abc
import random

from django.contrib.auth.models import User
from django.db import models
from enum import Enum

from translations.models import WordPL, WordZH, SentencePL, SentenceZH


PASS = 'p'
FAIL = 'f'

NONE = 'a'
WORD_PL = 'b'
WORD_ZH = 'c'
SENTENCE_PL = 'd'
SENTENCE_ZH = 'e'
EXPLANATION = 'f'
EXPLANATION_IMAGE = 'g'

LANGUAGE_CHOICES = {
    (NONE, 'none'),
    (WORD_PL, 'word_pl'),
    (WORD_ZH, 'word_zh'),
    (SENTENCE_PL, 'sentence_pl'),
    (SENTENCE_ZH, 'sentence_zh'),
    (EXPLANATION, 'explanation'),
    (EXPLANATION_IMAGE, 'explanation_image')
}


class Lesson(models.Model):
    """
    Single Chinese lesson is defined by level
    and words related to it.
    """
    topic = models.CharField(max_length=100, default="NO-NAME")
    exercises_number = models.IntegerField()
    requirement = models.ForeignKey("self", null=True)

    def determine_status(self, user):
        lesson_actions = LessonAction.objects.filter(lesson=self,user=user)
        if lesson_actions.filter(status='p').count() > 0:
            return PASS
        elif lesson_actions.filter(status='f').count() > 0:
            return FAIL
        else:
            return None

    def __unicode__(self):
        return unicode(self.topic)


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

        fixed_choice_exercises_count = exercises.filter(number__isnull=False).count()
        random_choice_exercises_count = lesson.exercises_number - fixed_choice_exercises_count
        random_exercises = random.sample(exercises.all(), random_choice_exercises_count)
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
        :return: true if lesson has next exercise
        """
        return self.current_exercise_number < self.total_exercises_number

    def next_exercise(self):
        self.current_exercise_number += 1
        self.save()

    def get_exercise_action(self):
        return ExerciseAction.objects.get(lesson_action=self, number=self.current_exercise_number)

    def check(self, proposition):
        response = self.get_exercise_action().check(proposition)
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
        self.status = FAIL
        self.save()

    def mark_status_as_success_if_not_failed(self):
        if self.status != FAIL:
            self.status = PASS
            self.save()


class Exercise(models.Model):
    lesson = models.ForeignKey(Lesson)
    type = models.CharField(max_length=1, choices=LANGUAGE_CHOICES)
    number = models.IntegerField(null=True)

    exercise_type_to_name_map = {
        WORD_PL: 'word_pl',
        WORD_ZH: 'word_zh',
        SENTENCE_PL: 'sentence_pl',
        SENTENCE_ZH: 'sentence_zh',
        EXPLANATION: 'explanation',
        EXPLANATION_IMAGE: 'explanation_image'
    }

    def __unicode__(self):
        return unicode(self.lesson) + ' ' + unicode(self.id)

    def type_name(self):
        return self.exercise_type_to_name_map[self.type]


class ExerciseResultState(Enum):
    NOT_DONE = 0
    SUCCESS = 1
    FAILURE = 2


class ExerciseAction(models.Model):
    exercise = models.ForeignKey(Exercise)
    lesson_action = models.ForeignKey(LessonAction)
    result = models.IntegerField(default=ExerciseResultState.NOT_DONE)
    number = models.IntegerField()

    def check(self, proposition):
        response = self.get_description().check(proposition)
        if response['success']:
            self.result = ExerciseResultState.SUCCESS
        else:
            self.result = ExerciseResultState.FAILURE
        return response

    def prepare(self):
        response = self.get_description().prepare()
        response['exercise_type'] = self.exercise.type_name()
        return response

    def get_description(self):
        return self.get_description_model().objects.get(exercise=self.exercise)

    def get_description_model(self):
        return exercise_type_to_model(self.exercise.type)


class AbstractExercise(models.Model):
    exercise = models.ForeignKey(Exercise)

    @abc.abstractmethod
    def check(self, proposition):
        pass

    @abc.abstractmethod
    def prepare(self):
        pass

    class Meta:
        abstract = True


class WordZHExercise(AbstractExercise):
    word = models.ForeignKey(WordZH)

    def check(self, proposition):
        return {'success': self.word.check_translation(proposition),
                'correct_word': self.word.wordpl_set.all()[0].word}

    def prepare(self):
        return {'word': self.word.word}

    def __unicode__(self):
        return unicode(self.word)


class WordPLExercise(AbstractExercise):
    word = models.ForeignKey(WordPL)

    def check(self, proposition):
        return {'success': self.word.check_translation(proposition),
                'correct_word': self.word.wordzh_set.all()[0].word}

    def prepare(self):
        return {'word': self.word.word}

    def __unicode__(self):
        return unicode(self.word)


class SentenceZHExercise(AbstractExercise):
    sentence = models.ForeignKey(SentenceZH)

    def check(self, proposition):
        return {'success': self.sentence.check_translation(proposition),
                'correct_sentence': self.sentence.sentencepl_set.all()[0].sentence}

    def prepare(self):
        return {'sentence': self.sentence.sentence}

    def __unicode__(self):
        return unicode(self.sentence)


class SentencePLExercise(AbstractExercise):
    sentence = models.ForeignKey(SentencePL)

    def check(self, proposition):
        return {'success': self.sentence.check_translation(proposition),
                'correct_sentence': self.sentence.sentencezh_set.all()[0].sentence}

    def prepare(self):
        return {'sentence': self.sentence.sentence}

    def __unicode__(self):
        return unicode(self.sentence)


class ExplanationExercise(AbstractExercise):
    text = models.TextField()

    def check(self, proposition):
        raise Exception("ExplanationExerciseDetails has no check method")

    def prepare(self):
        return {'text': self.text}

    def __unicode__(self):
        return unicode(self.text)


class ExplanationImageExercise(AbstractExercise):
    text = models.TextField()
    image = models.FileField(upload_to="image/")

    def check(self, proposition):
        raise Exception("ExplanationExerciseDetails has no check method")

    def prepare(self):
        return {'text': self.text}

    def __unicode__(self):
        return unicode(self.text)


exercise_type_to_model_map = {
    WORD_PL: WordPLExercise,
    WORD_ZH: WordZHExercise,
    SENTENCE_PL: SentencePLExercise,
    SENTENCE_ZH: SentenceZHExercise,
    EXPLANATION: ExplanationExercise,
    EXPLANATION_IMAGE: ExplanationImageExercise
}

exercise_model_to_type_map = {
    WordPLExercise: WORD_PL,
    WordZHExercise: WORD_ZH,
    SentencePLExercise: SENTENCE_PL,
    SentenceZHExercise: SENTENCE_ZH,
    ExplanationExercise: EXPLANATION,
    ExplanationImageExercise: EXPLANATION_IMAGE
}


def exercise_type_to_model(exercise_name):
    try:
        return exercise_type_to_model_map[exercise_name]
    except KeyError:
        raise Exception("Unknown exercise type: " + exercise_name)


def exercise_model_to_type(model):
    try:
        return exercise_model_to_type_map[model]
    except KeyError:
        raise Exception("Unknown exercise model: " + model)