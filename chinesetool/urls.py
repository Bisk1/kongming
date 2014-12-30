from django.conf.urls import include, patterns, url

from chinesetool import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^learn/(?P<lesson_id>\d+)/$', views.learn, name='learn'),
    url(r'login/$', 'django.contrib.auth.views.login', name='login'),
    url(r'^logout/$', views.logout_page, name='logout'),
    url(r'^register/$', views.register_page, name='register'),
    url(r'^dictionary/(?P<source_language>\w+)/$', views.dictionary, name='dictionary'),
    url(r'^choose_language/$', views.choose_language, name='choose_language'),
    url(r'^modify_lesson/(?P<lesson_id>\d+)/$', views.modify_lesson, name='modify_lesson'),
    url(r'^modify_lesson/(?P<lesson_id>\d+)/add_requirement/$', views.add_requirement, name='add_requirement'),
    url(r'^modify_lesson/(?P<lesson_id>\d+)/add_exercise_word_zh/$', views.add_exercise_word_zh, name='add_exercise_word_zh'),
    url(r'^modify_lesson/(?P<lesson_id>\d+)/add_exercise_word_pl/$', views.add_exercise_word_pl, name='add_exercise_word_pl'),
    url(r'^modify_lesson/(?P<lesson_id>\d+)/add_exercise_sentence_zh/$', views.add_exercise_sentence_zh, name='add_exercise_sentence_zh'),
    url(r'^modify_lesson/(?P<lesson_id>\d+)/add_exercise_sentence_pl/$', views.add_exercise_sentence_pl, name='add_exercise_sentence_pl'),
    url(r'^modify_lesson/(?P<lesson_id>\d+)/add_exercise_explanation/$', views.add_exercise_explanation, name='add_exercise_explanation'),
    url(r'lessons_map/$', views.lessons_map, name='lessons_map'),
    url(r'lesson_management/$', views.lessons_management, name='lessons_management'),
    url(r'^i18n/', include('django.conf.urls.i18n')),
)