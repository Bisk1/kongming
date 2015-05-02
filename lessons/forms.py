# _*_ coding: utf-8 _*_
from django import forms


class WordZHExerciseForm(forms.Form):
    word_zh = forms.CharField(label="New word")
    pinyin = forms.CharField(label="Pinyin")
    translations_pl = forms.CharField(label="Translations")
    number = forms.IntegerField(required=False)


class WordPLExerciseForm(forms.Form):
    word_pl = forms.CharField(label="New word")
    translations_zh = forms.CharField(label="Translations")
    number = forms.IntegerField(required=False)


class SentenceZHExerciseForm(forms.Form):
    sentence_zh = forms.CharField(label="New sentence")
    translations_pl = forms.CharField(label="Translations")
    number = forms.IntegerField(required=False)


class SentencePLExerciseForm(forms.Form):
    sentence_pl = forms.CharField(label="New sentence")
    translations_zh = forms.CharField(label="Translations")
    number = forms.IntegerField(required=False)


class ExplanationExerciseForm(forms.Form):
    text = forms.CharField(widget=forms.Textarea(), label="Explanation text")
    number = forms.IntegerField(required=False)


class ExplanationImageExerciseForm(forms.Form):
    text = forms.CharField(widget=forms.Textarea(), label="Explanation text")
    file  = forms.FileField()
    number = forms.IntegerField(required=False)


class AddLesson(forms.Form):
    text = forms.CharField()