from django.conf.urls import patterns, url

from . import views

urlpatterns = patterns('',
    url(r'^(?P<exercise_type>\w+)$', views.add_exercise, name='add_exercise'),
    url(r'^(?P<exercise_id>\d+)/$', views.modify_exercise, name='modify_exercise'),
    url(r'^(?P<exercise_id>\d+)/delete/$', views.delete_exercise, name='delete_exercise'),
)