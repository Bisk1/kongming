# -*- coding: utf-8 -*-

import random

from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models
import re
from redactor.fields import RedactorField
from django.template.loader import render_to_string

from lessons.models import Lesson
from translations.comparators import texts_difference
from translations.models import BusinessText
from translations.utils import Languages
from words.models import WordZH


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

    def render(self):
        raise NotImplementedError


class Typing(AbstractExercise):
    text_to_translate = models.ForeignKey(BusinessText)

    def check_answer(self, proposition):
        return {'success': self.text_to_translate.check_translation(proposition),
                'correct_translation': self.text_to_translate.translations.first().text}

    def prepare(self):
        return {'text': ChineseHelper.render_chinese_to_html(self.text_to_translate.text),
                'language': self.text_to_translate.language}

    def render(self):
        return render_to_string('learn/typing.html', self.prepare())

    def __str__(self):
        return 'Typing - [{0}] Text: {1} |' \
               'Translations: {2}'.format(self.text_to_translate.language,
                                          self.text_to_translate.text,
                                          ', '.join([translation.text for translation in
                                                     self.text_to_translate.translations.all()]))

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
        return {'text': ChineseHelper.render_chinese_to_html(self.text_to_translate.text),
                'choices': self._get_all_choices_in_random_order(),
                'language': self.text_to_translate.language}

    def render(self):
        return render_to_string('learn/choice.html', self.prepare())

    def __str__(self):
        return 'Choice - [{0}] Text: {1} |' \
               'Correct answer: {2}'.format(self.text_to_translate.language,
                                            self.text_to_translate.text,
                                            self.correct_choice.text)

    def __repr__(self):
        return str(self)

    def _get_all_choices_in_random_order(self):
        """
        Provide all choices with no way to determine the right one
        :return: list of all available choices
        """
        all_choices = [business_text.text for business_text in self.wrong_choices.all()]
        all_choices.append(self.correct_choice.text)
        random.shuffle(all_choices)
        return all_choices


class Explanation(AbstractExercise):
    text = RedactorField(
        verbose_name=u'Text',
        redactor_options={'focus': 'true'},
        allow_image_upload=True
    )

    def check_answer(self, proposition):
        raise Exception("Explanation has no check method")

    def prepare(self):
        return {'text': ChineseHelper.render_chinese_to_html(self.text)}

    def render(self):
        return render_to_string('learn/explanation.html', self.prepare())

    def __str__(self):
        return "Explanation - " + str(self.text)

    def __repr__(self):
        return str(self)


class Listening(AbstractExercise):
    text = models.ForeignKey(BusinessText)
    audio = models.FileField(upload_to='wav')

    def check_answer(self, proposition):
        return {'success': texts_difference(proposition, self.text.text) == 0,
                'text': self.text.text}

    def prepare(self):
        return {'audio_url': self.audio.url}

    def render(self):
        return render_to_string('learn/listening.html', self.prepare())

    def __str__(self):
        return "Listening - " + str(self.text.text)

    def __repr__(self):
        return str(self)


class ChineseHelper():
    CHINESE_SUBSTRING_REGEX = re.compile(r'[\u4e00-\u9fff]+')

    @classmethod
    def render_chinese_to_html(cls, text_to_render):
        """
        Render text to HTML where each Chinese word has its own span element
        of class chinese_word with pinyin in data-pinyin attribute
        1) Find all substrings consisting of Chinese characters with regex
        2) Tokenize the substring into Chinese words
        3) Wrap each word
        :param text_to_render:
        :return: rendered text
        """
        return cls.CHINESE_SUBSTRING_REGEX.sub(cls._break_and_wrap, text_to_render)

    @staticmethod
    def _break_and_wrap(text_to_tokenize_match):
        text_to_tokenize = text_to_tokenize_match.group(0)
        wrapped = ""
        for token in Languages.tokenize(Languages.chinese.value, text_to_tokenize):
            word_zh = WordZH.get_or_create_with_translator(word=token)[0]
            wrapped += '<span class="chinese-word"><span>' + word_zh.pinyin + '</span><span>' + token + '</span></span>'
        return wrapped
