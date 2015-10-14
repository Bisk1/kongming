from django.contrib import admin

from words.models import WordEN, WordZH


class WordZHAdmin(admin.ModelAdmin):
    list_display = ('word', 'pinyin')


admin.site.register(WordEN)
admin.site.register(WordZH, WordZHAdmin)