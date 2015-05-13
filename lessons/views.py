import logging
from itertools import chain
import uuid

from django.core.files.base import ContentFile
from django.core.files.storage import default_storage
from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from django.http import *
from django.template import loader, RequestContext
from django.views.decorators.csrf import ensure_csrf_cookie

from forms import WordZHExerciseForm, WordPLExerciseForm, SentenceZHExerciseForm, \
    SentencePLExerciseForm, ExplanationExerciseForm, ExplanationImageExerciseForm
from models import WordZH, WordPL, Lesson, \
    WordZHExercise, WORD_ZH, Exercise, WordPLExercise, SentenceZHExercise, SentencePLExercise, ExplanationExercise, \
    EXPLANATION, SENTENCE_PL, SENTENCE_ZH, WORD_PL, SentencePL, SentenceZH, \
    EXPLANATION_IMAGE, ExplanationImageExercise
from translations.models import SentenceTranslation, WordTranslation


logger = logging.getLogger(__name__)


def lessons_management(request):
    """
    Displays available lessons for modifying and adding new lessons
    :param request: HTTP request
    :return: HTTP response
    """
    if request.method == 'POST':
        if request.POST.get('create', False):
            lesson = Lesson(topic=request.POST.get('topic'), exercises_number=0)
            lesson.save()
            return HttpResponseRedirect(reverse('lessons:modify_lesson', args=(lesson.id,)))
        elif request.POST.get('delete', False):
            lesson = Lesson.objects.get(id=request.POST.get('lesson_id'))
            lesson.delete()
    lessons = Lesson.objects.all()
    template = loader.get_template('lessons/lessons_management.html')
    context = RequestContext(request, {'lessons': lessons})
    return HttpResponse(template.render(context))

def modify_lesson(request, lesson_id):

    """
    Modifies lesson - allows to change requirement and exercises
    :param request: HTTP request
    :return: HTTP response
    """
    print request.POST
    lesson = Lesson.objects.get(pk=lesson_id)
    if request.POST.get('topic', False):
        lesson.topic = request.POST.get('topic')
        lesson.save()
    if request.POST.get('exercises_number', False):
        lesson.exercises_number = request.POST.get('exercises_number')
        lesson.save()
    if request.POST.get('new_requirement', False):
        new_requirement_id = request.POST.get('new_requirement')
        if new_requirement_id != "None":
            requirement = Lesson.objects.get(pk=new_requirement_id)
            lesson.requirement = requirement
        else:
            lesson.requirement = None
        lesson.save()
    if request.POST.get('exercise_to_remove', False):
        exercise_to_remove = Exercise.objects.get(pk=request.POST.get('exercise_to_remove'))
        exercise_to_remove.delete()
    other_lessons = Lesson.objects.all().order_by('-topic')
    exercise_details_list = get_exercises(lesson)

    return render(request, 'lessons/modify_lesson.html', {'lesson': lesson,
                                       'exercise_details_list': exercise_details_list, 'other_lessons':other_lessons,
                                      })


def get_exercises(lesson):
    exercises = Exercise.objects.filter(lesson=lesson)
    word_zh_exercises = WordZHExercise.objects.filter(exercise__in=exercises)
    word_pl_exercises = WordPLExercise.objects.filter(exercise__in=exercises)
    sentence_zh_exercises = SentenceZHExercise.objects.filter(exercise__in=exercises)
    sentence_pl_exercises = SentencePLExercise.objects.filter(exercise__in=exercises)
    explanation_exercises = ExplanationExercise.objects.filter(exercise__in=exercises)
    explanation_image_exercises = ExplanationImageExercise.objects.filter(exercise__in=exercises)
    exercise_details_list = list(chain(word_zh_exercises,
                                 word_pl_exercises,
                                 sentence_zh_exercises,
                                 sentence_pl_exercises,
                                 explanation_exercises,
                                 explanation_image_exercises))

    return sorted(exercise_details_list,
                  key=lambda instance: instance.exercise.number)


