from datetime import datetime, timedelta
from itertools import chain
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db import transaction
from django.template import loader
from chinesetool.forms import RegistrationForm

from chinesetool.models import WordZH, WordPL, Subscription, LessonAction, Lesson, ExerciseType, \
    WordZHExerciseDetails, WORD_ZH, Exercise, WordPLExerciseDetails, SentenceZHExerciseDetails, SentencePLExerciseDetails, ExplanationExerciseDetails, \
    EXPLANATION, SENTENCE_PL, SENTENCE_ZH, WORD_PL, SentencePL, SentenceZH, SentenceTranslation, WordTranslation

from django.contrib.auth import authenticate, login, logout
from django.core.urlresolvers import reverse

from django.http import *
from django.template import RequestContext
import json


def login_my(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        login(request, user)
    else:
        pass


@login_required
def index(request):
    template = loader.get_template('chinesetool/index.html')
    context = RequestContext(request)
    return HttpResponse(template.render(context))


@login_required
def learn(request, lesson_id):
    """
    It generates an page with exercise content. It handles ajax queries and sends
    new exercise content to be replaced so that next exercise is displayed.
    :param request: HTTP request for this page
    :param lesson_id: id of the lesson that user will study
    :return: HTTP response showing exercise
    """
    lesson = Lesson.objects.get(pk=lesson_id)
    if request.is_ajax():
        lesson_action = LessonAction.objects.get(lesson=lesson, user=request.user)
        proposition = request.POST.get('proposition')
        if proposition is not None:
            response = lesson_action.check(proposition)
        else:
            if lesson_action.has_next():
                lesson_action.next_exercise()
                response = lesson_action.prepare()
            else:
                response = lesson_action.get_final_response()
        return HttpResponse(json.dumps(response),
                            content_type='application/javascript')
    LessonAction.objects.filter(user=request.user).delete()
    lesson_action = LessonAction.create_lesson_action(request.user, lesson=lesson)
    response = {'lesson_action': lesson_action}
    template = loader.get_template('chinesetool/learn.html')
    context = RequestContext(request, response)
    return HttpResponse(template.render(context))


@transaction.atomic
def register_page(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password1'],
                email=form.cleaned_data['email']
            )
            user.save()
            subscription = Subscription(name=user,
                                        registration_date=datetime.now(),
                                        last_login_date=datetime.now(),
                                        abo_date=datetime.now() + timedelta(days=30))
            subscription.save()

            template = loader.get_template("registration/register_success.html")
            variables = RequestContext(request, {'username': form.cleaned_data['username']})
            output = template.render(variables)
            return HttpResponse(output)
    else:
        form = RegistrationForm()
    template = loader.get_template("registration/register.html")
    context = RequestContext(request, {'form': form})
    return HttpResponse(template.render(context))


def logout_page(request):
    logout(request)
    return HttpResponseRedirect(reverse("chinesetool:index"))


def dictionary(request, source_language):
    if request.POST:
        word_to_search = request.POST['word_to_search']
        translations = []
        matching_words = []
        if request.POST['source_language'] == "polish":
            matching_words = WordPL.objects.filter(word=word_to_search)
        elif request.POST['source_language'] == "chinese":
            matching_words = WordZH.objects.filter(word=word_to_search)
        if matching_words:
            translations = matching_words[0].get_translations()
        return HttpResponse(json.dumps({'translations': translations}), mimetype='application/javascript')
    template = loader.get_template('chinesetool/dictionary.html')
    context = RequestContext(request, {'source_language': source_language})
    return HttpResponse(template.render(context))


@login_required
def choose_language(request):
    template = loader.get_template('chinesetool/choose_language.html')
    context = RequestContext(request)
    return HttpResponse(template.render(context))


def modify_lesson(request, lesson_id):
    """
    Modifies lesson - allows to change requirements and exercises
    :param request:
    :return:
    """
    lesson = Lesson.objects.get(pk=lesson_id)
    if request.POST.get('topic', False):
        lesson.topic = request.POST.get('topic')
        lesson.save()
    if request.POST.get('exercises_number', False):
        lesson.exercises_number = request.POST.get('exercises_number')
        lesson.save()
    if request.POST.get('requirement_to_remove', False):
        requirement_to_remove = Lesson.objects.get(pk=request.POST.get('requirement_to_remove'))
        lesson.requirements.remove(requirement_to_remove)
        lesson.save()
    if request.POST.get('exercise_to_remove', False):
        exercise_to_remove = Exercise.objects.get(pk=request.POST.get('exercise_to_remove'))
        exercise_to_remove.delete()

    requirements = lesson.requirements.all()
    exercises = Exercise.objects.filter(lesson=lesson)
    word_zh_exercises = WordZHExerciseDetails.objects.filter(exercise__in=exercises)
    word_pl_exercises = WordPLExerciseDetails.objects.filter(exercise__in=exercises)
    sentence_zh_exercises = SentenceZHExerciseDetails.objects.filter(exercise__in=exercises)
    sentence_pl_exercises = SentencePLExerciseDetails.objects.filter(exercise__in=exercises)
    explanation_exercises = ExplanationExerciseDetails.objects.filter(exercise__in=exercises)
    exercise_details_list = list(chain(word_zh_exercises,
                                 word_pl_exercises,
                                 sentence_zh_exercises,
                                 sentence_pl_exercises,
                                 explanation_exercises))

    exercise_details_list = sorted(exercise_details_list,
                                   key=lambda instance: instance.exercise.number)

    template = loader.get_template('chinesetool/modify_lesson.html')
    context = RequestContext(request, {'lesson': lesson, 'requirements': requirements,
                                       'exercise_details_list': exercise_details_list,
                                       'word_zh_exercises': word_zh_exercises,
                                       'word_pl_exercises': word_pl_exercises,
                                       'sentence_zh_exercises': sentence_zh_exercises,
                                       'sentence_pl_exercises': sentence_pl_exercises,
                                       'explanation_exercises': explanation_exercises})
    return HttpResponse(template.render(context))


def add_requirement(request, lesson_id):
    """
    Adds requirement for lesson - a lesson that should be learned first
    :param request:
    :return:
    """
    lesson = Lesson.objects.get(pk=lesson_id)
    if request.POST:
        lesson.requirements.add(request.POST.get('new_requirement'))
        lesson.save()
        return HttpResponseRedirect(reverse('chinesetool:modify_lesson', args=(lesson_id,)))
    other_lessons = Lesson.objects.all().order_by('-topic')
    template = loader.get_template('chinesetool/exercise/add_requirement.html')
    context = RequestContext(request, {'other_lessons': other_lessons, 'lesson': lesson})
    return HttpResponse(template.render(context))


def add_exercise_word_zh(request, lesson_id):
    """
    Adds exercise - Chinese word - for a lesson
    :param request:
    :return:
    """
    lesson = Lesson.objects.get(pk=lesson_id)
    if request.POST:
        exercise_type = ExerciseType.objects.get(name=WORD_ZH)
        exercise = Exercise(lesson=lesson, type=exercise_type, number=request.POST.get('number'))
        exercise.save()
        word_zh = WordZH.objects.get_or_create(word=request.POST.get('word_zh'))[0]
        for translation_pl in request.POST.getlist('translations_pl'):
            word_pl = WordPL.objects.get_or_create(word=translation_pl)[0]
            WordTranslation.objects.get_or_create(word_zh=word_zh, word_pl=word_pl)
        new_word_zh_exercise = WordZHExerciseDetails(exercise=exercise, word=word_zh)
        new_word_zh_exercise.save()
        return HttpResponseRedirect(reverse('chinesetool:modify_lesson', args=(lesson_id,)))
    template = loader.get_template('chinesetool/exercise/add_exercise_word_zh.html')
    context = RequestContext(request, {'lesson': lesson})
    return HttpResponse(template.render(context))


def add_exercise_word_pl(request, lesson_id):
    """
    Adds exercise - Polish word - for a lesson
    :param request:
    :return:
    """
    lesson = Lesson.objects.get(pk=lesson_id)
    if request.POST:
        exercise_type = ExerciseType.objects.get(name=WORD_PL)
        exercise = Exercise(lesson=lesson, type=exercise_type, number=request.POST.get('number'))
        exercise.save()
        word_pl = WordPL.objects.get_or_create(word=request.POST.get('word_pl'))[0]
        for translation_zh in request.POST.getlist('translations_zh'):
            word_zh = WordZH.objects.get_or_create(word=translation_zh)[0]
            WordTranslation.objects.get_or_create(word_zh=word_zh, word_pl=word_pl)
        new_word_pl_exercise = WordPLExerciseDetails(exercise=exercise, word=word_pl)
        new_word_pl_exercise.save()
        return HttpResponseRedirect(reverse('chinesetool:modify_lesson', args=(lesson_id,)))
    template = loader.get_template('chinesetool/exercise/add_exercise_word_pl.html')
    context = RequestContext(request, {'lesson': lesson})
    return HttpResponse(template.render(context))


def add_exercise_sentence_zh(request, lesson_id):
    """
    Adds exercise - Chinese sentence - for a lesson
    :param request:
    :return:
    """
    lesson = Lesson.objects.get(pk=lesson_id)
    if request.POST:
        exercise_type = ExerciseType.objects.get(name=SENTENCE_ZH)
        exercise = Exercise(lesson=lesson, type=exercise_type, number=request.POST.get('number'))
        exercise.save()
        sentence_zh = SentenceZH.objects.get_or_create(sentence=request.POST.get('sentence_zh'))[0]
        for translation_pl in request.POST.getlist('translations_pl'):
            sentence_pl = SentencePL.objects.get_or_create(sentence=translation_pl)[0]
            SentenceTranslation.objects.get_or_create(sentence_zh=sentence_zh, sentence_pl=sentence_pl)
        new_sentence_zh_exercise = SentenceZHExerciseDetails(exercise=exercise, sentence=sentence_zh)
        new_sentence_zh_exercise.save()
        return HttpResponseRedirect(reverse('chinesetool:modify_lesson', args=(lesson_id,)))
    template = loader.get_template('chinesetool/exercise/add_exercise_sentence_zh.html')
    context = RequestContext(request, {'lesson': lesson})
    return HttpResponse(template.render(context))


def add_exercise_sentence_pl(request, lesson_id):
    """
    Adds exercise - Polish sentence - for a lesson
    :param request:
    :return:
    """
    lesson = Lesson.objects.get(pk=lesson_id)
    if request.POST:
        exercise_type = ExerciseType.objects.get(name=SENTENCE_PL)
        exercise = Exercise(lesson=lesson, type=exercise_type, number=request.POST.get('number'))
        exercise.save()
        sentence_pl = SentencePL.objects.get_or_create(sentence=request.POST.get('sentence_pl'))[0]
        for translation_zh in request.POST.getlist('translations_zh'):
            sentence_zh = SentenceZH.objects.get_or_create(sentence=translation_zh)[0]
            SentenceTranslation.objects.get_or_create(sentence_zh=sentence_zh, sentence_pl=sentence_pl)
        new_sentence_pl_exercise = SentencePLExerciseDetails(exercise=exercise, sentence=sentence_pl)
        new_sentence_pl_exercise.save()
        return HttpResponseRedirect(reverse('chinesetool:modify_lesson', args=(lesson_id,)))
    template = loader.get_template('chinesetool/exercise/add_exercise_sentence_pl.html')
    context = RequestContext(request, {'lesson': lesson})
    return HttpResponse(template.render(context))


def add_exercise_explanation(request, lesson_id):
    """
    Adds exercise - explanation - for a lesson
    :param request:
    :return:
    """
    lesson = Lesson.objects.get(pk=lesson_id)
    if request.POST:
        exercise_type = ExerciseType.objects.get(name=EXPLANATION)
        exercise = Exercise(lesson=lesson, type=exercise_type, number=request.POST.get('number'))
        exercise.save()
        explanation = ExplanationExerciseDetails(text=request.POST.get('explanation'), exercise=exercise)
        explanation.save()
        return HttpResponseRedirect(reverse('chinesetool:modify_lesson', args=(lesson_id,)))
    template = loader.get_template('chinesetool/exercise/add_exercise_explanation.html')
    context = RequestContext(request, {'lesson': lesson})
    return HttpResponse(template.render(context))


def lessons_map(request):
    """
    Displays available lessons
    :param request:  HTTP request sent by user
    :return: HTTP response showing lessons
    """
    lessons = Lesson.objects.all()
    template = loader.get_template('chinesetool/lessons_map.html')
    context = RequestContext(request, {'lessons': lessons})
    return HttpResponse(template.render(context))


def lessons_management(request):
    """
    Displays available lessons for modifying
    and adding new lessons
    :param request: HTTP request sent by user
    :return: HTTP response showing lessons
    """
    if request.POST.get('topic', False):
        lesson = Lesson(topic=request.POST.get('topic'), exercises_number=0)
        lesson.save()
        return HttpResponseRedirect(reverse('chinesetool:modify_lesson', args=(lesson.id,)))
    lessons = Lesson.objects.all()
    template = loader.get_template('chinesetool/lessons_management.html')
    context = RequestContext(request, {'lessons': lessons})
    return HttpResponse(template.render(context))