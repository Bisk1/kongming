from django.conf.urls import include, patterns, url

from . import views

urlpatterns = patterns('',
    url(r'^add_exercise/(?P<lesson_id>\d+)/$', views.add_exercise, name='add_exercise'),
    url(r'^modify_exercise/(?P<exercise_id>\d+)/$', views.modify_exercise, name='modify_exercise'),
    url(r'^delete_exercise/(?P<exercise_id>\d+)/$', views.delete_exercise, name='delete_exercise'),

    url(r'^modify_exercise_word_zh/(?P<lesson_id>\d+)/$', views.modify_exercise_word_zh, name='modify_exercise_word_zh'),
    url(r'^modify_exercise_word_pl/(?P<lesson_id>\d+)/$', views.modify_exercise_word_pl, name='modify_exercise_word_pl'),
    url(r'^modify_exercise_sentence_zh/(?P<lesson_id>\d+)/$', views.modify_exercise_sentence_zh, name='modify_exercise_sentence_zh'),
    url(r'^modify_exercise_sentence_pl/(?P<lesson_id>\d+)/$', views.modify_exercise_sentence_pl, name='modify_exercise_sentence_pl'),
    url(r'^modify_exercise_explanation/(?P<lesson_id>\d+)/$', views.modify_exercise_explanation, name='modify_exercise_explanation'),
    url(r'^modify_exercise_explanation_image/(?P<lesson_id>\d+)/$', views.modify_exercise_explanation_image, name='modify_exercise_explanation_image'),

)