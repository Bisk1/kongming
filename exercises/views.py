import logging
import uuid

from django.core.files.base import ContentFile
from django.core.files.storage import default_storage
from django.shortcuts import render, redirect

from models import Lesson, Exercise, Explanation, ExerciseType, Typing
from translations.models import TextTranslation, TextZH, TextPL


logger = logging.getLogger(__name__)


def add_exercise(request, lesson_id):
    exercise_type = request.POST.get('exercise_type')
    return redirect('exercises:add_' + str(exercise_type), lesson_id=lesson_id)


def modify_exercise(request, lesson_id, exercise_id):
    exercise = Exercise.objects.get(id=exercise_id)
    exercise_type = ExerciseType.objects.get(model=exercise.content_type)
    exercise_type_slug = exercise_type.slug
    return redirect('exercises:modify_' + exercise_type_slug, lesson_id=lesson_id, exercise_id=exercise_id)


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
        print request.POST
        if request.POST.get('language') == "pl":
            return handle_modify_typing(request=request, lesson=lesson, exercise=exercise, source_model=TextPL, target_model=TextZH)
        else:
            return handle_modify_typing(request=request, lesson=lesson, exercise=exercise, source_model=TextZH, target_model=TextPL)
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
    explanation_spec = Explanation()
    if request.method == 'POST':
        return handle_explanation_spec(request, lesson, exercise, explanation_spec)
    else:
        return render(request, 'exercises/explanation.html', {'lesson': lesson})


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
        return render(request, 'exercises/explanation.html', {'lesson': lesson, 'exercise': exercise})


def handle_explanation_spec(request, lesson, exercise, explanation_spec):
    explanation_spec.text = request.POST.get('text')
    if 'file' in request.FILES:
        image_file = request.FILES['file']
        image_file.name = save_image_for_exercise(image_file)
        explanation_spec.image = image_file
    explanation_spec.save()
    exercise.lesson = lesson
    exercise.spec = explanation_spec
    exercise.save()
    return redirect('lessons:modify_lesson', lesson_id=lesson.id)


def save_image_for_exercise(file_to_save):
    """
    Generates an unique name for image and saves it in MEDIA_ROOT directory.
    :param file: file to save
    :return: name of the new saved file
    """
    name = unicode(uuid.uuid4()) + "." + file_to_save.name.split(".")[-1]
    default_storage.save(name, ContentFile(file_to_save.read()))
    return name