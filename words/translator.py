# coding=utf-8

from googletrans import translator
from translations.utils import Languages


def translate(word, src):
    translation = get_from_google(word, src)
    return translation.text


def get_from_google(word, src):
    return translator.translate(word,
                                src=language_to_google_code(src),
                                dest=language_to_google_code(Languages.other_language(src)))


def language_to_google_code(language):
    if language == Languages.chinese:
        return 'zh-CN'
    elif language == Languages.polish:
        return 'pl'
    else:
        raise Exception('Unrecognized language: ' + language)


def get_pinyin(chinese_word):
    word = get_from_google(chinese_word, Languages.chinese)
    return word.pronunciation
