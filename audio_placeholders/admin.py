from django.contrib import admin

from audio_placeholders.models import AudioPlaceholder


class AudioPlaceholderAdmin(admin.ModelAdmin):
    list_display = ('text',)

admin.site.register(AudioPlaceholder, AudioPlaceholderAdmin)