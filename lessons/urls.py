from django.conf.urls import patterns, url

from . import views

urlpatterns = patterns('',
    url(r'^lessons/$', views.lessons, name='lessons'),
    url(r'^lesson/(?P<lesson_id>\d+)/$', views.modify_lesson, name='modify_lesson'),
    url(r'^lesson/(?P<lesson_id>\d+)/delete/$', views.delete_lesson, name='delete_lesson'),
)