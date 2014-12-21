from datetime import datetime, timedelta
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db import transaction
from django.shortcuts import redirect
from django.template import loader
from chinesetool.forms import RegistrationForm

from chinesetool.models import WordZH, WordPL, WordTranslation, Subscription, LessonAction, Lesson, ExerciseType

from django.contrib.auth import authenticate, login, logout
from django.core.urlresolvers import reverse
from chinesetool.utils.model_utils import get_random


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
    latest_words_list = WordZH.objects.all().order_by('-lesson')[:5]
    template = loader.get_template('chinesetool/index.html')
    context = RequestContext(request, {
        'latest_words_list': latest_words_list,
    })
    return HttpResponse(template.render(context))


@login_required
def translate_word(request):
    """
    It generates a form with chinese word to be guessed and an input box for
    the user to type in his guess. If a guess has already been made, it shows results.
    :param request: http request for this page
    :return: http response showing guessing panel
    """
    if request.POST:
        lesson_action = LessonAction.objects.get(pk=request.POST.get('lesson_id'))
        proposition = request.POST.get('proposition')
        if proposition is not None:
            response = lesson_action.check(proposition)
            return HttpResponse(json.dumps(response), content_type='application/javascript')
        else:
            if lesson_action.has_next():
                lesson_action.next_exercise()
                response = lesson_action.prepare()
            else:
                response = lesson_action.get_final_response()
            return HttpResponse(json.dumps(response), content_type='application/javascript')

    new_lesson_action = LessonAction.create_word_lesson_action(request.user)
    response = {'lesson_action': new_lesson_action}
    template = loader.get_template('chinesetool/translate_word.html')
    context = RequestContext(request, response)
    return HttpResponse(template.render(context))


@login_required
def translate_sentence(request):
    """
    It generates a form with chinese sentence to be guessed and an input box for
    the user to type in his guess. If a guess has already been made, it shows results.
    :param request: http request for this page
    :return: http response showing guessing panel
    """
    if request.POST:
        lesson_action = LessonAction.objects.get(pk=request.POST.get('lesson_id'))
        proposition = request.POST.get('proposition')
        if proposition is not None:
            response = lesson_action.check(proposition)
            return HttpResponse(json.dumps(response), content_type='application/javascript')
        else:
            if lesson_action.has_next():
                lesson_action.next_exercise()
                response = lesson_action.prepare()
            else:
                response = lesson_action.get_final_response()
            return HttpResponse(json.dumps(response), content_type='application/javascript')

    new_lesson_action = LessonAction.create_sentence_lesson_action(request.user)
    response = {'lesson_action': new_lesson_action}
    template = loader.get_template('chinesetool/translate_sentence.html')
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
            abo = Subscription(name=user,
                               registration_date=datetime.now(),
                               last_login_date=datetime.now(),
                               abo_date=datetime.now() + timedelta(days=30))
            abo.save()

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


from django.http import *
from django.template import RequestContext
import json


def dictionary(request):
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
    context = RequestContext(request)
    return HttpResponse(template.render(context))


@login_required
def choose_language(request):
    template = loader.get_template('chinesetool/choose_language.html')
    context = RequestContext(request)
    return HttpResponse(template.render(context))


def add_lesson(request):
    """
    Allows user to add a new lesson
    :param request:
    :return:
    """
    if request.POST.get('topic', False):
        lesson = Lesson(topic=request.POST.get('topic'))
        lesson.save()
        return HttpResponseRedirect(reverse('chinesetool:modify_lesson', args=(lesson.id,)))
    template = loader.get_template(('chinesetool/add_lesson.html'))
    context = RequestContext(request)
    return HttpResponse(template.render(context))


def modify_lesson(request, lesson_id):
    """
    Modifies lesson - allows to change requirements and exercises
    :param request:
    :return:
    """
    lesson = Lesson.objects.get(pk=lesson_id)
    if request.POST.get('requirement_to_remove', False):
        requirement_to_remove = Lesson.objects.get(pk=request.POST.get('requirement_to_remove'))
        lesson.requirements.remove(requirement_to_remove)
        lesson.save()
    other_lessons = Lesson.objects.all().order_by('-topic')
    requirements = lesson.requirements.all()
    exercises_types = ExerciseType.objects.all().order_by('-description')
    template = loader.get_template('chinesetool/modify_lesson.html')
    context = RequestContext(request, {'other_lessons': other_lessons, 'exercises_types': exercises_types,
                                       'requirements': requirements, 'lesson': lesson})
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
    template = loader.get_template('chinesetool/add_requirement.html')
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
        lesson.add
        lesson.add(request.POST.get('new_word_zh'))
        lesson.save()
        return HttpResponseRedirect(reverse('chinesetool:modify_lesson', args=(lesson_id,)))
    lesson = Lesson.objects.get(pk=lesson_id)
    other_lessons = Lesson.objects.all().order_by('-topic')
    template = loader.get_template('chinesetool/add_requirement.html')
    context = RequestContext(request, {'other_lessons': other_lessons, 'lesson': lesson})
    return HttpResponse(template.render(context))