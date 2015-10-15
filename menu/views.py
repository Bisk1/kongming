from django.contrib.auth.decorators import login_required

from django.shortcuts import redirect


@login_required
def index(request):
    """
    Main page shown after login
    :param request:
    :return:
    """
    return redirect('learn:lessons_map')
