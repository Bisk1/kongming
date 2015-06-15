from django.conf.urls import patterns, url

from . import views

urlpatterns = patterns('',
    url(r'^lessons_management/$', views.lessons_management, name='lessons_management'),
    url(r'^delete_lesson/(?P<lesson_id>\d+)/$', views.delete_lesson, name='delete_lesson'),
    url(r'^modify_lesson/(?P<lesson_id>\d+)/$', views.modify_lesson, name='modify_lesson'),
)