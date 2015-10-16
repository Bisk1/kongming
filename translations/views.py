import json
import logging
from enum import Enum

from django.http import *
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render
from django.views.generic import View

from translations.models import BusinessText
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
            print(request.POST['word_to_translate'])
            print(source_word_model)
            self.delete_translations(request.POST['word_to_translate'], source_word_model)
            self.add_translations(request.POST['word_to_translate'],
                             source_word_model,
                             json.loads(request.POST['translations']))
            return JsonResponse({})
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
                word_to_translate.add(new_word_zh)
        else:
            word_to_translate = WordZH.objects.get_or_create(word=word_to_translate)[0]  # TODO: user should specify pinyin of source word?
            for translation in translations:
                new_word_en = WordEN.objects.get_or_create(word=translation['word'])[0]
                word_to_translate.wordzh_set.add(new_word_en)


class TextsTranslationsView(View):

    def post(self, request):
        """
        Manage texts translations. Allow selecting texts to edit.
        If exist display available translations.
        """
        source_language = request.POST['source_language']
        return render(request, 'translations/texts_translations.html', {'source_language': source_language})


class TextsTranslationsApiView(View):

    def post(self, request):
        """
        API for accessing text translations
        """
        source_language = request.POST['source_language']
        text_to_translate = request.POST['text_to_translate']
        operation = request.POST['operation']
        if operation == TranslationsOperation.set_translations.value:
            return self.set_text_translations(text_to_translate, source_language,
                                         translations=json.loads(request.POST['translations']))
        elif operation == TranslationsOperation.get_matches.value:
            return self.get_text_matches(text_to_translate, source_language)
        elif operation == TranslationsOperation.get_translations.value:
            return self.get_text_translations(text_to_translate, source_language)
        return HttpResponseBadRequest()


    def set_text_translations(self, source_text, source_language, translations):
        """
        Set translations of the source text in source language to the specified translations
        :param source_text: text to translate
        :param source_language: language of text to translate
        :param translations: translations of the text to translate
        :return:
        """
        business_text_to_translate, _ = BusinessText.objects.get_or_create(text=source_text, language=source_language)
        business_text_to_translate.translations.clear()
        for translation in translations:
            translation_language = Languages.chinese if source_language==Languages.english else Languages.english
            business_translation, _ = BusinessText.objects.get_or_create(text=translation, language=translation_language)
            business_text_to_translate.translations.add(business_translation)
        return JsonResponse({})


    def get_text_matches(self, source_text, source_language):
        """
        Get texts that start with the specified source text in specified language
        :param source_text: text that matches should start with
        :param source_language: languages of the matches
        :return:
        """
        matching_business_texts = BusinessText.objects.filter(text__startswith=source_text, language=source_language)
        matching_texts = matching_business_texts[:5].values_list('text', flat=True)
        return JsonResponse({'matches': list(matching_texts)})


    def get_text_translations(self, source_text, source_language):
        """
        Get translations of the specified text in specified language
        :param source_text: text to translate
        :param source_language: language of the text to translate
        :return:
        """
        business_text_to_translate = BusinessText.objects.get(text=source_text, language=source_language)
        translations = list(business_text_to_translate.translations.values('text'))
        return JsonResponse({'translations': translations})



