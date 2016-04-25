# -*- coding: utf-8 -*-
from crispy_forms.bootstrap import FormActions

from crispy_forms.helper import FormHelper
from crispy_forms.layout import HTML, Layout
from crispy_forms.layout import Submit
from django import forms
from django.template import loader
from django.utils.translation import ugettext_lazy as _

from lessons.models import Lesson
from exercises.models import Exercise
from recordings.models import Recording


class RecordingForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.header = "Recording: " + str(self.instance.text)
        self.helper.add_input(Submit('submit', 'Save', css_class='btn btn-primary'))
        self.helper.layout.append(HTML(loader.render_to_string('audio_player.html', {'audio_src': self.instance.url,
                                                                                  'unique_id': '1'})))

    class Meta:
        model = Recording
        fields = ['text', 'url']
        labels = {
            'text': _('Text'),
            'url': _('URL')
        }


class DeleteRecordingForm(forms.Form):

    def __init__(self, *args, **kwargs):
        instance = kwargs.pop('instance')
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.header = "Are you sure that you want delete the recording: " + str(instance) + "?"
        self.helper.add_layout(
            Layout(
                FormActions(
                    Submit('submit', 'Yes', css_class='btn btn-primary'),
                    HTML('<a class="btn btn-default" href={% url "recordings:recordings" %}>Return</a>')
                )
            )
        )