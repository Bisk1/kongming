from django.conf.urls import include, patterns, url

from . import views

urlpatterns = patterns('',
    url(r'^words_translations/(?P<source_language>\w+)/$', views.words_translations, name='words_translations'),
    url(r'^sentences_translations/(?P<source_language>\w+)/$', views.sentences_translations, name='sentences_translations'),
    url(r'^dictionary/(?P<source_language>\w+)/$', views.dictionary, name='dictionary'),
)