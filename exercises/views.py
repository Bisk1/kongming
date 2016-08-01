import logging

from django.shortcuts import render, redirect

from exercises.models import Lesson, Exercise
from django.core.urlresolvers import reverse
from exercises.forms import ExplanationForm, ChoiceForm, TypingForm, ListeningForm

logger = logging.getLogger(__name__)


class ExerciseTypeHandler:

    def __init__(self, name, form_class):
        self.name = name
        self.form_class = form_class

    def get_name(self):
        return self.name

    def get_form_class(self):
        return self.form_class


exercises_types_handlers = {
    'typing': ExerciseTypeHandler('typing', TypingForm),
    'choice': ExerciseTypeHandler('choice', ChoiceForm),
    'explanation': ExerciseTypeHandler('explanation', ExplanationForm),
    'listening': ExerciseTypeHandler('listening', ListeningForm)
}


def add_exercise(request, lesson_id, exercise_type):
    exercise_type_handler = exercises_types_handlers[exercise_type]
    lesson = Lesson.objects.get(id=lesson_id)
    exercise = Exercise()
    if request.method == 'POST':
        return handle_spec(request, exercise_type_handler, lesson, exercise)
    else:
        form_class = exercise_type_handler.get_form_class()
        form = form_class(lesson=lesson)
        form.helper.form_action = reverse('lessons:exercises:add_exercise',
                                          kwargs={'lesson_id': lesson.id,
                                                  'exercise_type': exercise_type})
        return render(request, 'exercises/' + str(exercise_type_handler.name) + '.html',
                      {'lesson': lesson, 'form': form})


def modify_exercise(request, lesson_id, exercise_id):
    exercise = Exercise.objects.get(id=exercise_id)
    spec_name = exercise.content_type.name
    exercise_type_handler = exercises_types_handlers[spec_name]

    lesson = Lesson.objects.get(id=lesson_id)
    exercise = Exercise.objects.get(id=exercise_id)
    spec = exercise.spec
    if request.method == 'POST':
        return handle_spec(request, exercise_type_handler, lesson, exercise, spec)
    else:
        form = exercise_type_handler.get_form_class()(instance=spec, lesson=lesson)
        form.helper.form_action = reverse('lessons:exercises:modify_exercise',
                                          kwargs={'lesson_id': lesson.id,
                                                  'exercise_id': exercise_id})
        return render(request, 'exercises/' + str(exercise_type_handler.name) + '.html',
                      {'lesson': lesson, 'exercise': exercise, 'form': form})


def handle_spec(request, exercise_type_handler, lesson, exercise, spec=None):
    form = exercise_type_handler.get_form_class()(data=request.POST or None,
                                                  files=request.FILES or None,
                                                  instance=spec, lesson=lesson)
    if form.is_valid():
        spec = form.save()
        exercise.lesson = lesson
        exercise.spec = spec
        exercise.save()
        return redirect('lessons:modify_lesson', lesson_id=lesson.id)
    else:
        return render(request, 'exercises/' + str(exercise_type_handler) + '.html',
                      {'lesson': lesson, 'exercise': exercise, 'form': form})


def delete_exercise(request, lesson_id, exercise_id):
    exercise = Exercise.objects.get(id=exercise_id)
    exercise.spec.delete()
    exercise.delete()
    return redirect('lessons:modify_lesson', lesson_id=lesson_id)
