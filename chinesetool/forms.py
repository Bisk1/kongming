# _*_ coding: utf-8 _*_
from django import forms


class RegistrationForm(forms.Form):
    username = forms.CharField(label="Login:",max_length=30)
    email = forms.EmailField(label="Email:")
    password1 = forms.CharField(label="Hasło:",widget=forms.PasswordInput())
    password2 = forms.CharField(label="Powtórz hasło:",widget=forms.PasswordInput())


class WordZHExerciseForm(forms.Form):
    word_zh = forms.CharField(label="New word")
    pinyin = forms.CharField(label="Pinyin")
    translations_pl = forms.CharField(label="Translations")
    number = forms.IntegerField()


class WordPLExerciseForm(forms.Form):
    word_pl = forms.CharField(label="New word")
    translations_zh = forms.CharField(label="Translations")
    number = forms.IntegerField()


class SentenceZHExerciseForm(forms.Form):
    sentence_zh = forms.CharField(label="New sentence")
    translations_pl = forms.CharField(label="Translations")
    number = forms.IntegerField()


class SentencePLExerciseForm(forms.Form):
    sentence_pl = forms.CharField(label="New sentence")
    translations_zh = forms.CharField(label="Translations")
    number = forms.IntegerField()


class ExplanationExerciseForm(forms.Form):
    text = forms.CharField(widget=forms.Textarea(), label="Explanation text")
    number = forms.IntegerField()


class AddLesson(forms.Form):
    text = forms.CharField()