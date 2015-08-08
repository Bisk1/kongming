from django import forms
from lessons.models import Lesson


class LessonForm(forms.Form):
    topic = forms.CharField(label='Temat lekcji', max_length=100)
    exercises_number = forms.IntegerField(label='Liczba cwiczen')
    requirement = forms.ModelChoiceField(label='Wymaganie', queryset=Lesson.objects.all())