from datetime import datetime, timedelta
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db import transaction
from django.template import loader
import random
from chinesetool.forms import RegistrationForm

from chinesetool.models import WordZH, WordPL, WordTranslation, Subscription

from django.contrib.auth import authenticate, login, logout
from django.core.urlresolvers import reverse

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
    random_word_zh = get_random(WordZH)
    template = loader.get_template('chinesetool/translate_word.html')
    context = RequestContext(request, {
        'wordzh': random_word_zh,
    })
    return HttpResponse(template.render(context))


def check_word_translation(word, word_zh_id):
    """
    Check if the polish word used by the user
    can be accepted for given chinese word
    :param word: word in polish typed in by the user
    :param word_zh_id: chinese word to be guessed
    :return: true if this translation is acceptable
    """
    # proposition = request.POST['proposition']
    proposition = word
    proposition_id = WordPL.objects.filter(word=proposition)
    status = 0
    if WordTranslation.objects.filter(word_pl=proposition_id, word_zh=word_zh_id).count() > 0:
        status = 1
    else:
        words = WordZH.objects.filter(pk=word_zh_id)[0].get_translations()
        if len(words) > 0:
            for word in words:
                if check_if_similar(word, proposition) < 2:
                    if WordPL.objects.filter(word=proposition).count() == 0:
                        status = 1

    # Always return an HttpResponseRedirect after successfully dealing
    # with POST data. This prevents data from being posted twice if a
    # user hits the Back button.

    return status


def check_if_similar(word1, word2):
    """
    Check if two words in the same language are similar enough
    to be accepted. In order to be accepted there must be at most
    one different character.
    :param word1:
    :param word2:
    :return:
    """
    if word1 == word2:
        return 0
    if len(word1) == len(word2):
        letter_count = 0
        for position, letter in enumerate(word1):
            if letter != word2[position]:
                letter_count += 1
        return letter_count

    if len(word1) > len(word2):
        if word1[1:] == word2:
            return 1
        elif word1[:-1] == word2:
            return 1
        else:
            return 1000

    if len(word2) > len(word1):
        if word2[1:] == word1:
            return 1
        elif word2[:-1] == word1:
            return 1
        else:
            return 1000


@login_required
def translate_sentence(request):
    """
    TODO: This is a mock!
    It generates a form with chinese sentence to be guessed and an input box for
    the user to type in his guess. If a guess has already been made, it shows results.
    :param request: http request for this page
    :return: http response showing guessing panel
    """
    random_sentence_zh = get_random(WordZH)
    template = loader.get_template('chinesetool/translate_sentence.html')
    context = RequestContext(request, {
        'sentencezh': random_sentence_zh,
    })
    return HttpResponse(template.render(context))


def get_random(model):
    """
    Gets a random object from any of the objects
    for given model. It uses all records specified
    for this model in the database
    :param model: model of the objects to be randomized
    :return: single object of given model
    """
    count = model.objects.all().count()
    if count > 0:
        random_index = random.randint(0, count - 1)
        return model.objects.all()[random_index]
    else:
        return


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
                            abo_date=datetime.now()+timedelta(days=30))
            abo.save()

            template = loader.get_template("registration/register_success.html")
            variables = RequestContext(request, {'username': form.cleaned_data['username']})
            output = template.render(variables)
            return HttpResponse(output)
    else:
        form = RegistrationForm()
    template = loader.get_template("registration/register.html")
    variables = RequestContext(request, {'form': form})
    output = template.render(variables)
    return HttpResponse(output)


def logout_page(request):
    logout(request)
    return HttpResponseRedirect(reverse("chinesetool:index"))


from django.http import *
from django.shortcuts import render_to_response
from django.template import RequestContext
import json


def ajax(request):
    if 'client_response' in request.POST:
        lesson = request.session.get('lesson')
        correct_word = ""
        result_to_send = ""
        if not lesson:
            lesson = LessonController()
        else:
            lesson = LessonController.to_object(lesson)
        if 0 < lesson.number < 20:
            word_to_check = request.POST['client_response']
            words = WordZH.objects.filter(pk=lesson.current_word.id)[0].get_translations()
            correct_word = words[0]

            if check_word_translation(word_to_check, lesson.current_word.id) == 1:
                result_to_send = "True"
            else:
                result_to_send = "False"
                lesson.fails += 1

        if lesson.number < 20:
            word_to_send = lesson.get_next_word().word
            result = result_to_send
            fails = lesson.fails
            number = lesson.number
            request.session['lesson'] = lesson.to_json()
            response_dict = {}
            response_dict.update({'word_to_display': word_to_send,
                                  'result': result,
                                  'fails': fails,
                                  'number': number,
                                  'correct': correct_word})

            return HttpResponse(json.dumps(response_dict), mimetype='application/javascript')
        word_to_send = "FINISH"
        response_dict = {}
        response_dict.update({'word_to_display': word_to_send, 'result': '', 'fails': '', 'number': ''})
        return HttpResponse(json.dumps(response_dict), mimetype='application/javascript')

    else:
        return render_to_response('ajaxexample.html', context_instance=RequestContext(request))


class LessonController():
    def __init__(self, number=0, fails=0, words=None, current_word=None):
        self.number = number
        self.fails = fails
        if words is None:
            self.words = self.get_words()
        else:
            self.words = words
        self.current_word = current_word

    def get_words(self):
        words = list()
        for i in range(20):
            words.append(get_random(WordZH))
        return words

    def get_next_word(self):
        if self.number < 20:
            self.number += 1
            self.current_word = self.words[self.number-1]
            return self.words[self.number-1]
        return "Koniec lekcji"

    def to_json(self):
        object_words = dict()
        for i, word in enumerate(self.words):
            object_words[i] = word.id
        object_dict = {
            'number': self.number,
            'fails': self.fails,
            'current_word': self.current_word.id,
            'words': object_words
        }
        return object_dict

    @staticmethod
    def to_object(object_dict):
        if "number" in object_dict:
            number = object_dict["number"]
        else:
            number = 0
        if "fails" in object_dict:
            fails = object_dict["fails"]
        else:
            fails = 0
        if "current_word" in object_dict:
            current_word = WordZH.objects.filter(pk=object_dict["current_word"])[0]
        else:
            current_word = None
        words = list()
        if "words" in object_dict:
            for i in range(20):
                words.append(WordZH.objects.filter(pk=object_dict['words'][str(i)])[0])

        return LessonController(number=number, fails=fails, words = words, current_word = current_word)


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
