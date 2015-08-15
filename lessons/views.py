import logging

from django.shortcuts import render, redirect

from lessons.forms import LessonForm
from models import Lesson
from exercises.models import Exercise, ExerciseType


logger = logging.getLogger(__name__)


def lessons(request):
    """
    Displays available lessons for modifying and adding new lessons
    :param request: HTTP request
    :return: HTTP response
    """
    all_lessons = Lesson.objects.all()
    return render(request, 'lessons/lessons.html', {'lessons': all_lessons})


def add_lesson(request):
    if request.method == 'POST':
        return handle_lesson(request)
    else:
        form = LessonForm()
        return render(request, 'lessons/lesson.html', {'form': form})


def modify_lesson(request, lesson_id):
    """
    Modifies lesson - allows to change requirement and exercises
    :param request: HTTP request
    :return: HTTP response
    """
    lesson = Lesson.objects.get(pk=lesson_id)
    if request.method == 'POST':
        return handle_lesson(request, lesson)
    else:
        form = LessonForm(instance=lesson)
        exercises = Exercise.objects.filter(lesson=lesson).order_by('number')
        exercises_types = ExerciseType.objects.all()
        return render(request, 'lessons/lesson.html', {'lesson': lesson,
                                                       'exercises': exercises,
                                                       'exercises_types': exercises_types,
                                                       'form': form,
                                                       })


def handle_lesson(request, lesson=None):
    exercises_ids=request.POST.getlist('exercises_ids')
    form = LessonForm(request.POST, instance=lesson, exercises_ids=exercises_ids)
    if form.is_valid():
        form.save()

        for exercise_id in exercises_ids:
            exercise = Exercise.objects.get(pk=exercise_id)
            exercise.number = form.cleaned_data['exercise_%s' % exercise_id]
            exercise.save()
        return redirect('lessons:lessons')
    else:
        return render(request, 'lessons/lesson.html', {'form': form})


def delete_lesson(request, lesson_id):
    """
    Delete lesson and redirect to lessons management page
    :param request: HTTP request
    :return: HTTP response
    """
    Lesson.objects.get(pk=lesson_id).delete()
    return redirect('lessons:lessons')