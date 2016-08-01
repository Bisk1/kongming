from django.contrib import admin

from recordings.models import Recording


class RecordingAdmin(admin.ModelAdmin):
    list_display = ('text',)

admin.site.register(Recording, RecordingAdmin)