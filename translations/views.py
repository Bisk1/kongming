import json
import logging

from django.template import loader
from django.http import *
from django.template import RequestContext
from django.core.exceptions import ObjectDoesNotExist

from translations.models import BusinessText
from translations.utils import Languages
from words.models import WordZH, WordPL
logger = logging.getLogger(__name__)


def words_translations(request, source_language):
    """
    Manage words translations. Allow selecting words to edit.
    If exist display available translations.
    :param request: HTTP request
    :param source_language: language to translate words from
    :return: HTTP response
    """
    if request.is_ajax():
        source_word_model = language_name_to_word_model(source_language)
        if 'translations' in request.POST:
            delete_translations(request.POST['word_to_translate'], source_word_model)
            add_translations(request.POST['word_to_translate'],
                             source_word_model,
                             json.loads(request.POST['translations']))
            return HttpResponse('{}', content_type='application/javascript')
        elif 'word_to_search' in request.POST:
            matching_words = source_word_model.objects.filter(word__startswith=request.POST['word_to_search'])[:5].values_list('word', flat=True)
            return HttpResponse(json.dumps({'matching_words': list(matching_words)}), content_type='application/javascript')
        elif 'word_to_translate' in request.POST:
            translations = get_translations_if_word_exists(request.POST['word_to_translate'], source_word_model)
            return HttpResponse(json.dumps({'translations': translations}), content_type='application/javascript')
        else:
            return HttpResponse('Unrecognized AJAX request', content_type='application/javascript')
    template = loader.get_template('translations/words_translations.html')
    context = RequestContext(request, {'source_language': source_language})
    return HttpResponse(template.render(context))


def language_name_to_word_model(language_name):
    if language_name == "polish":
        return WordPL
    elif language_name == "chinese":
        return WordZH
    else:
        raise Exception("Unknown language: " + language_name)


def get_translations_if_word_exists(word_to_search, word_model):
    try:
        if word_model == WordZH:
            return list(WordZH.objects.get(word=word_to_search).wordpl_set.values('word'))
        elif word_model == WordPL:
            return list(WordPL.objects.get(word=word_to_search).wordzh_set.values('word', 'pinyin'))
        else:
            logger.error("Unknown word model: " + word_model)
            return list()
    except ObjectDoesNotExist:
        return list()


def delete_translations(word_to_translate, source_word_model):
    for word_to_translate in source_word_model.objects.filter(word=word_to_translate):
        word_to_translate.get_translations().clear()


def add_translations(word_to_translate, source_word_model, translations):
    if source_word_model == WordPL:
        word_to_translate = WordPL.objects.get_or_create(word=word_to_translate)[0]
        for translation in translations:
            new_word_zh = WordZH.objects.get_or_create(word=translation['word'], pinyin=translation['pinyin'])[0]
            word_to_translate.add(new_word_zh)
    else:
        word_to_translate = WordZH.objects.get_or_create(word=word_to_translate)[0]  # TODO: user should specify pinyin of source word?
        for translation in translations:
            new_word_pl = WordPL.objects.get_or_create(word=translation['word'])[0]
            word_to_translate.wordzh_set.add(new_word_pl)


def texts_translations(request, source_language):
    """
    Manage texts translations. Allow selecting texts to edit.
    If exist display available translations.
    :param request: HTTP request
    :param source_language: language to translate texts from
    :return: HTTP response
    """
    template = loader.get_template('translations/texts_translations.html')
    context = RequestContext(request, {'source_language': source_language})
    return HttpResponse(template.render(context))


def texts_translations_service(request):
    """
    Same as texts_translations but handles operations in payload.
    :param request: HTTP request
    :return: HTTP response
    """
    source_language = request.POST['source_language']
    text_to_translate = request.POST['text_to_translate']
    operation = request.POST['operation']
    if operation == 'set_translations':
        return set_text_translations(text_to_translate, source_language,
                                     translations=json.loads(request.POST['translations']))
    elif operation == 'get_matches':
        return get_text_matches(text_to_translate, source_language)
    elif operation == 'get_translations':
        return get_text_translations(text_to_translate, source_language)
    else:
        return HttpResponse('Unrecognized request', content_type='application/javascript')


def set_text_translations(source_text, source_language, translations):
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
        translation_language = Languages.chinese if source_language==Languages.polish else Languages.polish
        business_translation, _ = BusinessText.objects.get_or_create(text=translation, language=translation_language)
        business_text_to_translate.translations.add(business_translation)
    return HttpResponse('{}', content_type='application/javascript')


def get_text_matches(source_text, source_language):
    """
    Get texts that start with the specified source text in specified language
    :param source_text: text that matches should start with
    :param source_language: languages of the matches
    :return:
    """
    matching_business_texts = BusinessText.objects.filter(text__startswith=source_text, language=source_language)
    matching_texts = matching_business_texts[:5].values_list('text', flat=True)
    return HttpResponse(json.dumps({'matches': list(matching_texts)}), content_type='application/javascript')


def get_text_translations(source_text, source_language):
    """
    Get translations of the specified text in specified language
    :param source_text: text to translate
    :param source_language: language of the text to translate
    :return:
    """
    business_text_to_translate = BusinessText.objects.get(text=source_text, language=source_language)
    translations = list(business_text_to_translate.translations.values('text'))
    return HttpResponse(json.dumps({'translations': translations}), content_type='application/javascript')



