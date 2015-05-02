from datetime import datetime, timedelta
import logging

from django.contrib.auth.models import User
from django.db import transaction
from django.template import loader
from django.contrib.auth import authenticate, login, logout
from django.core.urlresolvers import reverse
from django.http import *
from django.template import RequestContext

from forms import RegistrationForm
from models import Subscription


logger = logging.getLogger(__name__)


def login_my(request):
    """
    Handles username and password passed by user
    :param request: HTTP request
    :return: HTTP response
    """
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        login(request, user)
    else:
        pass


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
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password1'],
                email=form.cleaned_data['email']
            )
            user.save()
            subscription = Subscription(name=user,
                                        registration_date=datetime.now(),
                                        last_login_date=datetime.now(),
                                        abo_date=datetime.now() + timedelta(days=30))
            subscription.save()

            template = loader.get_template("users/register_success.html")
            variables = RequestContext(request, {'username': form.cleaned_data['username']})
            output = template.render(variables)
            return HttpResponse(output)
    else:
        form = RegistrationForm()
    template = loader.get_template("users/register.html")
    context = RequestContext(request, {'form': form})
    return HttpResponse(template.render(context))


def logout_page(request):
    """
    Handles user's logout and redirects to the main page
    :param request: HTTP request
    :return: HTTP response
    """
    logout(request)
    return HttpResponseRedirect(reverse("menu:index"))