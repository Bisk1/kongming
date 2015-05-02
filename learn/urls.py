from django.conf.urls import include, patterns, url

from . import views

urlpatterns = patterns('',
    url(r'^learn/(?P<lesson_id>\d+)/$', views.learn, name='learn'),
    url(r'^lessons_map/$', views.lessons_map, name='lessons_map'),
)