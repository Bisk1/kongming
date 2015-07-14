from django.conf.urls import include, patterns, url

from . import views

urlpatterns = patterns('',
    url(r'^add_exercise/(?P<lesson_id>\d+)/$', views.add_exercise, name='add_exercise'),
    url(r'^modify_exercise/(?P<exercise_id>\d+)/$', views.modify_exercise, name='modify_exercise'),
    url(r'^delete_exercise/(?P<exercise_id>\d+)/$', views.delete_exercise, name='delete_exercise'),

    url(r'^add_word-zh-exercise/(?P<lesson_id>\d+)/$', views.add_word_zh_exercise_, name='add_word-zh-exercise_'),
    url(r'^modify_word-zh-exercise/(?P<exercise_id>\d+)/$', views.modify_word_zh_exercise, name='modify_word-zh-exercise'),

    url(r'^add_word-pl-exercise/(?P<lesson_id>\d+)/$', views.add_word_pl_exercise, name='add_word-pl-exercise'),
    url(r'^modify_word-pl-exercise/(?P<exercise_id>\d+)/$', views.modify_word_pl_exercise, name='modify_word-pl-exercise'),

    url(r'^add_sentence_zh-exercise/(?P<lesson_id>\d+)/$', views.add_sentence_zh_exercise, name='add_sentence-zh-exercise'),
    url(r'^modify_sentence_zh-exercise/(?P<exercise_id>\d+)/$', views.modify_sentence_zh_exercise, name='modify_sentence-zh-exercise'),

    url(r'^add_sentence-pl-exercise/(?P<lesson_id>\d+)/$', views.add_sentence_pl_exercise, name='add_sentence-pl-exercise'),
    url(r'^modify_sentence-pl-exercise/(?P<exercise_id>\d+)/$', views.modify_sentence_pl_exercise, name='modify_sentence-pl-exercise'),

    url(r'^add_explanation-exercise/(?P<lesson_id>\d+)/$', views.add_explanation_exercise, name='add_explanation-exercise'),
    url(r'^modify_explanation-exercise/(?P<exercise_id>\d+)/$', views.modify_explanation_exercise, name='modify_explanation-exercise'),


)