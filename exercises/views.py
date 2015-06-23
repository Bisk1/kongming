import logging
import uuid

from django.core.files.base import ContentFile
from django.core.files.storage import default_storage
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse

from models import WordZH, WordPL, Lesson, \
    WordZHExercise, WORD_ZH, Exercise, WordPLExercise, SentenceZHExercise, SentencePLExercise, ExplanationExercise, \
    EXPLANATION, SENTENCE_PL, SENTENCE_ZH, WORD_PL, SentencePL, SentenceZH, exercise_type_to_name_map
from translations.models import SentenceTranslation, WordTranslation


logger = logging.getLogger(__name__)


def add_exercise(request, lesson_id):
    exercise_type = request.POST.get('exercise_type')
    return redirect('exercises:add_exercise_' + exercise_type, lesson_id=lesson_id)


def modify_exercise(request, exercise_id):
    exercise = Exercise.objects.get(id=exercise_id)
    exercise_type = exercise_type_to_name_map.get(exercise.type)
    return redirect('exercises:modify_exercise_' + exercise_type, exercise_id=exercise_id)


def delete_exercise(request, exercise_id):
    exercise = Exercise.objects.get(id=exercise_id)
    lesson_id = exercise.lesson.id
    exercise.delete()
    return redirect('lessons:modify_lesson', lesson_id=lesson_id)


def add_exercise_word_zh(request, lesson_id):
    lesson = Lesson.objects.get(id=lesson_id)
    if request.method == 'POST':
        exercise_type = WORD_ZH
        exercise = Exercise(lesson=lesson, type=exercise_type)
        exercise.save()
        word_zh = WordZH.objects.get_or_create(word=request.POST.get('word_zh'), pinyin=request.POST.get('pinyin'))[0]
        for translation_pl in request.POST.getlist('translations'):
            word_pl = WordPL.objects.get_or_create(word=translation_pl)[0]
            WordTranslation.objects.get_or_create(word_zh=word_zh, word_pl=word_pl)
        new_exercise_word_zh = WordZHExercise(exercise=exercise, word=word_zh)
        new_exercise_word_zh.save()
        return redirect('lessons:modify_lesson', lesson_id=lesson_id)
    else:
        return render(request, 'exercises/word_zh.html', {'lesson': lesson})


def modify_exercise_word_zh(request, exercise_id):
    """
    Modify exercise - Chinese word - for a lesson
    :param request: HTTP request
    :param lesson_id: id of lesson that exercise belongs to
    :param exercise_id: id of the exercise
    :return: HTTP response
    """
    exercise = Exercise.objects.get(id=exercise_id)
    exercise_word_zh = WordZHExercise.objects.get(exercise=exercise)
    if request.method == 'POST':
        word_zh = WordZH.objects.get_or_create(word=request.POST.get('word_zh'), pinyin=request.POST.get('pinyin'))[0]
        for translation_pl in request.POST.getlist('translations'):
            word_pl = WordPL.objects.get_or_create(word=translation_pl)[0]
            WordTranslation.objects.get_or_create(word_zh=word_zh, word_pl=word_pl)
        exercise_word_zh.word = word_zh
        exercise_word_zh.save()
        return redirect('lessons:modify_lesson', lesson_id=exercise.lesson.id)
    else:
        return render(request, 'exercises/word_zh.html', {'exercise_details': exercise_word_zh})


def add_exercise_word_pl(request, lesson_id):
    lesson = Lesson.objects.get(id=lesson_id)
    if request.method == 'POST':
        exercise_type = WORD_PL
        exercise = Exercise(lesson=lesson, type=exercise_type, number=request.POST.get('number'))
        exercise.save()
        word_pl = WordPL.objects.get_or_create(word=request.POST.get('word_pl'))[0]
        for translation_zh in request.POST.getlist('translations_zh'):
            word_zh = WordZH.objects.get_or_create(word=translation_zh)[0]
            WordTranslation.objects.get_or_create(word_zh=word_zh, word_pl=word_pl)
        new_exercise_word_pl = WordPLExercise(exercise=exercise, word=word_pl)
        new_exercise_word_pl.save()
        return redirect('lessons:modify_lesson', lesson_id=lesson_id)
    return render(request, 'exercises/word_pl.html', {'lesson': lesson})


def modify_exercise_word_pl(request, exercise_id):
    """
    Modify exercise - Polish word - for a lesson
    :param request: HTTP request
    :param lesson_id: id of lesson that exercise belongs to
    :param exercise_id: id of the exercise
    :return: HTTP response
    """
    exercise = Exercise.objects.get(id=exercise_id)
    exercise_word_pl = WordPLExercise.objects.get(exercise=exercise)
    if request.method == 'POST':
        word_pl = WordPL.objects.get_or_create(word=request.POST.get('word_pl'))[0]
        for translation_zh in request.POST.getlist('translations'):
            word_zh = WordZH.objects.get_or_create(word=translation_zh)[0]
            WordTranslation.objects.get_or_create(word_zh=word_zh, word_pl=word_pl)
        exercise_word_pl.word = word_pl
        exercise_word_pl.save()
        return redirect('lessons:modify_lesson', lesson_id=exercise.lesson.id)
    else:
        return render(request, 'exercises/word_pl.html', {'exercise_details': exercise_word_pl})


