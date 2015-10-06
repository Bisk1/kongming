from django.conf.urls import patterns, include, url
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^', include('menu.urls', namespace='menu')),
    url(r'^translations/', include('translations.urls', namespace='translations')),
    url(r'^learn/', include('learn.urls', namespace='learn')),
    url(r'^users/', include('users.urls', namespace='users')),
    url(r'^lessons/', include('lessons.urls', namespace='lessons')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^redactor/', include('redactor.urls')),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
