# coding=utf-8

from googletrans import translator
from translations.utils import Languages
from words.models import WordZH, WordPL
from django.core.exceptions import ObjectDoesNotExist


def translate(word, src):
    try:
        return get_from_db(word, src)
    except ObjectDoesNotExist:
        translation = get_from_google(word, src)
        add_to_db(translation, src)
        return translation.text


def get_from_google(word, src):
    return translator.translate(word,
                                src=language_to_google_code(src),
                                dest=language_to_google_code(Languages.other_language(src)))


def get_from_db(word, src):
    candidates = language_to_model(src).objects.filter(word=word)
    if len(candidates) == 0:
        raise ObjectDoesNotExist
    translations = candidates[0].get_translations().all()
    if len(translations) == 0:
        raise ObjectDoesNotExist
    return translations[0].word


def add_to_db(word, src):
    if src == Languages.polish:
        word_pl, _ = WordPL.objects.get_or_create(word=word.origin)
        word_zh, _ = WordZH.objects.get_or_create(word=word.text, pinyin=word.pronunciation)
        word_pl.wordzh_set.add(word_zh)
    elif src == Languages.chinese:
        word_zh, _ = WordZH.objects.get_or_create(word=word.origin, pinyin=get_pinyin(word.origin))
        word_pl, _ = WordPL.objects.get_or_create(word=word.text)
        word_zh.wordpl_set.add(word_pl)
    else:
        raise Exception('Unrecognized language: ' + src)


def language_to_google_code(language):
    if language == Languages.chinese:
        return 'zh-CN'
    elif language == Languages.polish:
        return 'pl'
    else:
        raise Exception('Unrecognized language: ' + language)


def language_to_model(language):
    if language == Languages.chinese:
        return WordZH
    elif language == Languages.polish:
        return WordPL
    else:
        raise Exception('Unrecognized language: ' + language)


def get_pinyin(chinese_word):
    word = get_from_google(chinese_word, Languages.chinese)
    return word.pronunciation
