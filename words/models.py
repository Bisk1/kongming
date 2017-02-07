from django.db import models
from translations import comparators
from translations.utils import Languages
from words.translator import CedictClient

translator = CedictClient()

class WordEN(models.Model):
    """
    English word has string value and set of
    Chinese translations related to it
    """
    word = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.word

    def get_translations(self):

        """
        Gets all translations of this word
        :return: array of Chinese words
        """
        return self.wordzh_set

    def check_translation(self, word_zh_proposition):
        """
        Check if the Chinese word used by the user can be accepted for this English word
        :param word_zh_proposition: word in Chinese (string) typed in by the user
        :return: true if this translation is acceptable
        """
        for chinese_translation in self.get_translations().all():
            if comparators.words_difference(chinese_translation.word, word_zh_proposition) == 0:
                return True
        return False

    @classmethod
    def get_or_create_with_translator(clss, word):
        """
        Same as get_or_create. Created for symmetry with WordZH.
        :return:
        """
        return WordEN.objects.get_or_create(word=word)

    @staticmethod
    def get_language():
        return Languages.english


class WordZH(models.Model):
    """
    Chinese word contains string value and set of
    English translations related to it
    """
    word = models.CharField(max_length=50)
    pinyin = models.CharField(max_length=100)
    worden_set = models.ManyToManyField(WordEN)

    class Meta:
        unique_together = ["word", "pinyin"]

    def __str__(self):
        return self.word + ' [' + self.pinyin + ']'

    def get_translations(self):
        """
        Gets all accurate translations of this word
        :return: array of English words
        """
        return self.worden_set

    def check_translation(self, word_en_proposition):
        """
        Check if the English word used by the user can be accepted for this Chinese word
        :param word_en_proposition: word in English (string) typed in by the user
        :return: true if this translation is acceptable
        """
        for english_translation in self.get_translations().all():
            if comparators.words_difference(english_translation.word, word_en_proposition) < 2:
                return True
        return False

    @staticmethod
    def get_or_create_with_translator(word):
        """
        If word does not exist, use translator to fetch pinyin
        :param word: Chinese word to get
        :return: 2-element tuple same as in get_or_create
        """
        try:
            return WordZH.objects.get(word=word), True
        except WordZH.DoesNotExist:
            pinyin = translator.get_pinyin(word)
            return WordZH.objects.create(word=word, pinyin=pinyin), False

    @staticmethod
    def get_language():
        return Languages.chinese


def to_word_model(language):
    if language == Languages.chinese.value:
        return WordZH
    elif language == Languages.english.value:
        return WordEN
    else:
        Languages.handle_non_existent_language(language)