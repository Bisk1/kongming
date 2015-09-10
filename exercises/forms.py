# -*- coding: utf-8 -*-

from django import forms
from django.utils.translation import ugettext_lazy as _
from exercises.models import Explanation, Choice
from translations.models import BusinessText
from translations.utils import Languages


class ExplanationForm(forms.ModelForm):

    class Meta:
        model = Explanation
        fields = ['text', 'image']
        labels = {
            'text': _('Treść'),
            'image': _('Obraz')
        }


class ChoiceForm(forms.Form):
    source_language = forms.ChoiceField(label='Język źródłowy', choices=((Languages.chinese.value, 'Chiński'),
                                                                         (Languages.polish.value, 'Polski')))
    text_to_translate = forms.CharField(label='Tekst do przetłumaczenia', max_length=255)
    correct_choice = forms.CharField(label='Prawidłowa odpowiedź', max_length=255)
    wrong_choice1 = forms.CharField(label='Błędna odpowiedź 1', max_length=255)
    wrong_choice2 = forms.CharField(label='Błędna odpowiedź 2', max_length=255)
    wrong_choice3 = forms.CharField(label='Błędna odpowiedź 3', max_length=255)

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
        print(source_language)
        target_language = Languages.other_language(source_language)
        self.instance.text_to_translate = BusinessText.objects.get_or_create(text=self.cleaned_data['text_to_translate'],
                                                                             language=source_language.value)[0]
        self.instance.correct_choice = BusinessText.objects.get_or_create(text=self.cleaned_data['correct_choice'],
                                                                          language=target_language.value)[0]
        self.instance.save()  # must save before adding many-to-many field instances
        self.instance.wrong_choices.add(BusinessText.objects.get_or_create(text=self.cleaned_data['wrong_choice1'],
                                                                           language=target_language.value)[0])
        self.instance.wrong_choices.add(BusinessText.objects.get_or_create(text=self.cleaned_data['wrong_choice2'],
                                                                           language=target_language.value)[0])
        self.instance.wrong_choices.add(BusinessText.objects.get_or_create(text=self.cleaned_data['wrong_choice3'],
                                                                           language=target_language.value)[0])
        return self.instance