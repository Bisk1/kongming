from django.contrib import admin

from models import Exercise, WordZHExercise, WordPLExercise, \
    SentenceZHExercise, SentencePLExercise, ExplanationExercise, ExerciseType




class LessonAdmin(admin.ModelAdmin):
    list_display = ('topic', 'level')


class ExerciseAdmin(admin.ModelAdmin):
    list_display = ('id', 'lesson', 'number')


class WordPLExerciseDetailsAdmin(admin.ModelAdmin):
    list_display = ('id', 'word')


admin.site.register(Exercise, ExerciseAdmin)
admin.site.register(WordZHExercise)
admin.site.register(WordPLExercise, WordPLExerciseDetailsAdmin)
admin.site.register(SentenceZHExercise)
admin.site.register(SentencePLExercise)
admin.site.register(ExplanationExercise)
admin.site.register(ExerciseType)