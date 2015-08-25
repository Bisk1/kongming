from django.contrib import admin

from exercises.models import Exercise, Typing, Explanation


class ExerciseAdmin(admin.ModelAdmin):
    list_display = ('id', 'lesson', 'number')


admin.site.register(Exercise, ExerciseAdmin)
admin.site.register(Typing)
admin.site.register(Explanation)