def display_exercises(request, lesson_id):
    lesson = Lesson.objects.get(pk=lesson_id)
    exercise_details_list = get_exercises(lesson)

    return render(request, 'lessons/exercises.html', {'exercise_details_list': exercise_details_list, 'lesson':lesson})


def delete_lesson(request, lesson_id):
    """
    Delete lesson
    :param request: HTTP request
    :return: HTTP response
    """
    print "Trying to delete lesson " + lesson_id
    Lesson.objects.get(id=lesson_id).delete()
    return redirect('lessons:lessons_management')


def add_exercise_word_zh(request, lesson_id):
    """
    Adds exercise - Chinese word - for a lesson
    :param request: HTTP request
    :param lesson_id: lesson id
    :return: HTTP response
    """
    lesson = Lesson.objects.get(pk=lesson_id)
    if request.method == 'POST':
        form = WordZHExerciseForm(request.POST)
        if form.is_valid():
            exercise_type = WORD_ZH
            exercise = Exercise(lesson=lesson, type=exercise_type, number=request.POST.get('number'))
            exercise.save()
            word_zh = WordZH.objects.get_or_create(word=request.POST.get('word_zh'))[0]
            for translation_pl in request.POST.getlist('translations_pl'):
                word_pl = WordPL.objects.get_or_create(word=translation_pl)[0]
                WordTranslation.objects.get_or_create(word_zh=word_zh, word_pl=word_pl)
            new_word_zh_exercise = WordZHExercise(exercise=exercise, word=word_zh)
            new_word_zh_exercise.save()
            return HttpResponseRedirect(reverse('lessons:modify_lesson', args=(lesson_id,)))
    else:
        form = WordZHExerciseForm()
    return render(request, 'lessons/exercise/word_zh.html', {'form': form, 'lesson': lesson})


def add_exercise_word_pl(request, lesson_id):
    """
    Adds exercise - Polish word - for a lesson
    :param request: HTTP request
    :param lesson_id: lesson id
    :return: HTTP response
    """
    lesson = Lesson.objects.get(pk=lesson_id)
    if request.method == 'POST':
        form = WordPLExerciseForm(request.POST)
        if form.is_valid():
            exercise_type = WORD_PL
            exercise = Exercise(lesson=lesson, type=exercise_type, number=request.POST.get('number'))
            exercise.save()
            word_pl = WordPL.objects.get_or_create(word=request.POST.get('word_pl'))[0]
            for translation_zh in request.POST.getlist('translations_zh'):
                word_zh = WordZH.objects.get_or_create(word=translation_zh)[0]
                WordTranslation.objects.get_or_create(word_zh=word_zh, word_pl=word_pl)
            new_word_pl_exercise = WordPLExercise(exercise=exercise, word=word_pl)
            new_word_pl_exercise.save()
            return HttpResponseRedirect(reverse('lessons:modify_lesson', args=(lesson_id,)))
    else:
        form = WordPLExerciseForm()
    return render(request, 'lessons/exercise/word_pl.html', {'form': form, 'lesson': lesson})


def add_exercise_sentence_zh(request, lesson_id):
    """
    Adds exercise - Chinese sentence - for a lesson
    :param request: HTTP request
    :param lesson_id: lesson id
    :return: HTTP response
    """
    lesson = Lesson.objects.get(pk=lesson_id)
    if request.method == 'POST':
        form = SentenceZHExerciseForm(request.POST)
        if form.is_valid():
            exercise_type = SENTENCE_ZH
            exercise = Exercise(lesson=lesson, type=exercise_type, number=request.POST.get('number'))
            exercise.save()
            sentence_zh = SentenceZH.objects.get_or_create(sentence=request.POST.get('sentence_zh'))[0]
            for translation_pl in request.POST.getlist('translations_pl'):
                sentence_pl = SentencePL.objects.get_or_create(sentence=translation_pl)[0]
                SentenceTranslation.objects.get_or_create(sentence_zh=sentence_zh, sentence_pl=sentence_pl)
            new_sentence_zh_exercise = SentenceZHExercise(exercise=exercise, sentence=sentence_zh)
            new_sentence_zh_exercise.save()
            return HttpResponseRedirect(reverse('lessons:modify_lesson', args=(lesson_id,)))
    else:
        form = SentenceZHExerciseForm()
    return render(request, 'lessons/exercise/sentence_zh.html', {'form': form, 'lesson': lesson})


