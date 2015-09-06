from django.db import models


from translations import comparators
from translations.utils import Languages


class WordPL(models.Model):
    """
    Polish word has string value and set of
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
        Check if the Chinese word used by the user can be accepted for this Polish word
        :param word_zh_proposition: word in Chinese (string) typed in by the user
        :return: true if this translation is acceptable
        """
        for chinese_translation in self.get_translations().all():
            if comparators.words_difference(chinese_translation.word, word_zh_proposition) == 0:
                return True
        return False

    @staticmethod
    def get_language():
        return Languages.polish


class WordZH(models.Model):
    """
    Chinese word contains string value and set of
    Polish translations related to it
    """
    word = models.CharField(max_length=50)
    pinyin = models.CharField(max_length=100)
    wordpl_set = models.ManyToManyField(WordPL)

    class Meta:
        unique_together = ["word", "pinyin"]

    def __str__(self):
        return self.word + ' [' + self.pinyin + ']'

    def get_translations(self):
        """
        Gets all accurate translations of this word
        :return: array of Polish words
        """
        return self.wordpl_set

    def check_translation(self, word_pl_proposition):
        """
        Check if the Polish word used by the user can be accepted for this Chinese word
        :param word_pl_proposition: word in Polish (string) typed in by the user
        :return: true if this translation is acceptable
        """
        for polish_translation in self.get_translations().all():
            if comparators.words_difference(polish_translation.word, word_pl_proposition) < 2:
                return True
        return False

    @staticmethod
    def get_language():
        return Languages.chinese
