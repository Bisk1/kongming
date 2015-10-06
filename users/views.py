from datetime import datetime, timedelta
import logging

from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.db import transaction
from django.contrib.auth import authenticate, login, logout

from users.forms import RegistrationForm, LoginForm
from users.models import Subscription

logger = logging.getLogger(__name__)


def login_my(request):
    """
    Handles username and password passed by user
    :param request: HTTP request
    :return: HTTP response
    """
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(username=form.cleaned_data.get('username'), password=form.cleaned_data.get('password'))
            login(request, user)
            return redirect(request.GET.get('next', "learn:lessons_map"))
    else:
        form = LoginForm()
    return render(request, "users/login.html", {"form": form})


@transaction.atomic
def register_page(request):
    """
    User can register here to get an account
    :param request: HTTP request
    :return: HTTP response
    """
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(
                username=form.cleaned_data.get('username'),
                password=form.cleaned_data.get('password'),
                email=form.cleaned_data.get('email')
            )
            user.save()
            subscription = Subscription(name=user,
                                        registration_date=datetime.now(),
                                        last_login_date=datetime.now(),
                                        abo_date=datetime.now() + timedelta(days=30))
            subscription.save()

            return render(request, "users/register_success.html", {'username': form.cleaned_data['username']})
    else:
        form = RegistrationForm()
    return render(request, "users/register.html", {"form": form})


def logout_page(request):
    """
    Handles user's logout and redirects to the main page
    :param request: HTTP request
    :return: HTTP response
    """
    logout(request)
    return redirect("users:login")