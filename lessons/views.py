import logging

from django.shortcuts import render, redirect

from lessons.forms import LessonForm
from lessons.models import Lesson
from exercises.models import Exercise


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
        return render(request, 'lessons/lesson.html', {'lesson': lesson,
                                                       'exercises': exercises,
                                                       'form': form,
                                                       })


def handle_lesson(request, lesson=None):
    form = LessonForm(request.POST, instance=lesson)
    if form.is_valid():
        form.save()
        return redirect('lessons:modify_lesson', lesson_id=form.instance.pk)
    else:
        return render(request, 'lessons/lesson.html', {'form': form})


def delete_lesson(request, lesson_id):
    """
    Delete lesson and redirect to lessons management page.
    Lessons that have requirement = deleted lesson,
    will have requirement = requirement of deleted lesson
    :param request: HTTP request
    :return: HTTP response
    """
    lesson_to_delete = Lesson.objects.get(pk=lesson_id)
    lessons_requiring_lesson_to_delete = lesson_to_delete.lesson_set.all()
    for lesson in lessons_requiring_lesson_to_delete:
        lesson.requirement = lesson_to_delete.requirement
        lesson.save()
    lesson_to_delete.delete()
    return redirect('lessons:lessons')