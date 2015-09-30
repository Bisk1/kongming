from django.contrib.auth.decorators import login_required

from django.shortcuts import render


@login_required
def index(request):
    """
    Main page shown after login
    :param request:
    :return:
    """
    return render(request, 'menu/index.html')