def add_exercise_sentence_pl(request, lesson_id):
    """
    Adds exercise - Polish sentence - for a lesson
    :param request: HTTP request
    :param lesson_id: lesson id
    :return: HTTP response
    """
    lesson = Lesson.objects.get(pk=lesson_id)
    if request.method == 'POST':
        form = SentencePLExerciseForm(request.POST)
        if form.is_valid():
            exercise_type = SENTENCE_PL
            exercise = Exercise(lesson=lesson, type=exercise_type, number=request.POST.get('number'))
            exercise.save()
            sentence_pl = SentencePL.objects.get_or_create(sentence=request.POST.get('sentence_pl'))[0]
            for translation_zh in request.POST.getlist('translations_zh'):
                sentence_zh = SentenceZH.objects.get_or_create(sentence=translation_zh)[0]
                SentenceTranslation.objects.get_or_create(sentence_zh=sentence_zh, sentence_pl=sentence_pl)
            new_sentence_pl_exercise = SentencePLExercise(exercise=exercise, sentence=sentence_pl)
            new_sentence_pl_exercise.save()
            return HttpResponseRedirect(reverse('lessons:modify_lesson', args=(lesson_id,)))
    else:
        form = SentencePLExerciseForm()
    return render(request, 'lessons/exercise/sentence_pl.html', {'form': form, 'lesson': lesson})


def add_exercise_explanation(request, lesson_id):
    """
    Adds exercise - explanation - for a lesson
    :param request: HTTP request
    :param lesson_id: lesson id
    :return: HTTP response
    """
    lesson = Lesson.objects.get(pk=lesson_id)
    if request.method == 'POST':
        form = ExplanationExerciseForm(request.POST)
        if form.is_valid():
            exercise_type = EXPLANATION
            exercise = Exercise(lesson=lesson, type=exercise_type, number=request.POST.get('number') or None)
            exercise.save()
            explanation = ExplanationExercise(text=request.POST.get('text'), exercise=exercise)
            explanation.save()
            return HttpResponseRedirect(reverse('lessons:modify_lesson', args=(lesson_id,)))
    else:
        form = ExplanationExerciseForm()
    return render(request, 'lessons/exercise/explanation.html', {'form': form, 'lesson': lesson})


def add_exercise_explanation_image(request, lesson_id):
    """
    Adds exercise - explanation with image - for a lesson
    :param request: HTTP request
    :param lesson_id: lesson id
    :return: HTTP response
    """
    lesson = Lesson.objects.get(pk=lesson_id)
    if request.method == 'POST':
        form = ExplanationImageExerciseForm(request.POST, request.FILES)
        if form.is_valid():
            exercise_type = EXPLANATION_IMAGE
            exercise = Exercise(lesson=lesson, type=exercise_type, number=request.POST.get('number'))
            exercise.save()
            file = request.FILES['file']
            file.name = unicode(uuid.uuid4()) + "." + file.name.split(".")[-1]
            explanation_image = ExplanationImageExercise(text=request.POST.get('text'), image=file, exercise=exercise)
            explanation_image.save()
            return HttpResponseRedirect(reverse('lessons:modify_lesson', args=(lesson_id,)))
    else:
        form = ExplanationImageExerciseForm()
    return render(request, 'lessons/exercise/explanation_image.html', {'form': form, 'lesson': lesson})


def save_image_for_exercise(file):
    """
    Generates an unique name for image and saves it in MEDIA_ROOT directory.
    :param file: file to save
    :return: name of the new saved file
    """
    name = unicode(uuid.uuid4()) + "." + file.name.split(".")[-1]
    default_storage.save(name, ContentFile(file.read()))
    return name