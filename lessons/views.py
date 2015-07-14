import logging

from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from django.http import *
from django.template import loader, RequestContext

from models import Lesson
from exercises.models import Exercise, ExerciseType


logger = logging.getLogger(__name__)


def lessons(request):
    """
    Displays available lessons for modifying and adding new lessons
    :param request: HTTP request
    :return: HTTP response
    """
    if request.method == 'POST':
        if request.POST.get('create', False):
            lesson = Lesson(topic=request.POST.get('topic'), exercises_number=0)
            lesson.save()
            return HttpResponseRedirect(reverse('lessons:modify_lesson', args=(lesson.id,)))
        elif request.POST.get('delete', False):
            lesson = Lesson.objects.get(id=request.POST.get('lesson_id'))
            lesson.delete()
    lessons = Lesson.objects.all()
    return render(request, 'lessons/lessons.html', {'lessons': lessons})


def modify_lesson(request, lesson_id):

    """
    Modifies lesson - allows to change requirement and exercises
    :param request: HTTP request
    :return: HTTP response
    """
    lesson = Lesson.objects.get(pk=lesson_id)
    if request.method == 'POST':
        if request.POST.get('topic', False):
            lesson.topic = request.POST.get('topic')
            lesson.save()
        if request.POST.get('exercises_number', False):
            lesson.exercises_number = request.POST.get('exercises_number')
            lesson.save()
        if request.POST.get('requirement', False):
            requirement_id = request.POST.get('requirement')
            if requirement_id != "None":
                requirement = Lesson.objects.get(pk=requirement_id)
                lesson.requirement = requirement
            else:
                lesson.requirement = None
            lesson.save()
        exercises = Exercise.objects.filter(lesson=lesson)
        for exercise in exercises:
            name_of_exercise_number_in_form = 'exercise' + str(exercise.id)
            if request.POST.get(name_of_exercise_number_in_form, False):
                exercise.number = request.POST.get(name_of_exercise_number_in_form)
                exercise.save()
        if request.POST.get('exercise_to_remove', False):
            exercise_to_remove = Exercise.objects.get(pk=request.POST.get('exercise_to_remove'))
            exercise_to_remove.delete()
    other_lessons = Lesson.objects.all().order_by('-topic')
    exercises = Exercise.objects.filter(lesson=lesson).order_by('number')
    exercises_types = ExerciseType.objects.all()

    return render(request, 'lessons/lesson.html', {'lesson': lesson,
                                                          'exercises': exercises,
                                                          'other_lessons': other_lessons,
                                                          'exercises_types': exercises_types
                                                          })


def delete_lesson(request, lesson_id):
    """
    Delete lesson and redirect to lessons management page
    :param request: HTTP request
    :return: HTTP response
    """
    Lesson.objects.get(id=lesson_id).delete()
    return redirect('lessons:lessons')
