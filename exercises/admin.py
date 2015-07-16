from django.contrib import admin

from models import Exercise, Typing, Explanation, ExerciseType




class LessonAdmin(admin.ModelAdmin):
    list_display = ('topic', 'level')


class ExerciseAdmin(admin.ModelAdmin):
    list_display = ('id', 'lesson', 'number')


admin.site.register(Exercise, ExerciseAdmin)
admin.site.register(Typing)
admin.site.register(Explanation)
admin.site.register(ExerciseType)