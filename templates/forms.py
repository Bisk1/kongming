__author__ = 'daniel'

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Reset


class MetroAdminFormHelper(FormHelper):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.primary_submit_button = Submit('submit', 'Save')  # can modify in subclass
        self.add_input(self.primary_submit_button)
        self.add_input(Reset('reset', 'Reset'))
