import abc
import random
from django.contrib.auth.models import User
from django.db import models
from enum import Enum
from chinesetool.learn import checkers

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

class Lesson(models.Model):
    """
    Single Chinese lesson is defined by level
    and words related to it.
    """
    topic = models.CharField(max_length=100, default="NO-NAME")
    exercises_number = models.IntegerField()
    requirements = models.ManyToManyField("self", symmetrical=False)

    def __unicode__(self):
        return unicode(self.topic)


class WordPL(models.Model):
    """
    Polish word has string value and set of
    Chinese translations related to it
    """
    word = models.CharField(max_length=100, unique=True)

    def __unicode__(self):
        return unicode(self.word)

    def get_translations(self): #TODO: Remove this method from all models - this logic should be in controller (.values())
        """
        Gets all accurate translations of this word
        :return: array of Chinese words
        """
        word_zh = list()
        for translation in self.wordzh_set.all():
            word_zh.append(translation.word)
        return word_zh

    def check_translation(self, word_zh_proposition):
        """
        Check if the Chinese word used by the user can be accepted for this Polish word
        :param word_zh_proposition: word in Chinese (string) typed in by the user
        :return: true if this translation is acceptable
        """
        correct_chinese_translations = self.get_translations()
        for chinese_word in correct_chinese_translations:
            if checkers.word_difference(chinese_word, word_zh_proposition) == 0:
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
        words_pl = list()
        for translation in self.wordpl_set.all():
            words_pl.append(translation.word)
        return words_pl

    def check_translation(self, word_pl_proposition):
        """
        Check if the Polish word used by the user can be accepted for this Chinese word
        :param word_pl_proposition: word in Polish (string) typed in by the user
        :return: true if this translation is acceptable
        """
        correct_polish_translations = self.get_translations()
        for polish_word in correct_polish_translations:
            if checkers.word_difference(polish_word, word_pl_proposition) < 2:
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
        Gets all accurate translations of this word
        :return: array of Chinese words
        """
        sentence_zh = list()
        for translation in self.sentencezh_set.all():
            sentence_zh.append(translation.sentence)
        return sentence_zh

    def check_translation(self, sentence_zh_proposition):
        """
        Check if the Chinese word used by the user can be accepted for this Polish word
        :param sentence_zh_proposition: word in Chinese (string) typed in by the user
        :return: true if this translation is acceptable
        """
        correct_chinese_translations = self.get_translations()
        for chinese_sentence in correct_chinese_translations:
            if checkers.sentence_difference(chinese_sentence, sentence_zh_proposition) < 2:
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
        Gets all accurate translations of this word
        :return: array of Polish words
        """
        sentences_pl = list()
        for translation in self.sentencepl_set.all():
            sentences_pl.append(translation.sentence)
        return sentences_pl

    def check_translation(self, sentence_pl_proposition):
        """
        Check if the Polish word used by the user can be accepted for this Chinese word
        :param sentence_pl_proposition: word in Polish (string) typed in by the user
        :return: true if this translation is acceptable
        """
        correct_polish_translations = self.get_translations()
        for polish_sentence in correct_polish_translations:
            if checkers.sentence_difference(polish_sentence, sentence_pl_proposition) < 2:
                return True
        return False


class SentenceTranslation(models.Model):
    """
    Pair of a Chinese sentence and a Polish sentence
    """
    class Meta:
        unique_together = ["sentence_zh", "sentence_pl"]

    sentence_zh = models.ForeignKey(SentenceZH)
    sentence_pl = models.ForeignKey(SentencePL)

    def __unicode__(self):
        return self.sentence_zh.sentence + " - " + self.sentence_pl.sentence


class Subscription(models.Model):
    name = models.ForeignKey(User)
    registration_date = models.DateTimeField()
    last_login_date = models.DateTimeField()
    abo_date = models.DateTimeField()

    def __unicode__(self):
        return unicode(self.name)


