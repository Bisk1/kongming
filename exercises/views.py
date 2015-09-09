import logging

from django.shortcuts import render, redirect

from exercises.models import Lesson, Exercise, Typing
from translations.models import BusinessText
from exercises.forms import ExplanationForm, ChoiceForm

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
    if request.method == 'POST':
        return handle_add_typing(request=request, lesson=lesson)
    else:
        return render(request, 'exercises/typing.html', {'lesson': lesson})


def handle_add_typing(request, lesson):
    typing_spec = Typing()
    response = handle_typing_spec(request, lesson, typing_spec)
    exercise = Exercise(lesson=lesson, number=request.POST.get('number'), spec=typing_spec)
    exercise.save()
    return response


def modify_typing(request, lesson_id, exercise_id):
    """
    Modify typing exercise
    :param request: HTTP request
    :param lesson_id: id of lesson that exercise belongs to
    :param exercise_id: id of the exercise
    :return: HTTP response
    """
    exercise = Exercise.objects.get(id=exercise_id)
    lesson = Lesson.objects.get(id=lesson_id)
    if request.method == 'POST':
        return handle_typing_spec(request=request, lesson=lesson, typing_spec=exercise.spec)
    else:
        return render(request, 'exercises/typing.html', {'lesson': lesson, 'exercise': exercise})


def handle_typing_spec(request, lesson, typing_spec):
    text_to_translate = request.POST.get('text_to_translate')
    translations = request.POST.getlist('translations')
    language = request.POST.get('language')
    business_text_to_translate, _ = BusinessText.objects.get_or_create(text=text_to_translate, language=language)
    business_text_to_translate.translations.clear()
    for translation in translations:
        business_text_to_translate.add_translation(translation)
    typing_spec.text_to_translate = business_text_to_translate
    typing_spec.save()
    return redirect('lessons:modify_lesson', lesson_id=lesson.id)


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
