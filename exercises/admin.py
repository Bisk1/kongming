from django.contrib import admin

from exercises.models import Exercise, Typing, Explanation, Choice, Listening


class ExerciseAdmin(admin.ModelAdmin):
    list_display = ('id', 'lesson', 'number')

class ExplanationAdmin(admin.ModelAdmin):
    list_display = ('id', 'text')

admin.site.register(Exercise, ExerciseAdmin)
admin.site.register(Typing)
admin.site.register(Explanation, ExplanationAdmin)
admin.site.register(Listening)
admin.site.register(Choice)