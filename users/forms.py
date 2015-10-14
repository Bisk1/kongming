# _*_ coding: utf-8 _*_
from django import forms
from templates.forms import MetroAdminFormHelper
from django.contrib.auth import authenticate

class RegistrationForm(forms.Form):

    helper = MetroAdminFormHelper()
    helper.header = 'Registeration'

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

class LoginFormHelper(MetroAdminFormHelper):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.primary_submit_button.value = 'Log in'


class LoginForm(forms.Form):

    helper = LoginFormHelper()
    helper.header = 'Log in'

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