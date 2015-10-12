from django.conf.urls import patterns, url, include

from . import views

urlpatterns = patterns('',
    url(r'^$', views.LessonListView.as_view(), name='lessons'),
    url(r'^add/$', views.CreateLessonView.as_view(), name='add_lesson'),
    url(r'^(?P<lesson_id>\d+)/modify/$', views.ModifyLessonView.as_view(), name='modify_lesson'),
    url(r'^(?P<lesson_id>\d+)/delete/$', views.DeleteLessonView.as_view(), name='delete_lesson'),

    url(r'^(?P<lesson_id>\d+)/exercises/', include('exercises.urls', namespace='exercises')),
)