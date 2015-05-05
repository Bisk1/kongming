from django.conf.urls import include, patterns, url

from . import views

urlpatterns = patterns('',
    url(r'^logout/$', views.logout_page, name='logout'),
    url(r'^register/$', views.register_page, name='register'),
)