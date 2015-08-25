from django.contrib import admin

from translations.models import WordPL, WordZH, WordTranslation, BusinessText


class WordTranslationAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Chinese word',{'fields': ['word_zh']}),
        ('Polish word', {'fields': ['word_pl']}),
    ]
    list_display = ('word_zh', 'word_pl')


class WordZHAdmin(admin.ModelAdmin):
    list_display = ('word', 'pinyin')


admin.site.register(WordPL)
admin.site.register(WordZH, WordZHAdmin)
admin.site.register(WordTranslation, WordTranslationAdmin)
admin.site.register(BusinessText)