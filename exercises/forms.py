# -*- coding: utf-8 -*-

from django import forms
from django.utils.translation import ugettext_lazy as _
from exercises.models import Explanation


class ExplanationForm(forms.ModelForm):

    class Meta:
        model = Explanation
        fields = ['text', 'image']
        labels = {
            'text': _('Treść'),
            'image': _('Obraz')
        }



