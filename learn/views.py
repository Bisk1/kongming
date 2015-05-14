import json
import logging

from django.contrib.auth.decorators import login_required
from django.template import loader
from django.http import *
from django.template import RequestContext
from django.core import serializers

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
    lessons_levels = determine_lessons_levels()
    lessons_levels_serialized = "[" + ",".join(serializers.serialize('json', query_set) for query_set in lessons_levels) + "]"
    context = RequestContext(request, {'lessons': lessons,
                                       'lessons_levels': lessons_levels_serialized})
    return HttpResponse(template.render(context))


def determine_lessons_levels():
    levels = list()
    next_level = Lesson.objects.filter(requirement=None).order_by('pk')  # first level - no requirements
    while next_level:
        levels.append(next_level)
        # Each level requires lessons from previous level.
        # Ordering prevents crossing lines in template (lessons are close to their requirements).
        next_level = Lesson.objects.filter(requirement__in=next_level).order_by('requirement')
    return levels


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