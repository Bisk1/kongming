from django.conf.urls import patterns, url

from django.contrib.auth.decorators import login_required

from . import views

urlpatterns = patterns('',
    url(r'^(?P<lesson_id>\d+)/$', login_required(views.LearnView.as_view()), name='learn'),
    url(r'^lessons_map/$', login_required(views.LessonMapView.as_view()), name='lessons_map'),
)