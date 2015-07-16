from django.contrib import admin

from models import WordPL, WordZH, WordTranslation, TextTranslation, TextPL, TextZH


class WordTranslationAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Chinese word',               {'fields': ['word_zh']}),
        ('Polish word', {'fields': ['word_pl']}),
    ]
    list_display = ('word_zh', 'word_pl')


class TextTranslationAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Chinese sentence', {'fields': ['text_zh']}),
        ('Polish sentence', {'fields': ['text_pl']}),
    ]
    list_display = ('text_zh', 'text_pl')


class WordZHAdmin(admin.ModelAdmin):
    list_display = ('word', 'pinyin')


admin.site.register(WordPL)
admin.site.register(WordZH, WordZHAdmin)
admin.site.register(WordTranslation, WordTranslationAdmin)
admin.site.register(TextTranslation, TextTranslationAdmin)
admin.site.register(TextPL)
admin.site.register(TextZH)