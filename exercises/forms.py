# -*- coding: utf-8 -*-

from django import forms
from django.utils.translation import ugettext_lazy as _
from exercises.models import Explanation, Choice, Typing, Listening
from translations.models import BusinessText
from translations.utils import Languages
from templates.forms import MetroAdminFormHelper


class TypingForm(forms.Form):

    helper = MetroAdminFormHelper()
    helper.header2 = 'Exercise - writing'

    source_language = forms.ChoiceField(label='Source language', choices=((Languages.chinese.value, 'Chinese'),
                                                                         (Languages.english.value, 'English')))
    text_to_translate = forms.CharField(label='Text to translate', max_length=255, widget=forms.TextInput())
    translation_0 = forms.CharField(label='Translation', max_length=255)

    def __init__(self, *args, **kwargs):
        self.instance = kwargs.pop('instance', None)
        self.lesson = kwargs.pop('lesson')
        super().__init__(*args, **kwargs)
        if self.lesson:
            self.helper.header = 'Lesson: ' + self.lesson.topic
        if self.instance:
            self._instance_to_fields()
        else:
            self.instance = Typing()

    def _instance_to_fields(self):
        self.fields['source_language'].initial = self.instance.text_to_translate.language
        self.fields['text_to_translate'].initial = self.instance.text_to_translate.text
        for i, translation in enumerate(self.instance.text_to_translate.translations.all()):
            self.fields['translation_%s' % i] = forms.CharField(label='Translation', max_length=255,
                                                                initial=translation.text)

    def save(self):
        source_language = Languages(self.cleaned_data['source_language'])
        self.instance.text_to_translate = BusinessText.get_or_create_and_auto_tokenize(
            text=self.cleaned_data['text_to_translate'],
            language=source_language.value)[0]
        self.instance.text_to_translate.translations.clear()
        for translation in self._received_translations():
            self.instance.text_to_translate.add_translation(translation)
        self.instance.save()
        return self.instance

    def _received_translations(self):
        """
        Translations that were received in POST request
        :return:
        """
        for name, value in self.cleaned_data.items():
            if name.startswith('translation_'):
                yield value.strip()


class ExplanationForm(forms.ModelForm):

    helper = MetroAdminFormHelper()
    helper.header2 = 'Exercise - explanation'

    def __init__(self, *args, **kwargs):
        self.lesson = kwargs.pop('lesson')
        super().__init__(*args, **kwargs)
        if self.lesson:
            self.helper.header = 'Lesson: ' + self.lesson.topic

    class Meta:
        model = Explanation
        fields = ['text']
        labels = {
            'text': _('Content'),
        }


class ChoiceForm(forms.Form):

    helper = MetroAdminFormHelper()
    helper.header2 = 'Exercise - choice'

    source_language = forms.ChoiceField(label='Source language', choices=((Languages.chinese.value, 'Chinese'),
                                                                         (Languages.english.value, 'English')),
                                        widget=forms.RadioSelect)
    text_to_translate = forms.CharField(label='Text to translate', max_length=255)
    correct_choice = forms.CharField(label='Correct answer', max_length=255)
    wrong_choice1 = forms.CharField(label='Wrong answer 1', max_length=255)
    wrong_choice2 = forms.CharField(label='Wrong answer 2', max_length=255)
    wrong_choice3 = forms.CharField(label='Wrong answer 3', max_length=255)


    def __init__(self, *args, **kwargs):
        self.instance = kwargs.pop('instance', None)
        self.lesson = kwargs.pop('lesson')
        super().__init__(*args, **kwargs)
        if self.lesson:
            self.helper.header = 'Lesson: ' + self.lesson.topic
        if self.instance:
            self._instance_to_fields()
        else:
            self.instance = Choice()

    def _instance_to_fields(self):
        self.fields['source_language'].initial = self.instance.text_to_translate.language
        self.fields['text_to_translate'].initial = self.instance.text_to_translate.text
        self.fields['correct_choice'].initial = self.instance.correct_choice.text
        wrong_choices = self.instance.wrong_choices.all()
        self.fields['wrong_choice1'].initial = wrong_choices[0].text
        self.fields['wrong_choice2'].initial = wrong_choices[1].text
        self.fields['wrong_choice3'].initial = wrong_choices[2].text

    def save(self):
        source_language = Languages(self.cleaned_data['source_language'])
        target_language = Languages.other_language(source_language)
        self.instance.text_to_translate = BusinessText.get_or_create_and_auto_tokenize(
            text=self.cleaned_data['text_to_translate'],
            language=source_language.value)[0]
        self.instance.correct_choice = BusinessText.get_or_create_and_auto_tokenize(
            text=self.cleaned_data['correct_choice'],
            language=target_language.value)[0]

        self.instance.save()  # must save before adding many-to-many field instances
        self.instance.wrong_choices.clear()
        self.instance.wrong_choices.add(BusinessText.objects.get_or_create(text=self.cleaned_data['wrong_choice1'],
                                                                           language=target_language.value)[0])
        self.instance.wrong_choices.add(BusinessText.objects.get_or_create(text=self.cleaned_data['wrong_choice2'],
                                                                           language=target_language.value)[0])
        self.instance.wrong_choices.add(BusinessText.objects.get_or_create(text=self.cleaned_data['wrong_choice3'],
                                                                           language=target_language.value)[0])
        return self.instance


class ListeningForm(forms.Form):

    helper = MetroAdminFormHelper()
    helper.header2 = 'Exercise - listening'

    text = forms.CharField(label='Text to listen', max_length=255)
    audio = forms.FileField()

    def __init__(self, *args, **kwargs):
        self.instance = kwargs.pop('instance', None)
        self.lesson = kwargs.pop('lesson')
        super().__init__(*args, **kwargs)
        if self.lesson:
            self.helper.header = 'Lesson: ' + self.lesson.topic
        if self.instance:
            self._instance_to_fields()
        else:
            self.instance = Listening()

    def _instance_to_fields(self):
        self.fields['text'].initial = self.instance.text.text
        self.fields['audio'].initial = self.instance.audio

    def save(self):
        self.instance.text = BusinessText.get_or_create_and_auto_tokenize(
            text=self.cleaned_data['text'],
            language=Languages.chinese.value)[0]
        self.instance.audio = self.cleaned_data['audio']
        self.instance.save()
        return self.instance
