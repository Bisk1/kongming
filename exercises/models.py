import abc
from django.contrib.contenttypes.generic import GenericForeignKey
from django.contrib.contenttypes.models import ContentType

from django.db import models
from enum import Enum

from lessons.models import Lesson


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
    @abc.abstractmethod
    def check(self, proposition):
        pass

    @abc.abstractmethod
    def prepare(self):
        pass

    class Meta:
        abstract = True


class Typing(AbstractExercise):
    # Can refer to Polish or Chinese text only
    limit = models.Q(app_label='translations', model='TextZH') | \
            models.Q(app_label='translations', model='TextPL')

    content_type = models.ForeignKey(ContentType, limit_choices_to=limit)
    object_id = models.PositiveIntegerField()
    text = GenericForeignKey('content_type', 'object_id')

    def check(self, proposition):
        return {'success': self.text.check_translation(proposition),
                'correct_translation': self.text.get_translations().first().text}

    def prepare(self):
        return {'text': self.text.text,
                'language': self.text.get_language()}

    def __unicode__(self):
        return unicode(self.text)


class Explanation(AbstractExercise):
    text = models.TextField()
    image = models.FileField(upload_to="image/", null=True)

    def check(self, proposition):
        raise Exception("Explanation has no check method")

    def prepare(self):
        return {'text': self.text}

    def __unicode__(self):
        return unicode(self.text)


class ExerciseType(models.Model):
    name = models.CharField(max_length=20)
    slug = models.CharField(max_length=20)
    model = models.ForeignKey(ContentType)

    def __unicode__(self):
        return unicode(self.name + ' (' + self.slug + ') - ' + self.model.name)