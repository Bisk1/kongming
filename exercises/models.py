import abc

from django.db import models
from enum import Enum

from lessons.models import Lesson
from translations.models import WordPL, WordZH, SentencePL, SentenceZH



NONE = 'a'
WORD_PL = 'b'
WORD_ZH = 'c'
SENTENCE_PL = 'd'
SENTENCE_ZH = 'e'
EXPLANATION = 'f'
EXPLANATION_IMAGE = 'g'

LANGUAGE_CHOICES = {
    (NONE, 'none'),
    (WORD_PL, 'word_pl'),
    (WORD_ZH, 'word_zh'),
    (SENTENCE_PL, 'sentence_pl'),
    (SENTENCE_ZH, 'sentence_zh'),
    (EXPLANATION, 'explanation'),
    (EXPLANATION_IMAGE, 'explanation_image')
}


class Exercise(models.Model):
    lesson = models.ForeignKey(Lesson)
    type = models.CharField(max_length=1, choices=LANGUAGE_CHOICES)
    number = models.IntegerField(null=True)

    @property
    def pretty_type_name(self):
        if self.type == WORD_PL:
            return 'Word PL'
        elif self.type == WORD_ZH:
            return 'Word ZH'
        elif self.type == SENTENCE_PL:
            return 'Sentence PL'
        elif self.type == SENTENCE_ZH:
            return 'Sentence ZH'
        elif self.type == EXPLANATION:
            return 'Explanation'
        elif self.type == EXPLANATION_IMAGE:
            return 'Explanation with image'
        raise Exception("Unknown type name: " + self.type)


    def __unicode__(self):
        return unicode(self.lesson) + ' ' + unicode(self.id)

    def type_name(self):
        return Exercise.exercise_type_to_name_map[self.type]


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

    def check(self, proposition):
        raise Exception("ExplanationExerciseDetails has no check method")

    def prepare(self):
        return {'text': self.text}

    def __unicode__(self):
        return unicode(self.text)


class ExplanationImageExercise(AbstractExercise):
    text = models.TextField()
    image = models.FileField(upload_to="image/")

    def check(self, proposition):
        raise Exception("ExplanationExerciseDetails has no check method")

    def prepare(self):
        return {'text': self.text}

    def __unicode__(self):
        return unicode(self.text)

exercise_type_to_name_map = {
    WORD_PL: 'word_pl',
    WORD_ZH: 'word_zh',
    SENTENCE_PL: 'sentence_pl',
    SENTENCE_ZH: 'sentence_zh',
    EXPLANATION: 'explanation',
    EXPLANATION_IMAGE: 'explanation_image'
}

exercise_type_to_model_map = {
    WORD_PL: WordPLExercise,
    WORD_ZH: WordZHExercise,
    SENTENCE_PL: SentencePLExercise,
    SENTENCE_ZH: SentenceZHExercise,
    EXPLANATION: ExplanationExercise,
    EXPLANATION_IMAGE: ExplanationImageExercise
}

exercise_model_to_type_map = {
    WordPLExercise: WORD_PL,
    WordZHExercise: WORD_ZH,
    SentencePLExercise: SENTENCE_PL,
    SentenceZHExercise: SENTENCE_ZH,
    ExplanationExercise: EXPLANATION,
    ExplanationImageExercise: EXPLANATION_IMAGE
}


def exercise_type_to_model(exercise_name):
    try:
        return exercise_type_to_model_map[exercise_name]
    except KeyError:
        raise Exception("Unknown exercise type: " + exercise_name)


def exercise_model_to_type(model):
    try:
        return exercise_model_to_type_map[model]
    except KeyError:
        raise Exception("Unknown exercise model: " + model)