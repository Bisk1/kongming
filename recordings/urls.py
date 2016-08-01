from django.conf.urls import patterns, url, include

from django.contrib.auth.decorators import login_required
from . import views

urlpatterns = patterns('',
    url(r'^$', login_required(views.RecordingsView.as_view()), name='recordings'),
    url(r'^create$', login_required(views.CreatePlaceholderView.as_view()), name='create_placeholder'),
)