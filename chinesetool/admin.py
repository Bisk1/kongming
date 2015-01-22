from django.contrib import admin

from chinesetool.models import WordPL, WordZH, WordTranslation, Subscription, WordSkill, SentenceZH, SentencePL, \
    SentenceTranslation, Lesson, ExerciseAction, Exercise, WordZHExercise, WordPLExercise, \
    SentenceZHExercise, SentencePLExercise, LANGUAGE_CHOICES


class WordTranslationAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Chinese word',               {'fields': ['word_zh']}),
        ('Polish word', {'fields': ['word_pl']}),
    ]
    list_display = ('word_zh', 'word_pl')


class SentenceTranslationAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Chinese sentence',               {'fields': ['sentence_zh']}),
        ('Polish sentence', {'fields': ['sentence_pl']}),
    ]
    list_display = ('sentence_zh', 'sentence_pl')


class WordZHAdmin(admin.ModelAdmin):
    list_display = ('word', 'pinyin')


class LessonAdmin(admin.ModelAdmin):
    list_display = ('topic', 'level')


class ExerciseAdmin(admin.ModelAdmin):
    list_display = ('id', 'lesson', 'type', 'number')


class WordPLExerciseDetailsAdmin(admin.ModelAdmin):
    list_display = ('id', 'exercise', 'word')


admin.site.register(WordPL)
admin.site.register(WordZH, WordZHAdmin)
admin.site.register(WordTranslation, WordTranslationAdmin)
admin.site.register(SentenceZH)
admin.site.register(SentencePL)
admin.site.register(SentenceTranslation, SentenceTranslationAdmin)
admin.site.register(Lesson)
admin.site.register(Subscription)
admin.site.register(WordSkill)
admin.site.register(ExerciseAction)
admin.site.register(Exercise, ExerciseAdmin)
admin.site.register(WordZHExercise)
admin.site.register(WordPLExercise, WordPLExerciseDetailsAdmin)
admin.site.register(SentenceZHExercise)
admin.site.register(SentencePLExercise)