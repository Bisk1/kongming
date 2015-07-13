from django.conf.urls import include, patterns, url

from . import views

urlpatterns = patterns('',
    url(r'^add_exercise/(?P<lesson_id>\d+)/$', views.add_exercise, name='add_exercise'),
    url(r'^modify_exercise/(?P<exercise_id>\d+)/$', views.modify_exercise, name='modify_exercise'),
    url(r'^delete_exercise/(?P<exercise_id>\d+)/$', views.delete_exercise, name='delete_exercise'),

    url(r'^add_word-zh-exercise/(?P<lesson_id>\d+)/$', views.add_wordzhexercise, name='add_exercise_word_zh'),
    url(r'^modify_word-zh-exercise/(?P<exercise_id>\d+)/$', views.modify_wordzhexercise, name='modify_exercise_word_zh'),

    url(r'^add_word-pl-exercise/(?P<lesson_id>\d+)/$', views.add_wordplexercise, name='add_exercise_word_pl'),
    url(r'^modify_word-pl-exercise/(?P<exercise_id>\d+)/$', views.modify_wordplexercise, name='modify_exercise_word_pl'),

    url(r'^add_sentence_zh-exercise/(?P<lesson_id>\d+)/$', views.add_sentencezhexercise, name='add_exercise_sentence_zh'),
    url(r'^modify_sentence_zh-exercise/(?P<exercise_id>\d+)/$', views.modify_sentencezhexercise, name='modify_exercise_sentence_zh'),

    url(r'^add_sentence-pl-exercise/(?P<lesson_id>\d+)/$', views.add_sentenceplexercise, name='add_exercise_sentence_pl'),
    url(r'^modify_sentence-pl-exercise/(?P<exercise_id>\d+)/$', views.modify_sentenceplexercise, name='modify_exercise_sentence_pl'),

    url(r'^add_explanation-exercise/(?P<lesson_id>\d+)/$', views.add_explanationexercise, name='add_exercise_explanation'),
    url(r'^modify_explanation-exercise/(?P<exercise_id>\d+)/$', views.modify_explanationexercise, name='modify_exercise_explanation'),


)