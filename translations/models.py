from django.db import models

from . import comparators

POLISH = "pl"
CHINESE = "zh"


class WordPL(models.Model):
    """
    Polish word has string value and set of
    Chinese translations related to it
    """
    word = models.CharField(max_length=100, unique=True)

    def __unicode__(self):
        return unicode(self.word)

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
        return POLISH


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

    def __unicode__(self):
        return unicode(self.word + ' [' + self.pinyin + ']')

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
        return CHINESE


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

    def __unicode__(self):
        return unicode(self.word_zh) + " - " + unicode(self.word_pl)


class TextPL(models.Model):
    """
    Polish text
    """
    text = models.CharField(max_length=255, unique=True)

    def __unicode__(self):
        return unicode(self.text)

    def get_translations(self):
        """
        Gets all translations of this word
        :return: array of Chinese texts
        """
        return self.textzh_set

    def check_translation(self, text_zh_proposition):
        """
        Check if the Chinese text used by the user can be accepted for this Polish text
        :param text_zh_proposition: text in Chinese (string) typed in by the user
        :return: true if this translation is acceptable
        """
        for chinese_translation in self.get_translations().all():
            if comparators.texts_difference(chinese_translation.text, text_zh_proposition) == 0:
                return True
        return False

    def add_translation(self, translation_text):
        TextTranslation(text_zh=translation_text, text_pl=self).save()

    @staticmethod
    def get_language():
        return POLISH


class TextZH(models.Model):
    """
    Chinese text
    """
    text = models.CharField(max_length=255, unique=True)
    textpl_set = models.ManyToManyField(TextPL, through='TextTranslation')

    def __unicode__(self):
        return unicode(self.text)

    def get_translations(self):
        """
        Gets all translations of this text
        :return: array of Polish texts
        """
        return self.textpl_set

    def check_translation(self, text_pl_proposition):
        """
        Check if the Polish text used by the user can be accepted for this Chinese text
        :param text_pl_proposition: text in Polish (string) typed in by the user
        :return: true if this translation is acceptable
        """
        for polish_translation in self.get_translations().all():
            if comparators.texts_difference(polish_translation.text, text_pl_proposition) == 0:
                return True
        return False

    def add_translation(self, translation_text):
        TextTranslation(text_zh=self, text_pl=translation_text).save()

    @staticmethod
    def get_language():
        return CHINESE

class TextTranslation(models.Model):
    """
    Pair of a Chinese text and a Polish texxt
    """
    text_zh = models.ForeignKey(TextZH)
    text_pl = models.ForeignKey(TextPL)

    class Meta:
        unique_together = ["text_zh", "text_pl"]

    def __unicode__(self):
        return unicode(self.text_zh) + " - " + unicode(self.text_pl)
