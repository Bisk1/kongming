import json
import logging

from django.contrib.auth.decorators import login_required
from django.template import loader
from django.http import *
from django.template import RequestContext

from lessons.models import LessonAction, Lesson

logger = logging.getLogger(__name__)


@login_required
def lessons_map(request):
    """
    Displays available lessons
    :param request: HTTP request
    :return: HTTP response
    """
    lessons_levels = determine_lessons_levels(request.user)
    serialized_lessons_levels = serialize_lessons_levels(lessons_levels)
    template = loader.get_template('learn/lessons_map.html')
    context = RequestContext(request, {'lessons_levels': serialized_lessons_levels})
    return HttpResponse(template.render(context))


def serialize_lessons_levels(lessons_levels):
    levels_serialized = list()
    for level in lessons_levels:
        level_serialized_list = [json.dumps(lesson) for lesson in level]
        level_serialized = "[" + ",".join(level_serialized_list) + "]"
        levels_serialized.append(level_serialized)
    return "[" + ",".join(levels_serialized) + "]"


def determine_lessons_levels(user):
    """
    Determine lessons levels - first level contains all lessons that don't have requirements.
    Each next level contains all lessons that require any lesson from previous level.
    Each level is related to a single row in lessons map.
    :return: list of lessons levels
    """
    levels = list()
    current_level = Lesson.objects.filter(requirement=None).order_by('pk') # first level - no requirements
    while current_level:
        levels.append(simple_lesson_level_dicts(current_level, user))
        # Each level requires lessons from previous level.
        # Ordering prevents crossing lines in template (lessons are close to their requirements).
        current_level = Lesson.objects.filter(requirement__in=current_level).order_by('requirement')
    return levels


def simple_lesson_level_dicts(lessons_query_set, user):
    """
    Custom conversion of list of Django QuerySets to list of dicts.
    Created to increase flexibility and optimality.
    :param lessons_query_set:
    :return:
    """
    lessons_levels_dicts = list()
    for lesson in lessons_query_set:
        if lesson.requirement is None:
            lessons_levels_dicts.append({'pk': lesson.pk, 'topic': lesson.topic, 'requirement': None,
                                         'status': lesson.determine_status(user)})
        else:
            lessons_levels_dicts.append({'pk': lesson.pk, 'topic': lesson.topic, 'requirement': lesson.requirement.pk,
                                         'status': lesson.determine_status(user)})
    return lessons_levels_dicts


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