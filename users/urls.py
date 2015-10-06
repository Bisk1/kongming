from django.conf.urls import patterns, url

from . import views

urlpatterns = patterns('',
    url(r'^login/$', views.login_my, name='login'),
    url(r'^logout/$', views.logout_page, name='logout'),
    url(r'^register/$', views.register_page, name='register'),
)