import json
import logging

from django.contrib.auth.decorators import login_required
from django.template import loader
from django.http import *
from django.template import RequestContext

from lessons.models import LessonAction, Lesson

logger = logging.getLogger(__name__)


def lessons_map(request):
    """
    Displays available lessons
    :param request: HTTP request
    :return: HTTP response
    """
    lessons = Lesson.objects.all()
    template = loader.get_template('learn/lessons_map.html')
    context = RequestContext(request, {'lessons': lessons})
    return HttpResponse(template.render(context))


@login_required
def learn(request, lesson_id):
    """
    It generates the exercise content. It handles ajax queries and sends
    new exercise content to be replaced so that next exercise is displayed.
    :param request: HTTP request
    :param lesson_id: id of the lesson that user will study
    :return: HTTP response
    """
    lesson = Lesson.objects.get(pk=lesson_id)
    if request.is_ajax():
        lesson_action = LessonAction.objects.get(lesson=lesson, user=request.user)
        proposition = request.POST.get('proposition')
        if proposition is not None:
            response = lesson_action.check(proposition)
        else:
            if lesson_action.has_next():
                lesson_action.next_exercise()
                response = lesson_action.prepare()
            else:
                response = lesson_action.get_final_response()
        return HttpResponse(json.dumps(response),
                            content_type='application/javascript')
    LessonAction.objects.filter(user=request.user).delete()
    lesson_action = LessonAction.create_lesson_action(request.user, lesson=lesson)
    response = {'lesson_action': lesson_action}
    template = loader.get_template('learn/learn.html')
    context = RequestContext(request, response)
    return HttpResponse(template.render(context))