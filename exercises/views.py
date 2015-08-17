import logging

from django.shortcuts import render, redirect

from models import Lesson, Exercise, ExerciseType, Typing
from translations.models import TextZH, TextPL
from forms import ExplanationForm


logger = logging.getLogger(__name__)


def add_exercise(request, lesson_id):
    exercise_type = request.POST.get('exercise_type')
    return redirect('lessons:exercises:add_' + str(exercise_type), lesson_id=lesson_id)


def modify_exercise(request, lesson_id, exercise_id):
    exercise = Exercise.objects.get(id=exercise_id)
    exercise_type = ExerciseType.objects.get(model=exercise.content_type)
    exercise_type_slug = exercise_type.slug
    return redirect('lessons:exercises:modify_' + exercise_type_slug, lesson_id=lesson_id, exercise_id=exercise_id)


def delete_exercise(request, lesson_id, exercise_id):
    exercise = Exercise.objects.get(id=exercise_id)
    exercise.spec.delete()
    exercise.delete()
    return redirect('lessons:modify_lesson', lesson_id=lesson_id)

# TYPING


def add_typing(request, lesson_id):
    lesson = Lesson.objects.get(id=lesson_id)
    if request.method == 'POST':
        if request.POST.get('language') == "pl":
            return handle_add_typing(request=request, lesson=lesson, source_model=TextPL, target_model=TextZH)
        else:
            return handle_add_typing(request=request, lesson=lesson, source_model=TextZH, target_model=TextPL)
    else:
        return render(request, 'exercises/typing.html', {'lesson': lesson})


def handle_add_typing(request, lesson, source_model, target_model):
    typing_spec = Typing()
    exercise = Exercise(lesson=lesson, number=request.POST.get('number'), spec=typing_spec)
    exercise.save()
    return handle_typing_spec(request, lesson, source_model, target_model, typing_spec)


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
        if request.POST.get('language') == "pl":
            return handle_modify_typing(request=request, lesson=lesson, exercise=exercise,
                                        source_model=TextPL, target_model=TextZH)
        else:
            return handle_modify_typing(request=request, lesson=lesson, exercise=exercise,
                                        source_model=TextZH, target_model=TextPL)
    else:
        return render(request, 'exercises/typing.html', {'lesson': lesson, 'exercise': exercise})


def handle_modify_typing(request, lesson, exercise, source_model, target_model):
    return handle_typing_spec(request, lesson, source_model, target_model, exercise.spec)


def handle_typing_spec(request, lesson, source_model, target_model, typing_spec):
    text_to_translate = source_model.objects.get_or_create(text=request.POST.get('text_to_translate'))[0]
    text_to_translate.get_translations().clear()
    for translation in request.POST.getlist('translations'):
        translated_text = target_model.objects.get_or_create(text=translation)[0]
        text_to_translate.add_translation(translated_text)
    typing_spec.text = text_to_translate
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