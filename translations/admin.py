from django.contrib import admin

from models import WordPL, WordZH, WordTranslation, SentenceTranslation, SentencePL, SentenceZH


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


admin.site.register(WordPL)
admin.site.register(WordZH, WordZHAdmin)
admin.site.register(WordTranslation, WordTranslationAdmin)
admin.site.register(SentenceTranslation, SentenceTranslationAdmin)
admin.site.register(SentencePL)
admin.site.register(SentenceZH)