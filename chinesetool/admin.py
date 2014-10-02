from django.contrib import admin

from chinesetool.models import WordPL, WordZH, WordTranslation, Subscription, WordSkills, SentenceZH, SentencePL, \
    SentenceTranslation, Lesson, ExerciseAction, ExerciseType


admin.site.register(WordPL)
admin.site.register(WordZH)
admin.site.register(WordTranslation)
admin.site.register(SentenceZH)
admin.site.register(SentencePL)
admin.site.register(SentenceTranslation)
admin.site.register(Lesson)
admin.site.register(Subscription)
admin.site.register(WordSkills)
admin.site.register(ExerciseAction)
admin.site.register(ExerciseType)