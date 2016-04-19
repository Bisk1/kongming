from django.contrib import admin

from recordings.models import Recording


class RecordingAdmin(admin.ModelAdmin):
    list_display = ('text', 'url')

admin.site.register(Recording, RecordingAdmin)