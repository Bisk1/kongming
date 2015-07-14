from django.conf.urls import include, patterns, url

from . import views

urlpatterns = patterns('',
    url(r'^lesson/(?P<lesson_id>\d+)/exercise/$', views.add_exercise, name='add_exercise'),
    url(r'^lesson/(?P<lesson_id>\d+)/exercise/(?P<exercise_id>\d+)/$', views.modify_exercise, name='modify_exercise'),
    url(r'^lesson/(?P<lesson_id>\d+)/exercise/(?P<exercise_id>\d+)/delete/$', views.delete_exercise, name='delete_exercise'),

    url(r'^lesson/(?P<lesson_id>\d+)/word-zh-exercise/$', views.add_word_zh_exercise_, name='add_word-zh'),
    url(r'^lesson/(?P<lesson_id>\d+)/word-zh-exercise/(?P<exercise_id>\d+)/$', views.modify_word_zh_exercise, name='modify_word-zh'),

    url(r'^lesson/(?P<lesson_id>\d+)/word-pl-exercise/$', views.add_word_pl_exercise, name='add_word-pl'),
    url(r'^lesson/(?P<lesson_id>\d+)/word-pl-exercise/(?P<exercise_id>\d+)/$', views.modify_word_pl_exercise, name='modify_word-pl'),

    url(r'^lesson/(?P<lesson_id>\d+)/sentence_zh-exercise/$', views.add_sentence_zh_exercise, name='add_sentence-zh'),
    url(r'^lesson/(?P<lesson_id>\d+)/sentence_zh-exercise/(?P<exercise_id>\d+)/$', views.modify_sentence_zh_exercise, name='modify_sentence-zh'),

    url(r'^lesson/(?P<lesson_id>\d+)/sentence-pl-exercise/$', views.add_sentence_pl_exercise, name='add_sentence-pl'),
    url(r'^lesson/(?P<lesson_id>\d+)/sentence-pl-exercise/(?P<exercise_id>\d+)/$', views.modify_sentence_pl_exercise, name='modify_sentence-pl'),

    url(r'^lesson/(?P<lesson_id>\d+)/explanation-exercise/$', views.add_explanation_exercise, name='add_explanation'),
    url(r'^lesson/(?P<lesson_id>\d+)/explanation-exercise/(?P<exercise_id>\d+)/$', views.modify_explanation_exercise, name='modify_explanation'),


)