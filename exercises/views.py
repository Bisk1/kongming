import logging

from django.shortcuts import render, redirect

from exercises.models import Lesson, Exercise
from django.core.urlresolvers import reverse
from exercises.forms import ExplanationForm, ChoiceForm, TypingForm

logger = logging.getLogger(__name__)


def add_exercise(request, lesson_id):
    exercise_type = request.POST.get('exercise_type')
    return redirect('lessons:exercises:add_' + str(exercise_type), lesson_id=lesson_id)


def modify_exercise(request, lesson_id, exercise_id):
    exercise = Exercise.objects.get(id=exercise_id)
    spec_name = exercise.content_type.name
    return redirect('lessons:exercises:modify_' + spec_name, lesson_id=lesson_id, exercise_id=exercise_id)


def delete_exercise(request, lesson_id, exercise_id):
    exercise = Exercise.objects.get(id=exercise_id)
    exercise.spec.delete()
    exercise.delete()
    return redirect('lessons:modify_lesson', lesson_id=lesson_id)

# TYPING


def add_typing(request, lesson_id):
    lesson = Lesson.objects.get(id=lesson_id)
    exercise = Exercise()
    if request.method == 'POST':
        return handle_typing_spec(request, lesson, exercise)
    else:
        form = TypingForm()
        return render(request, 'exercises/typing.html', {'lesson': lesson, 'form': form})


def modify_typing(request, lesson_id, exercise_id):
    """
    Modify typing exercise
    :param request: HTTP request
    :param lesson_id: id of lesson that exercise belongs to
    :param exercise_id: id of the exercise
    :return: HTTP response
    """
    lesson = Lesson.objects.get(id=lesson_id)
    exercise = Exercise.objects.get(id=exercise_id)
    typing_spec = exercise.spec
    if request.method == 'POST':
        return handle_typing_spec(request, lesson, exercise, typing_spec)
    else:
        form = TypingForm(instance=typing_spec)
        return render(request, 'exercises/typing.html', {'lesson': lesson, 'exercise': exercise, 'form': form})


def handle_typing_spec(request, lesson, exercise, typing_spec=None):
    form = TypingForm(data=request.POST or None, instance=typing_spec)
    if form.is_valid():
        typing_spec = form.save()
        exercise.lesson = lesson
        exercise.spec = typing_spec
        exercise.save()
        return redirect('lessons:modify_lesson', lesson_id=lesson.id)
    else:
        return render(request, 'exercises/typing.html', {'lesson': lesson, 'exercise': exercise, 'form': form})


# EXPLANATION


def add_explanation_exercise(request, lesson_id):
    lesson = Lesson.objects.get(id=lesson_id)
    exercise = Exercise()
    if request.method == 'POST':
        return handle_explanation_spec(request, lesson, exercise)
    else:
        form = ExplanationForm()
        return render(request, 'exercises/explanation.html', {'lesson': lesson, 'form': form})


def modify_explanation_exercise(request, lesson_id, exercise_id):
    """
    Modify exercise - explanation - for a lesson
    :param request: HTTP request
    :param lesson_id: id of lesson that exercise belongs to
    :param exercise_id: id of the exercise
    :return: HTTP response
    """
    lesson = Lesson.objects.get(id=lesson_id)
    exercise = Exercise.objects.get(id=exercise_id)
    explanation_spec = exercise.spec
    if request.method == 'POST':
        return handle_explanation_spec(request, lesson, exercise, explanation_spec)
    else:
        form = ExplanationForm(instance=explanation_spec)
        return render(request, 'exercises/explanation.html', {'lesson': lesson, 'exercise': exercise, 'form': form})


def handle_explanation_spec(request, lesson, exercise, explanation_spec=None):
    form = ExplanationForm(request.POST, request.FILES, instance=explanation_spec)
    if form.is_valid():
        explanation_spec = form.save()
        exercise.lesson = lesson
        exercise.spec = explanation_spec
        exercise.save()
        return redirect('lessons:modify_lesson', lesson_id=lesson.id)
    else:
        return render(request, 'exercises/explanation.html', {'lesson': lesson, 'exercise': exercise, 'form': form})


# CHOICE


def add_choice_exercise(request, lesson_id):
    lesson = Lesson.objects.get(id=lesson_id)
    exercise = Exercise()
    if request.method == 'POST':
        return handle_choice_spec(request, lesson, exercise)
    else:
        form = ChoiceForm()
        form.helper.form_action = reverse('lessons:exercises:add_choice', kwargs={'lesson_id': lesson.id})
        return render(request, 'exercises/choice.html', {'lesson': lesson, 'form': form})


def modify_choice_exercise(request, lesson_id, exercise_id):
    """
    Modify exercise - choice - for a lesson
    :param request: HTTP request
    :param lesson_id: id of lesson that exercise belongs to
    :param exercise_id: id of the exercise
    :return: HTTP response
    """
    lesson = Lesson.objects.get(id=lesson_id)
    exercise = Exercise.objects.get(id=exercise_id)
    choice_spec = exercise.spec
    if request.method == 'POST':
        return handle_choice_spec(request, lesson, exercise, choice_spec)
    else:
        form = ChoiceForm(instance=choice_spec)
        form.helper.form_action = reverse('lessons:exercises:modify_choice', kwargs={'lesson_id': lesson.id, 'exercise_id': exercise_id})
        return render(request, 'exercises/choice.html', {'lesson': lesson, 'exercise': exercise, 'form': form})


def handle_choice_spec(request, lesson, exercise, choice_spec=None):
    form = ChoiceForm(data=request.POST or None, instance=choice_spec)
    if form.is_valid():
        choice_spec = form.save()
        exercise.lesson = lesson
        exercise.spec = choice_spec
        exercise.save()
        return redirect('lessons:modify_lesson', lesson_id=lesson.id)
    else:
        return render(request, 'exercises/choice.html', {'lesson': lesson, 'exercise': exercise, 'form': form})
