# coding=utf-8

import requests


class Translator:

    def get_word_zh(self, text, pinyin):
        raise NotImplementedError

    def get_word_en(self, text):
        raise NotImplementedError

    def get_pinyin(self, text):
        raise NotImplementedError


class CedictClient(Translator):

    BASE_URL = "http://cedict.herokuapp.com/api/"

    def get_word_zh_translations(self, text, pinyin=None):
        if pinyin is None:
            return self._get_word_zh_translations_by_text(text)
        else:
            return self._get_word_zh_translations_by_text_and_pinyin(text, pinyin)

    def _get_word_zh_translations_by_text(self, text):
        return self._get_word_zh_by_text(text)['translations']

    def _get_word_zh_translations_by_text_and_pinyin(self, text, pinyin):
        response = requests.get(self.BASE_URL + "zh/" + text + "/" + pinyin)
        data = response.json()
        if response.status_code == 404:
            raise KeyError("Could not find Chinese word with text [" + text + "] and pinyin [" + pinyin + "]")
        return data['translations']

    def get_word_en_translations(self, text):
        response = requests.get(self.BASE_URL + "en/" + text)
        if response.status_code == 404:
            raise KeyError("Could not find Chinese word with text [" + text + "]")
        data = response.json()
        return data['translations']

    def get_pinyin(self, text):
        word = self._get_word_zh_by_text(text)
        return word['pinyin']

    def _get_word_zh_by_text(self, text):
        response = requests.get(self.BASE_URL + "zh/" + text)
        data = response.json()
        if response.status_code == 404:
            raise KeyError("Could not find English word with text [" + text + "]")
        return data[0]