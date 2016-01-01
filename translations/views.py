import json
import logging
from enum import Enum

from django.http import *
from django.shortcuts import render, redirect
from django.views.generic import View

from translations.forms import TextsTranslationsForm, WordsTranslationsForm
from translations.services import TextsTranslationsService, WordsTranslationsService
from translations.utils import Languages
from words.models import to_word_model


logger = logging.getLogger(__name__)


class TranslationsOperation(Enum):
    get_translations = 'get_translations'
    set_translations = 'set_translations'
    get_matches = 'get_matches'


words_translations_service = WordsTranslationsService()
texts_translations_service = TextsTranslationsService()


class WordsTranslationsView(View):

    def get(self, request):
        """
        Manage words translations. Allow selecting words to edit.
        If exist display available translations.
        """
        return render(request, 'translations/words_translations.html', {'form': WordsTranslationsForm})

    def post(self, request):
        form = WordsTranslationsForm(request.POST)
        if form.is_valid():
            words_translations_service.set_word_translations(
                form.cleaned_data['source_word'],
                to_word_model(form.cleaned_data['source_language']),
                form.translation_fields())
        return redirect('translations:words_translations')


class WordsTranslationsApiView(View):

    def post(self, request, *args, **kwargs):
        """
        API for accessing words translations
        """
        source_word_model = to_word_model(request.POST['source_language'])
        operation = request.POST['operation']
        if operation == TranslationsOperation.set_translations.value:
            words_translations_service.set_word_translations(request.POST['source_word'],
                                                             source_word_model,
                                                             json.loads(request.POST['translations']))
            return JsonResponse({})
        elif operation == TranslationsOperation.get_matches.value:
            matches = words_translations_service.get_word_matches(request.POST['source_word'],
                                                                  source_word_model)
            return JsonResponse({'matches': matches})
        elif operation == TranslationsOperation.get_translations.value:
            translations = words_translations_service.get_word_translations(request.POST['source_word'],
                                                                            source_word_model)
            return JsonResponse({'translations': translations})
        return HttpResponseBadRequest()


class TextsTranslationsView(View):

    def get(self, request):
        """
        Manage texts translations. Allow selecting texts to edit.
        If exist display available translations.
        """
        return render(request, 'translations/texts_translations.html', {'form': TextsTranslationsForm})

    def post(self, request):
        form = TextsTranslationsForm(request.POST)
        if form.is_valid():
            texts_translations_service.set_text_translations(
                form.cleaned_data['source_text'],
                Languages.from_string(form.cleaned_data['source_language']),
                form.translation_fields())
        return redirect('translations:texts_translations')


class TextsTranslationsApiView(View):

    def post(self, request):
        """
        API for accessing text translations
        """
        source_language = Languages.from_string(request.POST['source_language'])
        source_text = request.POST['source_text']
        operation = request.POST['operation']
        if operation == TranslationsOperation.get_matches.value:
            text_matches = texts_translations_service.get_text_matches(source_text, source_language)
            return JsonResponse({'matches': list(text_matches)})
        elif operation == TranslationsOperation.get_translations.value:
            translations = texts_translations_service.get_text_translations(source_text, source_language)
            return JsonResponse({'translations': translations})
        return HttpResponseBadRequest()




