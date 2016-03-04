# -*- coding: utf-8 -*-

import random
import re
from string import Template

from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models
from redactor.fields import RedactorField
from django.template.loader import render_to_string

from lxml import etree

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
        return {'language': self.text_to_translate.language}

    def render(self):
        return render_to_string('learn/typing.html',
                                {'text': ChineseHelper.render_chinese_to_html(self.text_to_translate.text)})

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
        return {}

    def render(self):
        return render_to_string('learn/choice.html',
                                {'text': ChineseHelper.render_chinese_to_html(self.text_to_translate.text),
                                 'choices': self._get_all_choices_in_random_order()})

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
        redactor_options={'focus': 'true', 'plugins': ['audio']},
        allow_image_upload=True
    )

    def check_answer(self, proposition):
        raise Exception("Explanation has no check method")

    def prepare(self):
        return {}

    def render(self):
        rendered_text = ChineseHelper.render_chinese_to_html(self.text)
        rendered_text = AudioHelper.render_audio_players(rendered_text)
        return render_to_string('learn/explanation.html', {'text': rendered_text})

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
        return {}

    def render(self):
        return render_to_string('learn/listening.html', {'audio_url': self.audio.url})

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


class AudioHelper():
    audio_player_template = Template(
        """<div id="$unique_id" class="cp-container" audio-src="$audio_src">
             <div class="cp-jplayer"></div>
             <div class="cp-buffer-holder cp-gt50" style="display: block;">
                <div class="cp-buffer-1" style="transform: rotate(180deg);"></div>
                <div class="cp-buffer-2" style="display: block; transform: rotate(271.362deg);"></div>
            </div>
            <div class="cp-progress-holder" style="display: block;">
                <div class="cp-progress-1" style="transform: rotate(94.2428deg);"></div>
                <div class="cp-progress-2" style="transform: rotate(0deg); display: none;"></div>
            </div>
            <div class="cp-circle-control"></div>
            <ul class="cp-controls">
                <li><a class="cp-play" tabindex="1" style="display: block;">play</a></li>
                <li><a class="cp-pause" style="display: none;" tabindex="1">pause</a></li>
            </ul>
        </div>""".replace('\n', '')
    )

    @classmethod
    def render_audio_players(cls, text_to_render):
        parser = etree.HTMLParser()
        root = etree.fromstring(text_to_render, parser)
        regexpNS = 'http://exslt.org/regular-expressions'  # to enable regex
        audio_link_elements = root.xpath("//a[re:test(@href, 'wav$')]", namespaces={'re': regexpNS})  # all wav files

        for index, audio_link_element in enumerate(audio_link_elements):
            audio_src = audio_link_element.attrib['href']
            rendered_player = cls.audio_player_template.substitute(audio_src=audio_src,
                                                                   unique_id='player-id-' + str(index))
            player_element = etree.fromstring(rendered_player)
            audio_link_element.getparent().replace(audio_link_element, player_element)
        res = etree.tostring(root, encoding='unicode')
        res = cls.unwrap(res)  # tree ends up wrapped in <html> and <body> elements that must be stripped
        return res

    @classmethod
    def unwrap(cls, text):
        if text.startswith("<html><body>") and text.endswith("</body></html>"):
            return text[12:len(text) - 14]
        else:
            raise Exception("Unexpected form of rendered HTML")
