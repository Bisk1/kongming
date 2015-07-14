import abc
from django.contrib.contenttypes.generic import GenericForeignKey
from django.contrib.contenttypes.models import ContentType

from django.db import models
from enum import Enum

from lessons.models import Lesson
from translations.models import WordPL, WordZH, SentencePL, SentenceZH


class Exercise(models.Model):
    lesson = models.ForeignKey(Lesson)
    number = models.IntegerField(null=True)
    content_type = models.ForeignKey(ContentType)
    object_id = models.PositiveIntegerField()
    spec = GenericForeignKey('content_type', 'object_id')

    def __unicode__(self):
        return unicode(self.spec)


class ExerciseResultState(Enum):
    NOT_DONE = 0
    SUCCESS = 1
    FAILURE = 2


class AbstractExercise(models.Model):
    exercise = models.ForeignKey(Exercise)

    @abc.abstractmethod
    def check(self, proposition):
        pass

    @abc.abstractmethod
    def prepare(self):
        pass

    class Meta:
        abstract = True


class WordZHExercise(AbstractExercise):
    word = models.ForeignKey(WordZH)

    def check(self, proposition):
        return {'success': self.word.check_translation(proposition),
                'correct_word': self.word.wordpl_set.all()[0].word}

    def prepare(self):
        return {'word': self.word.word}

    def __unicode__(self):
        return unicode(self.word)


class WordPLExercise(AbstractExercise):
    word = models.ForeignKey(WordPL)

    def check(self, proposition):
        return {'success': self.word.check_translation(proposition),
                'correct_word': self.word.wordzh_set.all()[0].word}

    def prepare(self):
        return {'word': self.word.word}

    def __unicode__(self):
        return unicode(self.word)


class SentenceZHExercise(AbstractExercise):
    sentence = models.ForeignKey(SentenceZH)

    def check(self, proposition):
        return {'success': self.sentence.check_translation(proposition),
                'correct_sentence': self.sentence.sentencepl_set.all()[0].sentence}

    def prepare(self):
        return {'sentence': self.sentence.sentence}

    def __unicode__(self):
        return unicode(self.sentence)


class SentencePLExercise(AbstractExercise):
    sentence = models.ForeignKey(SentencePL)

    def check(self, proposition):
        return {'success': self.sentence.check_translation(proposition),
                'correct_sentence': self.sentence.sentencezh_set.all()[0].sentence}

    def prepare(self):
        return {'sentence': self.sentence.sentence}

    def __unicode__(self):
        return unicode(self.sentence)


class ExplanationExercise(AbstractExercise):
    text = models.TextField()
    image = models.FileField(upload_to="image/", null=True)

    def check(self, proposition):
        raise Exception("ExplanationExerciseDetails has no check method")

    def prepare(self):
        return {'text': self.text}

    def __unicode__(self):
        return unicode(self.text)


class ExerciseType(models.Model):
    name = models.CharField(max_length=20)
    slug = models.CharField(max_length=20)
    model = models.ForeignKey(ContentType)

    def __unicode__(self):
        return unicode(self.name + ' (' + self.slug +') - ' + self.model.name)