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

)