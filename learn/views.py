import json
import logging
from enum import Enum

from django.views.generic import View
from django.http import *
from django.shortcuts import render

from lessons.models import Lesson
from learn.models import LessonAction
from lessons.lessons_levels import determine_lessons_levels, serialize_lessons_levels


logger = logging.getLogger(__name__)


class LessonMapView(View):

    def get(self, request, *args, **kwargs):
        lessons_levels = determine_lessons_levels(request.user)
        serialized_lessons_levels = serialize_lessons_levels(lessons_levels)
        return render(request, 'learn/lessons_map.html', {'lessons_levels': serialized_lessons_levels})


class ExerciseOperation(Enum):
    PREPARE = 'prepare'
    CHECK = 'check'

class LearnView(View):
    """
    Accept requests to prepare and check exercises
    """
    def post(self, request, *args, **kwargs):
        lesson_action = LessonAction.objects.get(pk=request.POST.get('lesson_action_id'))
        operation = request.POST.get('operation')
        if operation == ExerciseOperation.CHECK.value:
            proposition = request.POST.get('proposition')
            response = lesson_action.check_answer(proposition)
        elif operation == ExerciseOperation.PREPARE.value:
            if lesson_action.has_next():
                lesson_action.next_exercise()
                response = lesson_action.prepare()
            else:
                response = lesson_action.get_final_response()
        else:
            return HttpResponseBadRequest()
        return JsonResponse(response)

    def get(self, request, *args, **kwargs):
        lesson = Lesson.objects.get(pk=self.kwargs['lesson_id'])
        LessonAction.objects.filter(user=request.user, lesson=lesson, status=None).delete()
        lesson_action = LessonAction.create_lesson_action(request.user, lesson=lesson)
        response = {'lesson_action': lesson_action}
        return render(request, 'learn/learn.html', response)