class WordSkill(models.Model):
    word_zh = models.ForeignKey(WordZH)
    user = models.ForeignKey(User)
    last_time = models.DateTimeField()
    correct = models.IntegerField(default=0)
    correct_run = models.IntegerField(default=0)
    wrong = models.IntegerField(default=0)


class LessonAction(models.Model):
    total_exercises_number = models.IntegerField(default=0)
    current_exercise_number = models.IntegerField(default=0)
    fails = models.IntegerField(default=0)
    user = models.ForeignKey(User)
    lesson = models.ForeignKey(Lesson, null=True)

    @classmethod
    def create_lesson_action(cls, user, lesson):
        exercises = lesson.exercise_set
        new_lesson_action = cls(total_exercises_number=lesson.exercises_number, current_exercise_number=0,
                                fails=0, user=user, lesson=lesson)
        new_lesson_action.save()

        fixed_choice_exercises_count = exercises.filter(number__isnull=False).count()
        random_choice_exercises_count = lesson.exercises_number - fixed_choice_exercises_count
        random_exercises = random.sample(exercises.all(), random_choice_exercises_count)
        j = 0
        for i in range(1, lesson.exercises_number + 1):
            try:
                exercise = exercises.get(number=i)
            except Exercise.DoesNotExist:
                exercise = random_exercises[j]
                j += 1
            new_exercise_action = ExerciseAction(exercise=exercise, lesson_action=new_lesson_action, number=i)
            new_exercise_action.save()
        return new_lesson_action

    def has_next(self):
        """
        Check if lesson has next exercise
        :return: true if lesson has next exercise
        """
        return self.current_exercise_number < self.total_exercises_number

    def next_exercise(self):
        self.current_exercise_number += 1
        self.save()

    def get_exercise_action(self):
        return ExerciseAction.objects.get(lesson_action=self, number=self.current_exercise_number)

    def check(self, proposition):
        response = self.get_exercise_action().check(proposition)
        if not response['success']:
            self.fails += 1
            self.save()
        return self.add_lesson_specific_data(response)

    def prepare(self):
        response = self.get_exercise_action().prepare()
        return self.add_lesson_specific_data(response)

    def get_final_response(self):
        response = {'final': True}
        return self.add_lesson_specific_data(response)

    def add_lesson_specific_data(self, response):
        response['fails'] = self.fails
        response['current_exercise_number'] = self.current_exercise_number
        response['total_exercises_number'] = self.total_exercises_number
        return response


class Exercise(models.Model):
    lesson = models.ForeignKey(Lesson)
    type = models.CharField(max_length=1, choices=LANGUAGE_CHOICES)
    number = models.IntegerField(null=True)

    exercise_type_to_name_map = {
        WORD_PL: 'word_pl',
        WORD_ZH: 'word_zh',
        SENTENCE_PL: 'sentence_pl',
        SENTENCE_ZH: 'sentence_zh',
        EXPLANATION: 'explanation',
        EXPLANATION_IMAGE: 'explanation_image'
    }

    def __unicode__(self):
        return unicode(self.lesson) + ' ' + unicode(self.id)

    def type_name(self):
        return self.exercise_type_to_name_map[self.type]


class ExerciseResultState(Enum):
    NOT_DONE = 0
    SUCCESS = 1
    FAILURE = 2


class ExerciseAction(models.Model):
    exercise = models.ForeignKey(Exercise)
    lesson_action = models.ForeignKey(LessonAction)
    result = models.IntegerField(default=ExerciseResultState.NOT_DONE)
    number = models.IntegerField()

    def check(self, proposition):
        response = self.get_description().check(proposition)
        if response['success']:
            self.result = ExerciseResultState.SUCCESS
        else:
            self.result = ExerciseResultState.FAILURE
        return response

    def prepare(self):
        response = self.get_description().prepare()
        response['exercise_type'] = self.exercise.type_name()
        return response

    def get_description(self):
        return self.get_description_model().objects.get(exercise=self.exercise)

    def get_description_model(self):
        return exercise_type_to_model(self.exercise.type)


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