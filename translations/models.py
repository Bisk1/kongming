from django.db import models

from . import comparators


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
            if comparators.word_difference(chinese_translation.word, word_zh_proposition) == 0:
                return True
        return False


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
            if comparators.word_difference(polish_translation.word, word_pl_proposition) < 2:
                return True
        return False


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
        return self.word_zh.word + " - " + self.word_pl.word


class SentencePL(models.Model):
    """
    Polish sentence has a string value
    """
    sentence = models.CharField(max_length=255, unique=True)

    def __unicode__(self):
        return unicode(self.sentence)

    def get_translations(self):
        """
        Gets all translations of this word
        :return: array of Chinese words
        """
        return self.sentencezh_set

    def check_translation(self, sentence_zh_proposition):
        """
        Check if the Chinese word used by the user can be accepted for this Polish word
        :param sentence_zh_proposition: word in Chinese (string) typed in by the user
        :return: true if this translation is acceptable
        """
        for chinese_translation in self.get_translations().all():
            if comparators.sentence_difference(chinese_translation.sentence, sentence_zh_proposition) < 2:
                return True
        return False


class SentenceZH(models.Model):
    """
    Chinese sentence has a string value
    """
    sentence = models.CharField(max_length=255, unique=True)
    sentencepl_set = models.ManyToManyField(SentencePL, through='SentenceTranslation')

    def __unicode__(self):
        return unicode(self.sentence)

    def get_translations(self):
        """
        Gets all translations of this word
        :return: array of Polish words
        """
        return self.sentencepl_set

    def check_translation(self, sentence_pl_proposition):
        """
        Check if the Polish word used by the user can be accepted for this Chinese word
        :param sentence_pl_proposition: word in Polish (string) typed in by the user
        :return: true if this translation is acceptable
        """
        for polish_translation in self.get_translations().all():
            if comparators.sentence_difference(polish_translation.sentence, sentence_pl_proposition) < 2:
                return True
        return False


class SentenceTranslation(models.Model):
    """
    Pair of a Chinese sentence and a Polish sentence
    """
    sentence_zh = models.ForeignKey(SentenceZH)
    sentence_pl = models.ForeignKey(SentencePL)

    class Meta:
        unique_together = ["sentence_zh", "sentence_pl"]

    def __unicode__(self):
        return self.sentence_zh.sentence + " - " + self.sentence_pl.sentence
