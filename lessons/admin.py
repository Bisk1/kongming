from django.contrib import admin

from models import Lesson
from users.models import WordSkill


class LessonAdmin(admin.ModelAdmin):
    list_display = ('topic', 'level')


admin.site.register(Lesson)
admin.site.register(WordSkill)