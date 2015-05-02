from django.conf.urls import include, patterns, url

from . import views

urlpatterns = patterns('',
    url(r'^words_translations_management/(?P<source_language>\w+)/$', views.words_translations_management, name='words_translations_management'),
    url(r'^dictionary/(?P<source_language>\w+)/$', views.dictionary, name='dictionary'),
)