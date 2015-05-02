import logging

from django.contrib.auth.decorators import login_required

from django.template import loader
from django.http import *
from django.template import RequestContext


@login_required
def index(request):
    """
    Main page shown after login
    :param request:
    :return:
    """
    template = loader.get_template('menu/index.html')
    context = RequestContext(request)
    return HttpResponse(template.render(context))


@login_required
def choose_language(request):
    """
    Form to choose application language
    :param request: HTTP request
    :return: HTTP response
    """
    template = loader.get_template('menu/choose_language.html')
    context = RequestContext(request)
    return HttpResponse(template.render(context))