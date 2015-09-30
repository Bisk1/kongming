# -*- coding: utf-8 -*-

from django import forms
from django.utils.translation import ugettext_lazy as _
from exercises.models import Explanation, Choice, Typing
from translations.models import BusinessText
from translations.utils import Languages
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout


class MetroAdminFormHelper(FormHelper):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.form_class='form-horizontal'
        self.form_method='post'
        self.label_class='col-lg-4'
        self.field_class='col-lg-8'
        self.add_input(Submit('submit', 'Zapisz', css_class='btn btn-primary'))


class TypingForm(forms.Form):

    helper = MetroAdminFormHelper()

    source_language = forms.ChoiceField(label='Język źródłowy', choices=((Languages.chinese.value, 'Chiński'),
                                                                         (Languages.polish.value, 'Polski')))
    text_to_translate = forms.CharField(label='Tekst do przetłumaczenia', max_length=255, widget=forms.TextInput())
    translation_0 = forms.CharField(label='Tłumaczenie', max_length=255)

    def __init__(self, *args, **kwargs):
        self.instance = kwargs.pop('instance', None)
        super().__init__(*args, **kwargs)
        if self.instance:
            self._instance_to_fields()
        else:
            self.instance = Typing()

    def _instance_to_fields(self):
        self.fields['source_language'].initial = self.instance.text_to_translate.language
        self.fields['text_to_translate'].initial = self.instance.text_to_translate.text
        for i, translation in enumerate(self.instance.text_to_translate.translations.all()):
            self.fields['translation_%s' % i] = forms.CharField(label='Tłumaczenie', max_length=255,
                                                                initial=translation.text)

    def save(self):
        source_language = Languages(self.cleaned_data['source_language'])
        self.instance.text_to_translate = BusinessText.objects.get_or_create(text=self.cleaned_data['text_to_translate'],
                                                                             language=source_language.value)[0]
        for translation in self._received_translations():
            self.instance.text_to_translate.add_translation(translation)
        self.instance.text_to_translate.auto_tokenize()
        self.instance.save()
        return self.instance

    def _received_translations(self):
        """
        Translations that were received in POST request
        :return:
        """
        for name, value in self.cleaned_data.items():
            if name.startswith('translation_'):
                yield value


class ExplanationForm(forms.ModelForm):

    helper = MetroAdminFormHelper()

    class Meta:
        model = Explanation
        fields = ['text', 'image']
        labels = {
            'text': _('Treść'),
            'image': _('Obraz')
        }


class ChoiceForm(forms.Form):
    source_language = forms.ChoiceField(label='Język źródłowy', choices=((Languages.chinese.value, 'Chiński'),
                                                                         (Languages.polish.value, 'Polski')),
                                        widget=forms.RadioSelect)
    text_to_translate = forms.CharField(label='Tekst do przetłumaczenia', max_length=255)
    correct_choice = forms.CharField(label='Prawidłowa odpowiedź', max_length=255)
    wrong_choice1 = forms.CharField(label='Błędna odpowiedź 1', max_length=255)
    wrong_choice2 = forms.CharField(label='Błędna odpowiedź 2', max_length=255)
    wrong_choice3 = forms.CharField(label='Błędna odpowiedź 3', max_length=255)

    helper = MetroAdminFormHelper()

    def __init__(self, *args, **kwargs):
        self.instance = kwargs.pop('instance', None)
        super().__init__(*args, **kwargs)
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
        self.instance.text_to_translate = BusinessText.objects.get_or_create(text=self.cleaned_data['text_to_translate'],
                                                                             language=source_language.value)[0]
        self.instance.text_to_translate.auto_tokenize()
        self.instance.correct_choice = BusinessText.objects.get_or_create(text=self.cleaned_data['correct_choice'],
                                                                          language=target_language.value)[0]
        self.instance.correct_choice.auto_tokenize()
        self.instance.save()  # must save before adding many-to-many field instances
        self.instance.wrong_choices.clear()
        self.instance.wrong_choices.add(BusinessText.objects.get_or_create(text=self.cleaned_data['wrong_choice1'],
                                                                           language=target_language.value)[0])
        self.instance.wrong_choices.add(BusinessText.objects.get_or_create(text=self.cleaned_data['wrong_choice2'],
                                                                           language=target_language.value)[0])
        self.instance.wrong_choices.add(BusinessText.objects.get_or_create(text=self.cleaned_data['wrong_choice3'],
                                                                           language=target_language.value)[0])
        return self.instance