import json
import logging
from enum import Enum

from django.http import *
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render
from django.views.generic import View

from translations.models import BusinessText
from translations.services import TextsTranslationsService
from translations.utils import Languages
from words.models import WordZH, WordEN, to_word_model


logger = logging.getLogger(__name__)


class TranslationsOperation(Enum):
    get_translations = 'get_translations'
    set_translations = 'set_translations'
    get_matches = 'get_matches'


class WordsTranslationsView(View):

    def post(self, request, *args, **kwargs):
        """
        Manage words translations. Allow selecting words to edit.
        If exist display available translations.
        """
        source_word_model = to_word_model(kwargs['source_language'])
        operation = request.POST['operation']
        if operation == TranslationsOperation.set_translations.value:
            self.delete_translations(request.POST['word_to_translate'], source_word_model)
            self.add_translations(request.POST['word_to_translate'],
                             source_word_model,
                             json.loads(request.POST['translations']))
            return JsonResponse({}, status=204)
        elif operation == TranslationsOperation.get_matches.value:
            matching_words = source_word_model.objects.filter(word__startswith=request.POST['word_to_search'])[:5].values_list('word', flat=True)
            return JsonResponse({'matching_words': list(matching_words)})
        elif operation == TranslationsOperation.get_translations.value:
            translations = self.get_translations_if_word_exists(request.POST['word_to_translate'], source_word_model)
            return JsonResponse({'translations': translations})
        return HttpResponseBadRequest()

    def get(self, request, *args, **kwargs):
        return render(request, 'translations/words_translations.html', {'source_language': kwargs['source_language']})

    def get_translations_if_word_exists(self, word_to_search, word_model):
        try:
            if word_model == WordZH:
                return list(WordZH.objects.get(word=word_to_search).worden_set.values('word'))
            elif word_model == WordEN:
                return list(WordEN.objects.get(word=word_to_search).wordzh_set.values('word', 'pinyin'))
            else:
                logger.error("Unknown word model: " + word_model)
                return list()
        except ObjectDoesNotExist:
            return list()

    def delete_translations(self, word_to_translate, source_word_model):
        for word_to_translate in source_word_model.objects.filter(word=word_to_translate):
            word_to_translate.get_translations().clear()

    def add_translations(self, word_to_translate, source_word_model, translations):
        if source_word_model == WordEN:
            word_to_translate = WordEN.objects.get_or_create(word=word_to_translate)[0]
            for translation in translations:
                new_word_zh = WordZH.objects.get_or_create(word=translation['word'], pinyin=translation['pinyin'])[0]
                word_to_translate.wordzh_set.add(new_word_zh)
        else:
            word_to_translate = WordZH.objects.get_or_create(word=word_to_translate)[0]  # TODO: user should specify pinyin of source word?
            for translation in translations:
                new_word_en = WordEN.objects.get_or_create(word=translation['word'])[0]
                word_to_translate.worden_set.add(new_word_en)


class TextsTranslationsView(View):

    def get(self, request, source_language):
        """
        Manage texts translations. Allow selecting texts to edit.
        If exist display available translations.
        """
        #source_language = request.POST['source_language']
        return render(request, 'translations/texts_translations.html', {'source_language': source_language})


class TextsTranslationsApiView(View):

    texts_translations_service = TextsTranslationsService()

    def post(self, request):
        """
        API for accessing text translations
        """
        source_language = Languages.from_string(request.POST['source_language'])
        source_text = request.POST['source_text']
        operation = request.POST['operation']
        if operation == TranslationsOperation.set_translations.value:
            translations = [translation['text'] for translation in json.loads(request.POST['translations'])]
            self.texts_translations_service.set_text_translations(source_text, source_language, translations=translations)
            return JsonResponse({}, status=204)
        elif operation == TranslationsOperation.get_matches.value:
            text_matches = self.texts_translations_service.get_text_matches(source_text, source_language)
            return JsonResponse({'matches': list(text_matches)})
        elif operation == TranslationsOperation.get_translations.value:
            translations = self.texts_translations_service.get_text_translations(source_text, source_language)
            return JsonResponse({'translations': translations})
        return HttpResponseBadRequest()




