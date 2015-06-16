import json
import logging

from django.template import loader
from django.http import *
from django.template import RequestContext
from django.core.exceptions import ObjectDoesNotExist

from models import WordZH, WordPL, WordTranslation, SentencePL, SentenceZH, SentenceTranslation

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
        print request.POST
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
            print 'tr'
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
    if source_word_model == WordPL:
        WordPL.objects.get(word=word_to_translate).wordzh_set.clear()
    else:
        WordZH.objects.get(word=word_to_translate).wordpl_set.clear()


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


def sentences_translations(request, source_language):
    """
    Manage sentences translations. Allow selecting sentences to edit.
    If exist display available translations.
    :param request: HTTP request
    :param source_language: language to translate sentences from
    :return: HTTP response
    """
    if request.is_ajax() and request.method == 'POST':
        source_sentence_model = language_name_to_sentence_model(source_language)
        if 'translations' in request.POST:
            delete_sentence_translations(request.POST['sentence_to_translate'], source_sentence_model)

            add_sentence_translations(request.POST['sentence_to_translate'],
                             source_sentence_model,
                             json.loads(request.POST['translations']))
            return HttpResponse('{}', content_type='application/javascript')
        elif 'sentence_to_search' in request.POST:
            matching_sentences = source_sentence_model.objects.filter(sentence__startswith=request.POST['sentence_to_search'])[:5].values_list('sentence', flat=True)
            return HttpResponse(json.dumps({'matching_sentences': list(matching_sentences)}), content_type='application/javascript')
        elif 'sentence_to_translate' in request.POST:
            translations = get_translations_if_sentence_exists(request.POST['sentence_to_translate'], source_sentence_model)
            return HttpResponse(json.dumps({'translations': translations}), content_type='application/javascript')
        else:
            return HttpResponse('Unrecognized AJAX request', content_type='application/javascript')
    template = loader.get_template('translations/sentences_translations.html')
    context = RequestContext(request, {'source_language': source_language})
    return HttpResponse(template.render(context))


def language_name_to_sentence_model(language_name):
    if language_name == "polish":
        return SentencePL
    elif language_name == "chinese":
        return SentenceZH
    else:
        raise Exception("Unknown language: " + language_name)


def get_translations_if_sentence_exists(sentence_to_search, sentence_model):
    try:
        if sentence_model == SentencePL:
            return list(SentencePL.objects.get(sentence=sentence_to_search).sentencezh_set.values('sentence'))
        elif sentence_model == SentenceZH:
            return list(SentenceZH.objects.get(sentence=sentence_to_search).sentencepl_set.values('sentence'))
        else:
            logger.error("Unknown sentence model: " + sentence_model)
            return list()
    except ObjectDoesNotExist:
        return list()


def delete_sentence_translations(sentence_to_translate, source_sentence_model):
    if source_sentence_model == SentencePL:
        SentencePL.objects.get(sentence=sentence_to_translate).sentencezh_set.clear()
    else:
        SentenceZH.objects.get(sentence=sentence_to_translate).sentencepl_set.clear()


def add_sentence_translations(sentence_to_translate, source_sentence_model, translations):
    if source_sentence_model == SentencePL:
        sentence_to_translate = SentencePL.objects.get_or_create(sentence=sentence_to_translate)[0]
        for translation in translations:
            new_sentence_zh = SentenceZH.objects.get_or_create(sentence=translation['sentence'])[0]
            SentenceTranslation.objects.get_or_create(sentence_zh=new_sentence_zh, sentence_pl=sentence_to_translate)
    else:
        sentence_to_translate = SentenceZH.objects.get_or_create(sentence=sentence_to_translate)[0]
        for translation in translations:
            new_sentence_pl = SentencePL.objects.get_or_create(sentence=translation['sentence'])[0]
            SentenceTranslation.objects.get_or_create(sentence_zh=sentence_to_translate, sentence_pl=new_sentence_pl)