def add_exercise_sentence_zh(request, lesson_id):
    lesson = Lesson.objects.get(id=lesson_id)
    if request.method == 'POST':
        exercise_type = SENTENCE_ZH
        exercise = Exercise(lesson=lesson, type=exercise_type, number=request.POST.get('number'))
        exercise.save()
        sentence_zh = SentenceZH.objects.get_or_create(sentence=request.POST.get('sentence_zh'))[0]
        for translation_pl in request.POST.getlist('translations_pl'):
            sentence_pl = SentencePL.objects.get_or_create(sentence=translation_pl)[0]
            SentenceTranslation.objects.get_or_create(sentence_zh=sentence_zh, sentence_pl=sentence_pl)
        new_exercise_sentence_zh = SentenceZHExercise(exercise=exercise, sentence=sentence_zh)
        new_exercise_sentence_zh.save()
        return redirect('lessons:modify_lesson', lesson_id=lesson_id)
    else:
        return render(request, 'exercises/sentence_zh.html', {'lesson': lesson})


def modify_exercise_sentence_zh(request, exercise_id):
    """
    Modify exercise - Chinese sentence - for a lesson
    :param request: HTTP request
    :param lesson_id: id of lesson that exercise belongs to
    :param exercise_id: id of the exercise
    :return: HTTP response
    """
    exercise = Exercise.objects.get(id=exercise_id)
    exercise_sentence_zh = SentenceZHExercise.objects.get(exercise=exercise)
    if request.method == 'POST':
        sentence_zh = SentenceZH.objects.get_or_create(word=request.POST.get('sentence_zh'))[0]
        for translation_zh in request.POST.getlist('translations'):
            sentence_pl = SentencePL.objects.get_or_create(word=translation_zh)[0]
            SentenceTranslation.objects.get_or_create(sentence_zh=sentence_zh, sentence_pl=sentence_pl)
        exercise_sentence_zh.word = sentence_zh
        exercise_sentence_zh.save()
        return redirect('lessons:modify_lesson', lesson_id=exercise.lesson.id)
    else:
        return render(request, 'exercises/sentence_zh.html', {'exercise_details': exercise_sentence_zh})


def add_exercise_sentence_pl(request, lesson_id):
    lesson = Lesson.objects.get(id=lesson_id)
    if request.method == 'POST':
        exercise_type = SENTENCE_PL
        exercise = Exercise(lesson=lesson, type=exercise_type, number=request.POST.get('number'))
        exercise.save()
        sentence_pl = SentencePL.objects.get_or_create(sentence=request.POST.get('sentence_pl'))[0]
        for translation_zh in request.POST.getlist('translations_zh'):
            sentence_zh = SentenceZH.objects.get_or_create(sentence=translation_zh)[0]
            SentenceTranslation.objects.get_or_create(sentence_zh=sentence_zh, sentence_pl=sentence_pl)
        new_sentence_pl_exercise = SentencePLExercise(exercise=exercise, sentence=sentence_pl)
        new_sentence_pl_exercise.save()
        return redirect('lessons:modify_lesson', lesson_id=lesson_id)
    else:
        return render(request, 'exercises/sentence_pl.html', {'lesson': lesson})


def modify_exercise_sentence_pl(request, exercise_id):
    """
    Modify exercise - Polish sentence - for a lesson
    :param request: HTTP request
    :param lesson_id: id of lesson that exercise belongs to
    :param exercise_id: id of the exercise
    :return: HTTP response
    """
    exercise = Exercise.objects.get(id=exercise_id)
    exercise_sentence_pl = SentencePLExercise.objects.get(exercise=exercise)
    if request.method == 'POST':
        sentence_pl = SentencePL.objects.get_or_create(word=request.POST.get('sentence_pl'))[0]
        for translation_zh in request.POST.getlist('translations'):
            sentence_zh = SentenceZH.objects.get_or_create(word=translation_zh)[0]
            SentenceTranslation.objects.get_or_create(sentence_zh=sentence_zh, sentence_pl=sentence_pl)
        exercise_sentence_pl.word = sentence_pl
        exercise_sentence_pl.save()
        return redirect('lessons:modify_lesson', lesson_id=exercise.lesson.id)
    else:
        return render(request, 'exercises/sentence_pl.html', {'exercise_details': exercise_sentence_pl})


def add_exercise_explanation(request, lesson_id):
    lesson = Lesson.objects.get(id=lesson_id)
    if request.method == 'POST':
        exercise_type = EXPLANATION
        exercise = Exercise(lesson=lesson, type=exercise_type, number=request.POST.get('number') or None)
        exercise.save()
        exercise_explanation = ExplanationExercise(text=request.POST.get('text'), exercise=exercise)
        if 'file' in request.FILES:
            image_file = request.FILES['file']
            image_file.name = save_image_for_exercise(image_file)
            exercise_explanation.image = image_file
        exercise_explanation.save()
        return redirect('lessons:modify_lesson', lesson_id=lesson_id)
    else:
        return render(request, 'exercises/explanation.html', {'lesson': lesson})


def modify_exercise_explanation(request, exercise_id):
    """
    Modify exercise - explanation - for a lesson
    :param request: HTTP request
    :param lesson_id: id of lesson that exercise belongs to
    :param exercise_id: id of the exercise
    :return: HTTP response
    """
    exercise = Exercise.objects.get(id=exercise_id)
    exercise_explanation = ExplanationExercise.objects.get(exercise=exercise)
    if request.method == 'POST':
        exercise_explanation.text = request.POST.get('text')
        if 'file' in request.FILES:
            image_file = request.FILES['file']
            image_file.name = save_image_for_exercise(image_file)
            exercise_explanation.image = image_file
        exercise_explanation.save()
        return redirect('lessons:modify_lesson', lesson_id=exercise.lesson.id)
    else:
        return render(request, 'exercises/explanation.html', {'exercise_details': exercise_explanation})


def save_image_for_exercise(file):
    """
    Generates an unique name for image and saves it in MEDIA_ROOT directory.
    :param file: file to save
    :return: name of the new saved file
    """
    name = unicode(uuid.uuid4()) + "." + file.name.split(".")[-1]
    default_storage.save(name, ContentFile(file.read()))
    return name