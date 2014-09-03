from django.contrib.auth.models import User
from django.db import models


class Lesson(models.Model):
    level = models.IntegerField(default=0)

    def __unicode__(self):
        return unicode(self.level)


class WordPL(models.Model):
    word = models.CharField(max_length=100, unique=True)

    def __unicode__(self):
        return unicode(self.word)


    def get_translations(self):
        word_zh = list()
        for translation in self.wordzh_set.all():
            word_zh.append(translation.word)
        return word_zh

class WordZH(models.Model):
    word = models.CharField(max_length=50, unique=True)
    pinyin = models.CharField(max_length=100)
    lesson = models.ForeignKey(Lesson, null=True, default=None)
    wordpl_set = models.ManyToManyField(WordPL, through='WordTranslation')

    class Meta:
        unique_together = ["word", "pinyin"]

    def __unicode__(self):
        return unicode(self.word)


    def get_translations(self):
        words_pl = list()
        for translation in self.wordpl_set.all():
            words_pl.append(translation.word)
        return words_pl



class WordTranslation(models.Model):
    word_zh = models.ForeignKey(WordZH)
    word_pl = models.ForeignKey(WordPL)

    class Meta:
        unique_together = ["word_zh", "word_pl"]

    def __unicode__(self):
        return self.word_zh.word + " - " + self.word_pl.word


class SentencePL(models.Model):
    level = models.IntegerField(default=0)
    sentence = models.TextField(default='')


class SentenceZH(models.Model):
    level = models.IntegerField(default=0)
    sentence = models.TextField(default='')


class SentenceTranslation(models.Model):
    sentence_zh = models.ForeignKey(WordZH)
    sentence_pl = models.ForeignKey(WordPL)


class Abonament(models.Model):
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




