# -*- coding: utf-8 -*-

from django import forms
from django.utils.translation import ugettext_lazy as _

from lessons.models import Lesson
from exercises.models import Exercise


class LessonForm(forms.ModelForm):

    class Meta:
        model = Lesson
        fields = ['topic', 'exercises_number', 'requirement']
        labels = {
            'topic': _('Topic'),
            'exercises_number': _('Exercises number'),
            'requirement': _('Requirement')
        }

    def clean(self):
        cleaned_data = super(LessonForm, self).clean()
        for name, value in self.data.items():
            if name.startswith('exercise_'):
                cleaned_data[name] = value
        return cleaned_data

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.instance.clean_exercises_number()

        for exercise_id, number in self._received_exercises_numbers():
            exercise = Exercise.objects.get(pk=exercise_id)
            if number:
                exercise.number = number
            else:
                exercise.number = None
            exercise.save()
        return self.instance

    def _received_exercises_numbers(self):
        """
        Translations that were received in POST request
        :return:
        """
        for name, value in self.cleaned_data.items():
            if name.startswith('exercise_'):
                yield name[len('exercise_'):], value
