# encoding=utf-8

from enum import Enum
import jieba
import string


class Languages(Enum):
    polish = 'pl'
    chinese = 'zh'

    @staticmethod
    def other_language(language):
        if language == Languages.polish:
            return Languages.chinese
        elif language == Languages.chinese:
            return Languages.polish
        else:
            Languages.handle_non_existent_language(language)


    @staticmethod
    def tokenize(language, text):
        to_tokenize = _remove_punctuation(text)
        if language == Languages.chinese.value:
            return jieba.cut(to_tokenize)
        elif language == Languages.polish.value:
            return _polish_tokenize(to_tokenize)
        else:
            Languages.handle_non_existent_language(language)

    @staticmethod
    def handle_non_existent_language(language):
        try:
            raise Exception('Unknown language: ' + language.value)
        except AttributeError:
            raise Exception('Input is not language: ' + language)


def _polish_tokenize(text):
    result = text
    result = result.strip()
    result = result.split(' ')
    return result


def _remove_punctuation(text):
    result = text
    result = result.replace('.', ' ')
    result = result.replace(',', ' ')
    result = result.replace(':', ' ')
    result = result.replace(';', ' ')
    result = result.replace('!', ' ')
    result = result.replace('?', ' ')
    result = result.replace('\"', ' ')
    result = result.replace('\'', ' ')
    result = result.replace('(', ' ')
    result = result.replace(')', ' ')
    result = result.replace('？', ' ')
    result = result.replace('！', ' ')
    result = ' '.join(result.split())  # remove extra whitespace
    return result