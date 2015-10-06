# _*_ coding: utf-8 _*_
from django import forms
from templates.forms import MetroAdminFormHelper
from django.contrib.auth import authenticate

class RegistrationForm(forms.Form):

    helper = MetroAdminFormHelper()

    username = forms.CharField(label="Login",max_length=30)
    email = forms.EmailField(label="Email")
    password = forms.CharField(label="Hasło",widget=forms.PasswordInput())
    repeat_password = forms.CharField(label="Powtórz hasło",widget=forms.PasswordInput())

    def clean_repeat_password(self):
        password = self.cleaned_data.get('password')
        repeat_password = self.cleaned_data.get('repeat_password')
        if not password == repeat_password:
            raise forms.ValidationError('Podane hasła różnią się')
        return repeat_password

class LoginFormHelper(MetroAdminFormHelper):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.primary_submit_button.value = 'Zaloguj'


class LoginForm(forms.Form):

    helper = LoginFormHelper()

    username = forms.CharField(label="Użytkownik", max_length=30)
    password = forms.CharField(label="Hasło", widget=forms.PasswordInput())
    remember_me = forms.BooleanField(label="Zapamiętaj mnie", required=False)

    def clean(self):
        cleaned_data = super().clean()
        if not authenticate(username=cleaned_data.get('username'), password=cleaned_data.get('password')):
            raise forms.ValidationError(
                    "Nieprawidłowa nazwa użytkownika lub hasło"
                )
        return cleaned_data