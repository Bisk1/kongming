from django.db import models

from . import comparators
from translations.utils import Languages, other_language


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
    wordpl_set = models.ManyToManyField(WordPL, through='WordTranslation')

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


class WordTranslation(models.Model):
    """
    Pair of a Chinese word and a Polish word defines
    single translation. This is a many-to-many field
    because one Polish word can have many Chinese
    translations and one Chinese word can have
    many Polish translations
    """
    word_zh = models.ForeignKey(WordZH)
    word_pl = models.ForeignKey(WordPL)

    class Meta:
        unique_together = ["word_zh", "word_pl"]

    def __str__(self):
        return self.word_zh + " - " + self.word_pl


class BusinessText(models.Model):
    """
    Text with specified language and translations
    """
    text = models.CharField(max_length=255)
    language = models.CharField(max_length=2)
    translations = models.ManyToManyField("self", symmetrical=True)

    class Meta:
        unique_together = ["text", "language"]

    def __str__(self):
        return self.language + " - " + self.text

    def __repr__(self):
        return str(self)

    def check_translation(self, proposition):
        """
        Check if the proposition is acceptable as a translation for this text
        :param proposition: translation to verify
        :return: true if this translation is acceptable
        """
        for translation in self.translations.all():
            if comparators.texts_difference(translation.text, proposition) == 0:
                return True
        return False

    def add_translation(self, translation_text):
        translation_language = other_language(self.language)
        business_translation, _ = BusinessText.objects.get_or_create(text=translation_text,
                                                                     language=translation_language)
        self.translations.add(business_translation)
