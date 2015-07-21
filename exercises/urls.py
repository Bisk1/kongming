from django.conf.urls import include, patterns, url

from . import views

urlpatterns = patterns('',
    url(r'^lesson/(?P<lesson_id>\d+)/exercise/$', views.add_exercise, name='add_exercise'),
    url(r'^lesson/(?P<lesson_id>\d+)/exercise/(?P<exercise_id>\d+)/$', views.modify_exercise, name='modify_exercise'),
    url(r'^lesson/(?P<lesson_id>\d+)/exercise/(?P<exercise_id>\d+)/delete/$', views.delete_exercise, name='delete_exercise'),

    url(r'^lesson/(?P<lesson_id>\d+)/exercise/typing/$', views.add_typing, name='add_typing'),
    url(r'^lesson/(?P<lesson_id>\d+)/exercise/typing/(?P<exercise_id>\d+)/$', views.modify_typing, name='modify_typing'),

    url(r'^lesson/(?P<lesson_id>\d+)/exercise/explanation/$', views.add_explanation_exercise, name='add_explanation'),
    url(r'^lesson/(?P<lesson_id>\d+)/exercise/explanation/(?P<exercise_id>\d+)/$', views.modify_explanation_exercise, name='modify_explanation'),


)