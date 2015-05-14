from django.contrib import admin

from models import SentenceZH, SentencePL, \
    Lesson, LessonAction, ExerciseAction, Exercise, WordZHExercise, WordPLExercise, \
    SentenceZHExercise, SentencePLExercise, ExplanationImageExercise, ExplanationExercise
from users.models import WordSkill


class LessonAdmin(admin.ModelAdmin):
    list_display = ('topic', 'level')


class ExerciseAdmin(admin.ModelAdmin):
    list_display = ('id', 'lesson', 'type', 'number')


class WordPLExerciseDetailsAdmin(admin.ModelAdmin):
    list_display = ('id', 'exercise', 'word')


admin.site.register(SentenceZH)
admin.site.register(SentencePL)
admin.site.register(Lesson)
admin.site.register(LessonAction)
admin.site.register(WordSkill)
admin.site.register(ExerciseAction)
admin.site.register(Exercise, ExerciseAdmin)
admin.site.register(WordZHExercise)
admin.site.register(WordPLExercise, WordPLExerciseDetailsAdmin)
admin.site.register(SentenceZHExercise)
admin.site.register(SentencePLExercise)
admin.site.register(ExplanationExercise)
admin.site.register(ExplanationImageExercise)