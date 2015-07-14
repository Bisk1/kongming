import logging
import uuid

from django.core.files.base import ContentFile
from django.core.files.storage import default_storage
from django.shortcuts import render, redirect
from django.utils.text import slugify

from models import WordZH, WordPL, Lesson, \
    WordZHExercise, Exercise, WordPLExercise, SentenceZHExercise, SentencePLExercise, ExplanationExercise, \
    SentencePL, SentenceZH
from translations.models import SentenceTranslation, WordTranslation


logger = logging.getLogger(__name__)


def add_exercise(request, lesson_id):
    exercise_type = request.POST.get('exercise_type')
    return redirect('exercises:add_' + str(exercise_type), lesson_id=lesson_id)


def modify_exercise(request, lesson_id, exercise_id):
    exercise = Exercise.objects.get(id=exercise_id)
    exercise_type_slug = slugify(unicode(exercise.content_type.name))
    return redirect('exercises:modify_' + exercise_type_slug, lesson_id=lesson_id, exercise_id=exercise_id)


def delete_exercise(request, exercise_id):
    exercise = Exercise.objects.get(id=exercise_id)
    lesson_id = exercise.lesson.id
    exercise.spec.delete()
    exercise.delete()
    return redirect('lessons:delete_exercise', lesson_id=lesson_id)


def add_word_zh_exercise_(request, lesson_id):
    lesson = Lesson.objects.get(id=lesson_id)
    if request.method == 'POST':
        word_zh = WordZH.objects.get_or_create(word=request.POST.get('word_zh'), pinyin=request.POST.get('pinyin'))[0]
        for translation_pl in request.POST.getlist('translations'):
            word_pl = WordPL.objects.get_or_create(word=translation_pl)[0]
            WordTranslation.objects.get_or_create(word_zh=word_zh, word_pl=word_pl)
        word_zh_exercise_spec = WordZHExercise(word=word_zh)
        word_zh_exercise_spec.save()
        exercise = Exercise(lesson=lesson, spec=word_zh_exercise_spec)
        exercise.save()
        return redirect('lessons:modify_lesson', lesson_id=lesson_id)
    else:
        return render(request, 'exercises/word_zh.html', {'lesson': lesson})


def modify_word_zh_exercise(request, lesson_id, exercise_id):
    """
    Modify exercise - Chinese word - for a lesson
    :param request: HTTP request
    :param lesson_id: id of lesson that exercise belongs to
    :param exercise_id: id of the exercise
    :return: HTTP response
    """
    exercise = Exercise.objects.get(id=exercise_id)
    lesson = Lesson.objects.get(id=lesson_id)
    if request.method == 'POST':
        word_zh = WordZH.objects.get_or_create(word=request.POST.get('word_zh'), pinyin=request.POST.get('pinyin'))[0]
        for translation_pl in request.POST.getlist('translations'):
            word_pl = WordPL.objects.get_or_create(word=translation_pl)[0]
            WordTranslation.objects.get_or_create(word_zh=word_zh, word_pl=word_pl)
        return redirect('lessons:modify_lesson', lesson_id=exercise.lesson.id)
        word_zh_exercise_spec = exercise.spec
        word_zh_exercise_spec.word = word_zh
        word_zh_exercise_spec.save()
    else:
        return render(request, 'exercises/word_zh.html', {'lesson': lesson, 'exercise': exercise})


def add_word_pl_exercise(request, lesson_id):
    lesson = Lesson.objects.get(id=lesson_id)
    if request.method == 'POST':
        word_pl = WordPL.objects.get_or_create(word=request.POST.get('word_pl'))[0]
        for translation_zh in request.POST.getlist('translations_zh'):
            word_zh = WordZH.objects.get_or_create(word=translation_zh)[0]
            WordTranslation.objects.get_or_create(word_zh=word_zh, word_pl=word_pl)
        word_pl_exercise_spec = WordPLExercise(word=word_pl)
        word_pl_exercise_spec.save()
        exercise = Exercise(lesson=lesson, number=request.POST.get('number'), spec=word_pl_exercise_spec)
        exercise.save()
        return redirect('lessons:modify_lesson', lesson_id=lesson_id)
    return render(request, 'exercises/word_pl.html', {'lesson': lesson})


def modify_word_pl_exercise(request, lesson_id, exercise_id):
    """
    Modify exercise - Polish word - for a lesson
    :param request: HTTP request
    :param lesson_id: id of lesson that exercise belongs to
    :param exercise_id: id of the exercise
    :return: HTTP response
    """
    exercise = Exercise.objects.get(id=exercise_id)
    lesson = Lesson.objects.get(id=lesson_id)
    if request.method == 'POST':
        word_pl = WordPL.objects.get_or_create(word=request.POST.get('word_pl'))[0]
        for translation_zh in request.POST.getlist('translations'):
            word_zh = WordZH.objects.get_or_create(word=translation_zh)[0]
            WordTranslation.objects.get_or_create(word_zh=word_zh, word_pl=word_pl)
        word_pl_exercise_spec = exercise.spec
        word_pl_exercise_spec.word = word_pl
        word_pl_exercise_spec.save()
        return redirect('lessons:modify_lesson', lesson_id=exercise.lesson.id)
    else:
        return render(request, 'exercises/word_pl.html', {'lesson': lesson, 'exercise': exercise})


