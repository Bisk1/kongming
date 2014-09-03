from django.conf.urls import patterns, url

from chinesetool import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^translate_word/$', views.translate_word, name='translate_word'),
    url(r'^translate_sentence/$', views.translate_sentence, name='translate_sentence'),
    url(r'^(?P<wordzh_id>\d+)/check_word_translation/$', views.check_word_translation, name='check_word_translation'),
    (r'login/$','django.contrib.auth.views.login'),
    url(r'^logout/$', views.logout_page),

    (r'^register/$',views.register_page),
# Process a quiz guess

    url(r'^ajaxexample_json$',views.ajax),

)