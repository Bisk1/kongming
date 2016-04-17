# _*_ coding: utf-8 _*_
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from crispy_forms.layout import Reset

from django import forms
from django.contrib.auth import authenticate


class RegistrationForm(forms.Form):

    helper = FormHelper()
    helper.header = 'Registration'
    helper.add_input(Submit('submit', 'Register'))
    helper.add_input(Reset('reset', 'Reset'))

    username = forms.CharField(label="Login",max_length=30)
    email = forms.EmailField(label="Email")
    password = forms.CharField(label="Password",widget=forms.PasswordInput())
    repeat_password = forms.CharField(label="Repeat password",widget=forms.PasswordInput())

    def clean_repeat_password(self):
        password = self.cleaned_data.get('password')
        repeat_password = self.cleaned_data.get('repeat_password')
        if not password == repeat_password:
            raise forms.ValidationError('The password are different')
        return repeat_password


class LoginForm(forms.Form):

    helper = FormHelper()
    helper.header = 'Log in'
    helper.add_input(Submit('submit', 'Log in'))
    helper.add_input(Reset('reset', 'Reset'))

    username = forms.CharField(label="Username", max_length=30)
    password = forms.CharField(label="Password", widget=forms.PasswordInput())
    remember_me = forms.BooleanField(label="Remember me", required=False)

    def clean(self):
        cleaned_data = super().clean()
        if not authenticate(username=cleaned_data.get('username'), password=cleaned_data.get('password')):
            raise forms.ValidationError(
                    "Bad username or password"
                )
        return cleaned_data