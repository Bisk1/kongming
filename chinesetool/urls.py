from django.conf.urls import include, patterns, url

from chinesetool.views import menu
from chinesetool.views import modify_lesson

urlpatterns = patterns('',
    url(r'^$', menu.index, name='index'),
    url(r'^learn/(?P<lesson_id>\d+)/$', menu.learn, name='learn'),
    url(r'login/$', 'django.contrib.auth.views.login', name='login'),
    url(r'^logout/$', menu.logout_page, name='logout'),
    url(r'^register/$', menu.register_page, name='register'),
    url(r'^dictionary/(?P<source_language>\w+)/$', menu.dictionary, name='dictionary'),
    url(r'^choose_language/$', menu.choose_language, name='choose_language'),
    url(r'^delete_lesson/(?P<lesson_id>\d+)/$', modify_lesson.delete_lesson, name='delete_lesson'),
    url(r'^modify_lesson/(?P<lesson_id>\d+)/$', modify_lesson.modify_lesson, name='modify_lesson'),
    url(r'^modify_lesson/(?P<lesson_id>\d+)/add_requirement/$', modify_lesson.add_requirement, name='add_requirement'),
    url(r'^modify_lesson/(?P<lesson_id>\d+)/add_exercise_word_zh/$', modify_lesson.add_exercise_word_zh, name='add_exercise_word_zh'),
    url(r'^modify_lesson/(?P<lesson_id>\d+)/add_exercise_word_pl/$', modify_lesson.add_exercise_word_pl, name='add_exercise_word_pl'),
    url(r'^modify_lesson/(?P<lesson_id>\d+)/add_exercise_sentence_zh/$', modify_lesson.add_exercise_sentence_zh, name='add_exercise_sentence_zh'),
    url(r'^modify_lesson/(?P<lesson_id>\d+)/add_exercise_sentence_pl/$', modify_lesson.add_exercise_sentence_pl, name='add_exercise_sentence_pl'),
    url(r'^modify_lesson/(?P<lesson_id>\d+)/add_exercise_explanation/$', modify_lesson.add_exercise_explanation, name='add_exercise_explanation'),
    url(r'^modify_lesson/(?P<lesson_id>\d+)/add_exercise_explanation_image/$', modify_lesson.add_exercise_explanation_image, name='add_exercise_explanation_image'),
    url(r'lessons_map/$', menu.lessons_map, name='lessons_map'),
    url(r'lessons_management/$', menu.lessons_management, name='lessons_management'),
    url(r'^i18n/', include('django.conf.urls.i18n')),
)