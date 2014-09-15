from django.conf.urls import include, patterns, url

from chinesetool import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^translate_word/$', views.translate_word, name='translate_word'),
    url(r'^translate_sentence/$', views.translate_sentence, name='translate_sentence'),
    url(r'^(?P<wordzh_id>\d+)/check_word_translation/$', views.check_word_translation, name='check_word_translation'),
    url(r'login/$', 'django.contrib.auth.views.login', name='login'),
    url(r'^logout/$', views.logout_page, name='logout'),
    url(r'^register/$', views.register_page, name='register'),
    url(r'^dictionary/$', views.dictionary, name='dictionary'),
    url(r'^choose_language/', views.choose_language, name='choose_language'),
    url(r'^i18n/', include('django.conf.urls.i18n')),

    url(r'^ajaxexample_json$',views.ajax),

)