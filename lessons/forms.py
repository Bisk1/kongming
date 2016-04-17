# -*- coding: utf-8 -*-
from crispy_forms.bootstrap import FormActions

from crispy_forms.helper import FormHelper
from crispy_forms.layout import HTML, Layout
from crispy_forms.layout import Submit
from django import forms
from django.utils.translation import ugettext_lazy as _

from lessons.models import Lesson
from exercises.models import Exercise


class LessonForm(forms.ModelForm):

    helper = FormHelper()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper.form_tag = False
        if self.instance.id:
            self.helper.header = "Lesson: " + str(self.instance.topic)
        else:
            self.helper.header = "New lesson"

    class Meta:
        model = Lesson
        fields = ['topic', 'exercises_number', 'requirement', 'publish']
        labels = {
            'topic': _('Topic'),
            'exercises_number': _('Exercises number'),
            'requirement': _('Requirement'),
            'publish': _('Publish')
        }

    def clean(self):
        cleaned_data = super(LessonForm, self).clean()
        for name, value in self.data.items():
            if name.startswith('exercise_'):
                cleaned_data[name] = value
        return cleaned_data

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self._update_exercises_numbers()
        self.instance.clean_exercises_number()
        return self.instance

    def _update_exercises_numbers(self):
        for exercise_id, number in self._received_exercises_numbers():
            exercise = Exercise.objects.get(pk=exercise_id)
            if number:
                exercise.number = number
            else:
                exercise.number = None
            exercise.save()

    def _received_exercises_numbers(self):
        """
        Translations that were received in POST request
        :return:
        """
        for name, value in self.cleaned_data.items():
            if name.startswith('exercise_'):
                yield name[len('exercise_'):], value

class DeleteLessonForm(forms.Form):

    helper = FormHelper()

    def __init__(self, *args, **kwargs):
        instance = kwargs.pop('instance')
        super().__init__(*args, **kwargs)
        self.helper.header = "Are you sure that you want delete the lesson: " + str(instance) + "?"
        self.helper.add_layout(
            Layout(
                FormActions(
                    Submit('submit', 'Yes', css_class='btn btn-primary'),
                    HTML('<a class="btn btn-default" href={% url "lessons:lessons" %}>Return</a>')
                )
            )
        )