def add_sentence_zh_exercise(request, lesson_id):
    lesson = Lesson.objects.get(id=lesson_id)
    if request.method == 'POST':
        sentence_zh = SentenceZH.objects.get_or_create(sentence=request.POST.get('sentence_zh'))[0]
        for translation_pl in request.POST.getlist('translations_pl'):
            sentence_pl = SentencePL.objects.get_or_create(sentence=translation_pl)[0]
            SentenceTranslation.objects.get_or_create(sentence_zh=sentence_zh, sentence_pl=sentence_pl)
        sentence_zh_exercise_spec = SentenceZHExercise(sentence=sentence_zh)
        sentence_zh_exercise_spec.save()
        exercise = Exercise(lesson=lesson, number=request.POST.get('number'), spec=sentence_zh_exercise_spec)
        exercise.save()
        return redirect('lessons:modify_lesson', lesson_id=lesson_id)
    else:
        return render(request, 'exercises/sentence_zh.html', {'lesson': lesson})


def modify_sentence_zh_exercise(request, lesson_id, exercise_id):
    """
    Modify exercise - Chinese sentence - for a lesson
    :param request: HTTP request
    :param lesson_id: id of lesson that exercise belongs to
    :param exercise_id: id of the exercise
    :return: HTTP response
    """
    exercise = Exercise.objects.get(id=exercise_id)
    lesson = Lesson.objects.get(id=lesson_id)
    if request.method == 'POST':
        sentence_zh = SentenceZH.objects.get_or_create(word=request.POST.get('sentence_zh'))[0]
        for translation_zh in request.POST.getlist('translations'):
            sentence_pl = SentencePL.objects.get_or_create(word=translation_zh)[0]
            SentenceTranslation.objects.get_or_create(sentence_zh=sentence_zh, sentence_pl=sentence_pl)
        sentence_zh_exercise_spec = exercise.spec
        sentence_zh_exercise_spec.word = sentence_zh
        sentence_zh_exercise_spec.save()
        return redirect('lessons:modify_lesson', lesson_id=exercise.lesson.id)
    else:
        return render(request, 'exercises/sentence_zh.html', {'lesson': lesson, 'exercise': exercise})


def add_sentence_pl_exercise(request, lesson_id):
    lesson = Lesson.objects.get(id=lesson_id)
    if request.method == 'POST':
        sentence_pl = SentencePL.objects.get_or_create(sentence=request.POST.get('sentence_pl'))[0]
        for translation_zh in request.POST.getlist('translations_zh'):
            sentence_zh = SentenceZH.objects.get_or_create(sentence=translation_zh)[0]
            SentenceTranslation.objects.get_or_create(sentence_zh=sentence_zh, sentence_pl=sentence_pl)
        sentence_pl_exercise_spec = SentencePLExercise(sentence=sentence_pl)
        sentence_pl_exercise_spec.save()
        exercise = Exercise(lesson=lesson, number=request.POST.get('number'), spec=sentence_pl_exercise_spec)
        exercise.save()
        return redirect('lessons:modify_lesson', lesson_id=lesson_id)
    else:
        return render(request, 'exercises/sentence_pl.html', {'lesson': lesson})


def modify_sentence_pl_exercise(request, lesson_id, exercise_id):
    """
    Modify exercise - Polish sentence - for a lesson
    :param request: HTTP request
    :param lesson_id: id of lesson that exercise belongs to
    :param exercise_id: id of the exercise
    :return: HTTP response
    """
    exercise = Exercise.objects.get(id=exercise_id)
    lesson = Lesson.objects.get(id=lesson_id)
    if request.method == 'POST':
        sentence_pl_exercise_spec = exercise.spec
        sentence_pl = SentencePL.objects.get_or_create(word=request.POST.get('sentence_pl'))[0]
        for translation_zh in request.POST.getlist('translations'):
            sentence_zh = SentenceZH.objects.get_or_create(word=translation_zh)[0]
            SentenceTranslation.objects.get_or_create(sentence_zh=sentence_zh, sentence_pl=sentence_pl)
        sentence_pl_exercise_spec = exercise.spec
        sentence_pl_exercise_spec.word = sentence_pl
        sentence_pl_exercise_spec.save()
        return redirect('lessons:modify_lesson', lesson_id=exercise.lesson.id)
    else:
        return render(request, 'exercises/sentence_pl.html', {'lesson': lesson, 'exercise': exercise})


def add_explanation_exercise(request, lesson_id):
    lesson = Lesson.objects.get(id=lesson_id)
    if request.method == 'POST':
        explanation_exercise_spec = ExplanationExercise(text=request.POST.get('text'))
        if 'file' in request.FILES:
            image_file = request.FILES['file']
            image_file.name = save_image_for_exercise(image_file)
            explanation_exercise_spec.image = image_file
        explanation_exercise_spec.save()
        exercise = Exercise(lesson=lesson, number=request.POST.get('number') or None, spec=explanation_exercise_spec)
        exercise.save()
        return redirect('lessons:modify_lesson', lesson_id=lesson_id)
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
    exercise = Exercise.objects.get(id=exercise_id)
    lesson = Lesson.objects.get(id=lesson_id)
    if request.method == 'POST':
        explanation_exercise_spec = exercise.spec
        explanation_exercise_spec.text = request.POST.get('text')
        if 'file' in request.FILES:
            image_file = request.FILES['file']
            image_file.name = save_image_for_exercise(image_file)
            explanation_exercise_spec.image = image_file
        explanation_exercise_spec.save()
        return redirect('lessons:modify_lesson', lesson_id=exercise.lesson.id)
    else:
        return render(request, 'exercises/explanation.html', {'lesson': lesson, 'exercise': exercise})


def save_image_for_exercise(file):
    """
    Generates an unique name for image and saves it in MEDIA_ROOT directory.
    :param file: file to save
    :return: name of the new saved file
    """
    name = unicode(uuid.uuid4()) + "." + file.name.split(".")[-1]
    default_storage.save(name, ContentFile(file.read()))
    return name