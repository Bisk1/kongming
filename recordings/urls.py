from django.conf.urls import patterns, url, include

from django.contrib.auth.decorators import login_required
from . import views

urlpatterns = patterns('',
    url(r'^$', login_required(views.RecordingsView.as_view()), name='recordings'),
    url(r'^(?P<pk>\d+)/modify/$', login_required(views.ModifyRecordingView.as_view()), name='modify_recording'),
    url(r'^(?P<pk>\d+)/delete/$', login_required(views.DeleteRecordingView.as_view()), name='delete_recording'),
)