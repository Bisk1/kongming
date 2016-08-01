from django.conf.urls import patterns, url, include

from django.contrib.auth.decorators import login_required
from . import views

urlpatterns = patterns('',
    url(r'^$', login_required(views.PlaceholdersView.as_view()), name='placeholders'),
    url(r'^create$', login_required(views.CreatePlaceholderView.as_view()), name='create_placeholder'),
)