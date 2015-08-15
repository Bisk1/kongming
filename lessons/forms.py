# -*- coding: utf-8 -*-

from django import forms
from lessons.models import Lesson
from django.utils.translation import ugettext_lazy as _


class LessonForm(forms.ModelForm):

    class Meta:
        model = Lesson
        fields = ['topic', 'exercises_number', 'requirement']
        labels = {
            'topic': _('Temat'),
            'exercises_number': _('Liczba ćwiczeń'),
            'requirement': _('Wymaganie')
        }

    def __init__(self, *args, **kwargs):
        if 'exercises_ids' not in kwargs:
            super(LessonForm, self).__init__(*args, **kwargs)
        else:
            exercises_ids = kwargs.pop('exercises_ids')
            super(LessonForm, self).__init__(*args, **kwargs)

            for exercise_id in exercises_ids:
                self.fields['exercise_%s' % exercise_id] = forms.IntegerField()