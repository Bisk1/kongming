from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Button
from django import forms
from translations.utils import Languages


class BusinessTextInputWithTranslations(forms.TextInput):

    class Media:
        js = ('translations/js/business_text_input.js',
              'translations/js/common_translations.js',
              'translations/js/business_text_translations.js')

class WordInputWithTranslations(forms.TextInput):

    class Media:
        js = ('translations/js/word_input.js',
              'translations/js/common_translations.js',
              'translations/js/word_translations.js')


class WordsTranslationsForm(forms.Form):

    helper = FormHelper()
    helper.header2 = 'Words translations'

    helper.add_input(Button('add', 'Add translation'))
    helper.add_input(Submit('submit', 'Save', css_class='btn btn-primary'))

    source_language = forms.ChoiceField(label='Source language', choices=((Languages.chinese.value, 'Chinese'),
                                                                          (Languages.english.value, 'English')))
    source_word = forms.CharField(label='Word to translate', widget=WordInputWithTranslations)
    translation_0 = forms.CharField(label='Translation', max_length=255)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for name, value in self.data.items():
            if name.startswith('translation_'):
                self.fields[name] = forms.CharField(label='Translation', max_length=255, initial=value)

        for name, value in self.data.items():
            if name.startswith('pinyin_'):
                self.fields[name] = forms.CharField(label='Pinyin', max_length=255, initial=value)

    def translation_fields(self):
        for name, value in self.cleaned_data.items():
            if name.startswith('translation_'):
                yield value

    def pinyin_fields(self):
        for name, value in self.cleaned_data.items():
            if name.startswith('pinyin_'):
                yield value

class TextsTranslationsForm(forms.Form):

    helper = FormHelper()
    helper.header2 = 'Texts translations'

    helper.add_input(Button('add', 'Add translation'))
    helper.add_input(Submit('submit', 'Save', css_class='btn btn-primary'))

    source_language = forms.ChoiceField(label='Source language', choices=((Languages.chinese.value, 'Chinese'),
                                                                          (Languages.english.value, 'English')))
    source_text = forms.CharField(label='Text to translate', widget=BusinessTextInputWithTranslations)
    translation_0 = forms.CharField(label='Translation', max_length=255)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for name, value in self.data.items():
            if name.startswith('translation_'):
                self.fields[name] = forms.CharField(label='Translation', max_length=255, initial=value)

    def translation_fields(self):
        for name, value in self.cleaned_data.items():
            if name.startswith('translation_'):
                yield value