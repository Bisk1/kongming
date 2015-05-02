from django.conf.urls import include, patterns, url

from . import views

urlpatterns = patterns('',
    url(r'lessons_management/$', views.lessons_management, name='lessons_management'),
    url(r'modify_lesson/(?P<lesson_id>\d+)/get_exercises/$', views.display_exercises, name='display_exercises'),
    url(r'^delete_lesson/(?P<lesson_id>\d+)/$', views.delete_lesson, name='delete_lesson'),
    url(r'^modify_lesson/(?P<lesson_id>\d+)/$', views.modify_lesson, name='modify_lesson'),
    url(r'^modify_lesson/(?P<lesson_id>\d+)/add_requirement/$', views.add_requirement, name='add_requirement'),
    url(r'^modify_lesson/(?P<lesson_id>\d+)/add_exercise_word_zh/$', views.add_exercise_word_zh, name='add_exercise_word_zh'),
    url(r'^modify_lesson/(?P<lesson_id>\d+)/add_exercise_word_pl/$', views.add_exercise_word_pl, name='add_exercise_word_pl'),
    url(r'^modify_lesson/(?P<lesson_id>\d+)/add_exercise_sentence_zh/$', views.add_exercise_sentence_zh, name='add_exercise_sentence_zh'),
    url(r'^modify_lesson/(?P<lesson_id>\d+)/add_exercise_sentence_pl/$', views.add_exercise_sentence_pl, name='add_exercise_sentence_pl'),
    url(r'^modify_lesson/(?P<lesson_id>\d+)/add_exercise_explanation/$', views.add_exercise_explanation, name='add_exercise_explanation'),
    url(r'^modify_lesson/(?P<lesson_id>\d+)/add_exercise_explanation_image/$', views.add_exercise_explanation_image, name='add_exercise_explanation_image'),
)