import abc
from django.contrib.auth.models import User
from django.db import models
from enum import Enum
from chinesetool.learn import checkers
from chinesetool.utils.model_utils import get_random_list

NUMBER_OF_EXERCISES_PER_LESSON_ACTION = 5

NONE = 'a'
WORD_PL = 'b'
WORD_ZH = 'c'
SENTENCE_PL = 'd'
SENTENCE_ZH = 'e'
EXERCISE_TYPE = (
    (NONE, 'none'),
    (WORD_PL, 'word_pl'),
    (WORD_PL, 'word_zh'),
    (SENTENCE_PL, 'sentence_pl'),
    (SENTENCE_ZH, 'sentence_zh'),
)


class Lesson(models.Model):
    """
    Single Chinese lesson is defined by level
    and words related to it.
    """
    level = models.IntegerField(default=0)

    def __unicode__(self):
        return unicode(self.level)


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
            if checkers.word_difference(chinese_word, word_zh_proposition) < 2:
                return True
        return False


class WordZH(models.Model):
    """
    Chinese word contains string value and set of
    Polish translations related to it
    """
    word = models.CharField(max_length=50)
    pinyin = models.CharField(max_length=100)
    lesson = models.ForeignKey(Lesson, null=True, default=0)
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
    sentence = models.TextField(unique=True)

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
    sentence = models.TextField(unique=True)
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
        return self.word_zh.word + " - " + self.word_pl.word


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
    def create_word_lesson_action(cls, user, lesson=None,
                                  number_of_exercises=NUMBER_OF_EXERCISES_PER_LESSON_ACTION):
        new_lesson_action = cls(total_exercises_number=number_of_exercises, current_exercise_number=0,
                                fails=0, user=user, lesson=lesson)
        new_lesson_action.save()

        if lesson is None:
            words = get_random_list(WordZH, number_of_exercises)
        else:
            words = get_random_list(WordZH.objects.filter(lesson=lesson), number=number_of_exercises)
        i = 1
        for word in words:
            new_exercise = ExerciseAction(type=WORD_ZH, lesson_action=new_lesson_action, number=i)
            new_exercise.save()
            WordZHExerciseActionDescription(word=word,
                                            exercise=new_exercise).save()  # TODO: should use multiple actions
            i += 1
        return new_lesson_action

    @classmethod
    def create_sentence_lesson_action(cls, user, lesson=None,
                                      number_of_exercises=NUMBER_OF_EXERCISES_PER_LESSON_ACTION):
        new_lesson_action = cls(total_exercises_number=number_of_exercises, current_exercise_number=0,
                                fails=0, user=user, lesson=lesson)
        new_lesson_action.save()

        if lesson is None:
            sentences = get_random_list(SentenceZH, number_of_exercises)
        else:
            sentences = get_random_list(SentenceZH.objects.filter(lesson=lesson), number=number_of_exercises)
        i = 1
        for sentence in sentences:
            new_exercise = ExerciseAction(type=SENTENCE_ZH, lesson_action=new_lesson_action, number=i)
            new_exercise.save()
            SentenceZHExerciseActionDescription(sentence=sentence,
                                                exercise=new_exercise).save()
            i += 1
        return new_lesson_action

    def has_next(self):
        """
        Check if lesson has next exercise
        :return: true if lesson has next exercise
        """
        return self.current_exercise_number <= self.total_exercises_number - 1

    def next_exercise(self):
        self.current_exercise_number += 1
        self.save()

    def get_exercise(self):
        return ExerciseAction.objects.get(lesson_action=self, number=self.current_exercise_number)

    def check(self, proposition):
        response = self.get_exercise().check(proposition)
        if not response['success']:
            self.fails += 1
            self.save()
        return self.add_lesson_specific_data(response)

    def prepare(self):
        response = self.get_exercise().prepare()
        return self.add_lesson_specific_data(response)

    def get_final_response(self):
        response = {'final': True}
        return self.add_lesson_specific_data(response)

    def add_lesson_specific_data(self, response):
        response['fails'] = self.fails
        response['current_exercise_number'] = self.current_exercise_number
        response['total_exercises_number'] = self.total_exercises_number
        return response


class ExerciseResultState(Enum):
    NOT_DONE = 0
    SUCCESS = 1
    FAILURE = 2


class ExerciseAction(models.Model):
    type = models.CharField(max_length=1, choices=EXERCISE_TYPE, default=NONE)
    lesson_action = models.ForeignKey(LessonAction)
    number = models.IntegerField(default=0)
    result = models.IntegerField(default=ExerciseResultState.NOT_DONE)

    def check(self, proposition):
        response = self.get_description().check(proposition)
        if response['success']:
            self.result = ExerciseResultState.SUCCESS
        else:
            self.result = ExerciseResultState.FAILURE
        return response

    def prepare(self):
        return self.get_description().prepare()

    def get_description(self):
        return self.get_description_model().objects.get(exercise=self)

    def get_description_model(self):
        if self.type == WORD_ZH:
            return WordZHExerciseActionDescription
        if self.type == WORD_PL:
            return WordPLExerciseActionDescription
        if self.type == SENTENCE_ZH:
            return SentenceZHExerciseActionDescription
        if self.type == SENTENCE_PL:
            return SentencePLExerciseActionDescription
        else:
            raise Exception("Unknown exercise type")


class AbstractExerciseActionDescription(models.Model):
    exercise = models.ForeignKey(ExerciseAction)

    @abc.abstractmethod
    def check(self, proposition):
        pass

    @abc.abstractmethod
    def prepare(self):
        pass


class WordZHExerciseActionDescription(AbstractExerciseActionDescription):
    word = models.ForeignKey(WordZH)

    def check(self, proposition):
        return {'success': self.word.check_translation(proposition),
                'correct_word': self.word.wordpl_set.all()[0].word}

    def prepare(self):
        return {'word_to_display': self.word.word}


class WordPLExerciseActionDescription(AbstractExerciseActionDescription):
    word = models.ForeignKey(WordPL)

    def check(self, proposition):
        return {'success': self.word.check_translation(proposition),
                'correct_word': self.word.wordzh_set.all()[0].word}

    def prepare(self):
        return {'word_to_display': self.word.word}


class SentenceZHExerciseActionDescription(AbstractExerciseActionDescription):
    sentence = models.ForeignKey(SentenceZH)

    def check(self, proposition):
        return {'success': self.sentence.check_translation(proposition),
                'correct_sentence': self.sentence.sentencepl_set.all()[0].sentence}

    def prepare(self):
        return {'sentence_to_display': self.sentence.sentence}


class SentencePLExerciseActionDescription(AbstractExerciseActionDescription):
    sentence = models.ForeignKey(SentencePL)

    def check(self, proposition):
        return {'success': self.sentence.check_translation(proposition),
                'correct_sentence': self.sentence.sentencezh_set.all()[0].sentence}

    def prepare(self):
        return {'sentence_to_display': self.sentence.sentence}