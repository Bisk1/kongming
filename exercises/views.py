import logging
import uuid

from django.core.files.base import ContentFile
from django.core.files.storage import default_storage
from django.shortcuts import render, redirect

from models import Lesson, \
    Exercise, Explanation, \
    ExerciseType, Typing
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


def add_typing(request, lesson_id):
    lesson = Lesson.objects.get(id=lesson_id)
    return render(request, 'exercises/typing.html', {'lesson': lesson})


def modify_typing(request, lesson_id, exercise_id):
    exercise = Exercise.objects.get(id=exercise_id)
    if exercise.spec.content_type.model_class() == TextZH:
        return redirect('exercises:modify_typing_zh', lesson_id=lesson_id, exercise_id=exercise_id)
    else:
        return redirect('exercises:modify_typing_pl', lesson_id=lesson_id, exercise_id=exercise_id)


def add_typing_zh_exercise(request, lesson_id):
    lesson = Lesson.objects.get(id=lesson_id)
    if request.method == 'POST':
        text_zh = TextZH.objects.get_or_create(text=request.POST.get('text_zh'))[0]
        for translation_pl in request.POST.getlist('translations'):
            text_pl = TextPL.objects.get_or_create(text=translation_pl)[0]
            TextTranslation.objects.get_or_create(text_zh=text_zh, text_pl=text_pl)
        text_zh_exercise_spec = Typing(text=text_zh)
        text_zh_exercise_spec.save()
        exercise = Exercise(lesson=lesson, number=request.POST.get('number'), spec=text_zh_exercise_spec)
        exercise.save()
        return redirect('lessons:modify_lesson', lesson_id=lesson_id)
    else:
        return render(request, 'exercises/typing_zh.html', {'lesson': lesson})


def modify_typing_zh_exercise(request, lesson_id, exercise_id):
    """
    Modify exercise - Chinese text - for a lesson
    :param request: HTTP request
    :param lesson_id: id of lesson that exercise belongs to
    :param exercise_id: id of the exercise
    :return: HTTP response
    """
    exercise = Exercise.objects.get(id=exercise_id)
    lesson = Lesson.objects.get(id=lesson_id)
    if request.method == 'POST':
        text_zh = TextZH.objects.get_or_create(text=request.POST.get('text_zh'))[0]
        for translation_pl in request.POST.getlist('translations'):
            text_pl = TextPL.objects.get_or_create(text=translation_pl)[0]
            TextTranslation.objects.get_or_create(text_zh=text_zh, text_pl=text_pl)
        text_zh_exercise_spec = exercise.spec
        text_zh_exercise_spec.text = text_zh
        text_zh_exercise_spec.save()
        return redirect('lessons:modify_lesson', lesson_id=exercise.lesson.id)
    else:
        return render(request, 'exercises/typing_zh.html', {'lesson': lesson, 'exercise': exercise})


def add_typing_pl_exercise(request, lesson_id):
    lesson = Lesson.objects.get(id=lesson_id)
    if request.method == 'POST':
        text_pl = TextPL.objects.get_or_create(text=request.POST.get('text_pl'))[0]
        for translation_zh in request.POST.getlist('translations'):
            text_zh = TextZH.objects.get_or_create(text=translation_zh)[0]
            TextTranslation.objects.get_or_create(text_zh=text_zh, text_pl=text_pl)
        text_pl_exercise_spec = Typing(text=text_pl)
        text_pl_exercise_spec.save()
        exercise = Exercise(lesson=lesson, number=request.POST.get('number'), spec=text_pl_exercise_spec)
        exercise.save()
        return redirect('lessons:modify_lesson', lesson_id=lesson_id)
    else:
        return render(request, 'exercises/typing_pl.html', {'lesson': lesson})


def modify_typing_pl_exercise(request, lesson_id, exercise_id):
    """
    Modify exercise - Polish text - for a lesson
    :param request: HTTP request
    :param lesson_id: id of lesson that exercise belongs to
    :param exercise_id: id of the exercise
    :return: HTTP response
    """
    exercise = Exercise.objects.get(id=exercise_id)
    lesson = Lesson.objects.get(id=lesson_id)
    if request.method == 'POST':
        text_pl = TextPL.objects.get_or_create(text=request.POST.get('text_pl'))[0]
        for translation_zh in request.POST.getlist('translations'):
            text_zh = TextZH.objects.get_or_create(text=translation_zh)[0]
            TextTranslation.objects.get_or_create(text_zh=text_zh, text_pl=text_pl)
        text_pl_exercise_spec = exercise.spec
        text_pl_exercise_spec.word = text_pl
        text_pl_exercise_spec.save()
        return redirect('lessons:modify_lesson', lesson_id=exercise.lesson.id)
    else:
        return render(request, 'exercises/typing_pl.html', {'lesson': lesson, 'exercise': exercise})


def add_explanation_exercise(request, lesson_id):
    lesson = Lesson.objects.get(id=lesson_id)
    exercise = Exercise()
    explanation_exercise_spec = Explanation()
    if request.method == 'POST':
        return handle_explanation_spec(request, lesson, exercise, explanation_exercise_spec)
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
    explanation_exercise_spec = exercise.spec
    if request.method == 'POST':
        return handle_explanation_spec(request, lesson, exercise, explanation_exercise_spec)
    else:
        return render(request, 'exercises/explanation.html', {'lesson': lesson, 'exercise': exercise})


def handle_explanation_spec(request, lesson, exercise, explanation_exercise_spec):
    explanation_exercise_spec.text = request.POST.get('text')
    if 'file' in request.FILES:
        image_file = request.FILES['file']
        image_file.name = save_image_for_exercise(image_file)
        explanation_exercise_spec.image = image_file
    explanation_exercise_spec.save()
    exercise.lesson = lesson
    exercise.spec = explanation_exercise_spec
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