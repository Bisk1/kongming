from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()


urlpatterns = patterns('',
    url(r'^', include('menu.urls', namespace='menu')),
    url(r'^translations/', include('translations.urls', namespace='translations')),
    url(r'^learn/', include('learn.urls', namespace='learn')),
    url(r'^users/', include('users.urls', namespace='users')),
    url(r'^lessons/', include('lessons.urls', namespace='lessons')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^i18n/', include('django.conf.urls.i18n')),
)