import json
import logging

from django.contrib.auth.decorators import login_required
from django.http import *
from django.shortcuts import render

from lessons.models import Lesson
from learn.models import LessonAction
from lessons.lessons_levels import determine_lessons_levels, serialize_lessons_levels


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
    return render(request, 'learn/lessons_map.html', {'lessons_levels': serialized_lessons_levels})


@login_required
def learn(request, lesson_id):
    """
    It generates the exercise content. It handles ajax queries and sends
    new exercise content to be replaced so that next exercise is displayed.
    :param request: HTTP request
    :param lesson_id: id of the lesson that user will study
    :return: HTTP response
    """
    if request.is_ajax():
        lesson_action = LessonAction.objects.get(pk=request.POST.get('lesson_action_id'))
        proposition = request.POST.get('proposition')
        if proposition is not None:
            response = lesson_action.check_answer(proposition)
        else:
            if lesson_action.has_next():
                lesson_action.next_exercise()
                response = lesson_action.prepare()
            else:
                response = lesson_action.get_final_response()
        return JsonResponse(response)
    else:
        lesson = Lesson.objects.get(pk=lesson_id)
        LessonAction.objects.filter(user=request.user, lesson=lesson, status=None).delete()
        lesson_action = LessonAction.create_lesson_action(request.user, lesson=lesson)
        response = {'lesson_action': lesson_action}
        return render(request, 'learn/learn.html', response)