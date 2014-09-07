from django.contrib.auth.models import User
from django.db import models


class Lesson(models.Model):
    """
    Single chinese lesson is defined by level
    and words related to it.
    """
    level = models.IntegerField(default=0)

    def __unicode__(self):
        return unicode(self.level)


class WordPL(models.Model):
    """
    Polish word has string value and set of
    chinese translations related to it
    """
    word = models.CharField(max_length=100, unique=True)

    def __unicode__(self):
        return unicode(self.word)


    def get_translations(self):
        """
        Gets all accurate translations of this word
        :return: array of chinese words
        """
        word_zh = list()
        for translation in self.wordzh_set.all():
            word_zh.append(translation.word)
        return word_zh


class WordZH(models.Model):
    """
    Chinese word contains string value and set of
    polish translations related to it
    """
    word = models.CharField(max_length=50, unique=True)
    pinyin = models.CharField(max_length=100)
    lesson = models.ForeignKey(Lesson, null=True, default=None)
    wordpl_set = models.ManyToManyField(WordPL, through='WordTranslation')

    class Meta:
        unique_together = ["word", "pinyin"]

    def __unicode__(self):
        return unicode(self.word)


    def get_translations(self):
        """
        Gets all accurate translations of this word
        :return: array of polish words
        """
        words_pl = list()
        for translation in self.wordpl_set.all():
            words_pl.append(translation.word)
        return words_pl


class WordTranslation(models.Model):
    """
    Pair of chinese word and polish word defines
    single translation. This is a many-to-many field
    because oen polish word can have many chinese
    translations and one chinese word can have
    many polish translations
    """
    word_zh = models.ForeignKey(WordZH)
    word_pl = models.ForeignKey(WordPL)

    class Meta:
        unique_together = ["word_zh", "word_pl"]

    def __unicode__(self):
        return self.word_zh.word + " - " + self.word_pl.word


class SentencePL(models.Model):
    """
    TODO: This is mock
    Polish sentence has string value
    """
    level = models.IntegerField(default=0)
    sentence = models.TextField(default='')


class SentenceZH(models.Model):
    """
    TODO: This is mock
    Chinese sentence has string value
    """
    level = models.IntegerField(default=0)
    sentence = models.TextField(default='')


class SentenceTranslation(models.Model):
    """
    TODO: This is mock
    Pair of chinese sentece and polish sentence
    """
    sentence_zh = models.ForeignKey(WordZH)
    sentence_pl = models.ForeignKey(WordPL)


class Subscription(models.Model):
    name = models.ForeignKey(User)
    registration_date = models.DateTimeField()
    last_login_date = models.DateTimeField()
    abo_date = models.DateTimeField()
    def __unicode__(self):
        return unicode(self.name)


class WordSkills(models.Model):
    word_zh = models.ForeignKey(WordZH)
    user = models.ForeignKey(User)
    last_time = models.DateTimeField()
    correct = models.IntegerField(default=0)
    correct.run = models.IntegerField(default=0)
    wrong = models.IntegerField(default=0)




