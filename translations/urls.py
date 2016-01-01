from django.conf.urls import patterns, url

from django.contrib.auth.decorators import login_required
from . import views

urlpatterns = patterns('',
    url(r'^words_translations/$', login_required(views.WordsTranslationsView.as_view()), name='words_translations'),
    url(r'^words_translations_api/$', login_required(views.WordsTranslationsApiView.as_view()), name='words_translations_api'),
    url(r'^texts_translations/$', login_required(views.TextsTranslationsView.as_view()), name='texts_translations'),
    url(r'^texts_translations_api/$', login_required(views.TextsTranslationsApiView.as_view()), name='texts_translations_api'),
)