from django.conf.urls import include, patterns, url

from . import views

urlpatterns = patterns('',
    url(r'^words_translations/(?P<source_language>\w+)/$', views.words_translations, name='words_translations'),
    url(r'^texts_translations/(?P<source_language>\w+)/$', views.texts_translations, name='texts_translations'),
    url(r'^texts_translations_service/$', views.texts_translations_service, name='texts_translations_service'),
)