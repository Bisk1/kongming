from django.conf.urls import patterns, url

from . import views

urlpatterns = patterns('',
    url(r'^$', views.add_exercise, name='add_exercise'),
    url(r'^(?P<exercise_id>\d+)/$', views.modify_exercise, name='modify_exercise'),
    url(r'^(?P<exercise_id>\d+)/delete/$', views.delete_exercise, name='delete_exercise'),

    url(r'^typing/$', views.add_typing, name='add_typing'),
    url(r'^typing/(?P<exercise_id>\d+)/$', views.modify_typing, name='modify_typing'),

    url(r'^explanation/$', views.add_explanation_exercise, name='add_explanation'),
    url(r'^explanation/(?P<exercise_id>\d+)/$', views.modify_explanation_exercise, name='modify_explanation'),

    url(r'^choice/$', views.add_choice_exercise, name='add_choice'),
    url(r'^choice/(?P<exercise_id>\d+)/$', views.modify_choice_exercise, name='modify_choice'),

    url(r'^listening/$', views.add_listening_exercise, name='add_listening'),
    url(r'^listening/(?P<exercise_id>\d+)/$', views.modify_listening_exercise, name='modify_listening'),

)