import json
from lessons.models import Lesson
from learn.models import LessonAction, Status

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
    current_level = Lesson.objects.filter(requirement=None).order_by('pk')  # first level - no requirements
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
                                         'status': determine_lesson_status_for_user(lesson, user)})
        else:
            lessons_levels_dicts.append({'pk': lesson.pk, 'topic': lesson.topic, 'requirement': lesson.requirement.pk,
                                         'status': determine_lesson_status_for_user(lesson, user)})
    return lessons_levels_dicts


def determine_lesson_status_for_user(lesson, user):
    lesson_actions = LessonAction.objects.filter(lesson=lesson, user=user)
    if lesson_actions.filter(status=Status.success.value).count() > 0:
        return Status.success.value
    elif lesson_actions.filter(status=Status.failure.value).count() > 0:
        return Status.failure.value
    else:
        return Status.not_done.value
