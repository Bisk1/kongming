from django.contrib import admin

from words.models import WordPL, WordZH


class WordZHAdmin(admin.ModelAdmin):
    list_display = ('word', 'pinyin')


admin.site.register(WordPL)
admin.site.register(WordZH, WordZHAdmin)