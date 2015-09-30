# -*- coding: utf-8 -*-

from django import forms
from lessons.models import Lesson
from django.utils.translation import ugettext_lazy as _
from exercises.models import Exercise


class LessonForm(forms.ModelForm):

    class Meta:
        model = Lesson
        fields = ['topic', 'exercises_number', 'requirement']
        labels = {
            'topic': _('Temat'),
            'exercises_number': _('Liczba ćwiczeń'),
            'requirement': _('Wymaganie')
        }

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.instance.clean_exercises_number()

        for exercise_id, number in self._received_exercises_numbers():
            exercise = Exercise.objects.get(pk=exercise_id)
            exercise.number = number
            exercise.save()

    def _received_exercises_numbers(self):
        """
        Translations that were received in POST request
        :return:
        """
        for name, value in self.cleaned_data.items():
            if name.startswith('exercise_'):
                yield name[len('exercise_'):], value