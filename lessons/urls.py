from django.conf.urls import patterns, url, include

from django.contrib.auth.decorators import login_required
from . import views

urlpatterns = patterns('',
    url(r'^$', login_required(views.LessonListView.as_view()), name='lessons'),
    url(r'^add/$', login_required(views.CreateLessonView.as_view()), name='add_lesson'),
    url(r'^(?P<lesson_id>\d+)/modify/$', login_required(views.ModifyLessonView.as_view()), name='modify_lesson'),
    url(r'^(?P<lesson_id>\d+)/delete/$', login_required(views.DeleteLessonView.as_view()), name='delete_lesson'),

    url(r'^(?P<lesson_id>\d+)/exercises/', include('exercises.urls', namespace='exercises')),
)