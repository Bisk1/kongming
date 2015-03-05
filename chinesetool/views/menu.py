from datetime import datetime, timedelta
import json

from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db import transaction
from django.template import loader
from django.contrib.auth import authenticate, login, logout
from django.core.urlresolvers import reverse
from django.http import *
from django.template import RequestContext

from chinesetool.forms import RegistrationForm
from chinesetool.models import WordZH, WordPL, Subscription, LessonAction, Lesson


def login_my(request):
    """
    Handles username and password passed by user
    :param request: HTTP request
    :return: HTTP response
    """
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        login(request, user)
    else:
        pass


@login_required
def index(request):
    """
    Main page shown after login
    :param request:
    :return:
    """
    template = loader.get_template('chinesetool/index.html')
    context = RequestContext(request)
    return HttpResponse(template.render(context))


@login_required
def learn(request, lesson_id):
    """
    It generates the exercise content. It handles ajax queries and sends
    new exercise content to be replaced so that next exercise is displayed.
    :param request: HTTP request
    :param lesson_id: id of the lesson that user will study
    :return: HTTP response
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
    """
    User can register here to get an account
    :param request: HTTP request
    :return: HTTP response
    """
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
    """
    Handles user's logout and redirects to the main page
    :param request: HTTP request
    :return: HTTP response
    """
    logout(request)
    return HttpResponseRedirect(reverse("chinesetool:index"))


def dictionary(request, source_language):
    """
    Word dictionary. It translates words from source language.
    :param request: HTTP request
    :param source_language: language to translate words from
    :return: HTTP response
    """
    if request.method == 'POST':
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
    """
    Form to choose application language
    :param request: HTTP request
    :return: HTTP response
    """
    template = loader.get_template('chinesetool/choose_language.html')
    context = RequestContext(request)
    return HttpResponse(template.render(context))


def lessons_map(request):
    """
    Displays available lessons
    :param request: HTTP request
    :return: HTTP response
    """
    lessons = Lesson.objects.all()
    template = loader.get_template('chinesetool/lessons_map.html')
    context = RequestContext(request, {'lessons': lessons})
    return HttpResponse(template.render(context))


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
            return HttpResponseRedirect(reverse('chinesetool:modify_lesson', args=(lesson.id,)))
        elif request.POST.get('delete', False):
            lesson = Lesson.objects.get(id=request.POST.get('lesson_id'))
            lesson.delete()
    lessons = Lesson.objects.all()
    template = loader.get_template('chinesetool/lessons_management.html')
    context = RequestContext(request, {'lessons': lessons})
    return HttpResponse(template.render(context))