from django.conf.urls import patterns, url, include

from . import views

urlpatterns = patterns('',
    url(r'^$', views.lessons, name='lessons'),
    url(r'^add$', views.add_lesson, name='add_lesson'),
    url(r'^(?P<lesson_id>\d+)/modify$', views.modify_lesson, name='modify_lesson'),
    url(r'^(?P<lesson_id>\d+)/delete/$', views.delete_lesson, name='delete_lesson'),

    url(r'^(?P<lesson_id>\d+)/exercises/', include('exercises.urls', namespace='exercises')),
)