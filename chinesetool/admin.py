from django.contrib import admin

from chinesetool.models import WordPL, WordZH, WordTranslation, Subscription, WordSkill, SentenceZH, SentencePL, \
    SentenceTranslation, Lesson, ExerciseAction, ExerciseType


class WordTranslationAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Chinese word',               {'fields': ['word_zh']}),
        ('Polish word', {'fields': ['word_pl']}),
    ]
    list_display = ('word_zh', 'word_pl')


class WordZHAdmin(admin.ModelAdmin):
    list_display = ('word', 'pinyin')


admin.site.register(WordPL)
admin.site.register(WordZH, WordZHAdmin)
admin.site.register(WordTranslation, WordTranslationAdmin)
admin.site.register(SentenceZH)
admin.site.register(SentencePL)
admin.site.register(SentenceTranslation)
admin.site.register(Lesson)
admin.site.register(Subscription)
admin.site.register(WordSkill)
admin.site.register(ExerciseAction)
admin.site.register(ExerciseType)