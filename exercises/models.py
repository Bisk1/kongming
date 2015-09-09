from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType

from django.db import models

from lessons.models import Lesson
from translations.models import BusinessText


class Exercise(models.Model):
    lesson = models.ForeignKey(Lesson)
    number = models.IntegerField(null=True)
    content_type = models.ForeignKey(ContentType)
    object_id = models.PositiveIntegerField()
    spec = GenericForeignKey('content_type', 'object_id')

    def __str__(self):
        return str(self.spec)

    def __repr__(self):
        return str(self)


class AbstractExercise(models.Model):
    def check_answer(self, proposition):
        raise NotImplementedError

    def prepare(self):
        raise NotImplementedError


class Typing(AbstractExercise):
    text_to_translate = models.ForeignKey(BusinessText)

    def check_answer(self, proposition):
        return {'success': self.text_to_translate.check_translation(proposition),
                'correct_translation': self.text_to_translate.translations.first().text}

    def prepare(self):
        return {'text': self.text_to_translate.text,
                'language': self.text_to_translate.language}

    def __str__(self):
        return self.text_to_translate.language + ': ' + self.text_to_translate.text + ' - ' \
               + ', '.join([translation.text for translation in self.text_to_translate.translations.all()])

    def __repr__(self):
        return str(self)


class Choice(AbstractExercise):
    text_to_translate = models.ForeignKey(BusinessText, related_name='choice_exercise_as_text_to_translate')
    correct_choice = models.ForeignKey(BusinessText, related_name='choice_exercise_as_correct')
    wrong_choices = models.ManyToManyField(BusinessText, related_name='choice_exercise_as_wrong')

    def check_answer(self, proposition):
        return {'success': proposition == self.correct_choice.text,
                'correct_translation': self.correct_choice.text}

    def prepare(self):
        return {'text': self.text_to_translate.text}

    def __str__(self):
        return self.text_to_translate.language + ': ' + self.text_to_translate.text + ' - ' \
               + self.correct_choice.text + ' - '
               #+ ', '.join([wrong_choice.text for wrong_choice in self.wrong_choices])

    def __repr__(self):
        return str(self)


class Explanation(AbstractExercise):
    text = models.TextField()
    image = models.FileField(upload_to="image/", blank=True)

    def check_answer(self, proposition):
        raise Exception("Explanation has no check method")

    def prepare(self):
        return {'text': self.text}

    def __str__(self):
        return self.text

    def __repr__(self):
        return str(self)