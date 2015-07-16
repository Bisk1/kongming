import json
import logging

from django.template import loader
from django.http import *
from django.template import RequestContext
from django.core.exceptions import ObjectDoesNotExist

from models import WordZH, WordPL, WordTranslation, TextPL, TextZH, TextTranslation

logger = logging.getLogger(__name__)


def words_translations(request, source_language):
    """
    Manage words translations. Allow selecting words to edit.
    If exist display available translations.
    :param request: HTTP request
    :param source_language: language to translate words from
    :return: HTTP response
    """
    if request.is_ajax() and request.method == 'POST':
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
            print translations
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
            WordTranslation.objects.get_or_create(word_zh=new_word_zh, word_pl=word_to_translate)
    else:
        word_to_translate = WordZH.objects.get_or_create(word=word_to_translate)[0]  # TODO: user should specify pinyin of source word?
        for translation in translations:
            new_word_zh = WordZH.objects.get_or_create(word=translation['word'])[0]
            WordTranslation.objects.get_or_create(word_zh=new_word_zh, word_pl=word_to_translate)


def texts_translations(request, source_language):
    """
    Manage texts translations. Allow selecting texts to edit.
    If exist display available translations.
    :param request: HTTP request
    :param source_language: language to translate texts from
    :return: HTTP response
    """
    if request.is_ajax() and request.method == 'POST':
        source_text_model = language_name_to_text_model(source_language)
        if 'translations' in request.POST:
            delete_text_translations(request.POST['text_to_translate'], source_text_model)

            add_text_translations(request.POST['text_to_translate'],
                             source_text_model,
                             json.loads(request.POST['translations']))
            return HttpResponse('{}', content_type='application/javascript')
        elif 'text_to_search' in request.POST:
            print source_text_model
            matching_texts = source_text_model.objects.filter(text__startswith=request.POST['text_to_search'])[:5].values_list('text', flat=True)
            return HttpResponse(json.dumps({'matching_texts': list(matching_texts)}), content_type='application/javascript')
        elif 'text_to_translate' in request.POST:
            translations = get_translations_if_text_exists(request.POST['text_to_translate'], source_text_model)
            return HttpResponse(json.dumps({'translations': translations}), content_type='application/javascript')
        else:
            return HttpResponse('Unrecognized AJAX request', content_type='application/javascript')
    template = loader.get_template('translations/texts_translations.html')
    context = RequestContext(request, {'source_language': source_language})
    return HttpResponse(template.render(context))


def language_name_to_text_model(language_name):
    if language_name == "polish":
        return TextPL
    elif language_name == "chinese":
        return TextZH
    else:
        raise Exception("Unknown language: " + language_name)


def get_translations_if_text_exists(text_to_search, text_model):
    try:
        if text_model == TextPL:
            return list(TextPL.objects.get(text=text_to_search).TextZH_set.values('text'))
        elif text_model == TextZH:
            return list(TextZH.objects.get(text=text_to_search).TextPL_set.values('text'))
        else:
            logger.error("Unknown text model: " + text_model)
            return list()
    except ObjectDoesNotExist:
        return list()


def delete_text_translations(text_to_translate, source_text_model):
    if source_text_model == TextPL:
        TextPL.objects.get(text=text_to_translate).TextZH_set.clear()
    else:
        TextZH.objects.get(text=text_to_translate).TextPL_set.clear()


def add_text_translations(text_to_translate, source_text_model, translations):
    if source_text_model == TextPL:
        text_to_translate = TextPL.objects.get_or_create(text=text_to_translate)[0]
        for translation in translations:
            new_text_zh = TextZH.objects.get_or_create(text=translation['text'])[0]
            TextTranslation.objects.get_or_create(text_zh=new_text_zh, text_pl=text_to_translate)
    else:
        text_to_translate = TextZH.objects.get_or_create(text=text_to_translate)[0]
        for translation in translations:
            new_text_pl = TextPL.objects.get_or_create(text=translation['text'])[0]
            TextTranslation.objects.get_or_create(text_zh=text_to_translate, text_pl=new_text_pl)

