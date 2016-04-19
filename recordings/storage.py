import os
from django.utils.module_loading import import_string

from recordings.models import Recording
from django.conf import settings

base_storage_class_name = settings.BASE_DEFAULT_FILE_STORAGE
base_storage_class = import_string(base_storage_class_name)


class TrackingStorage(base_storage_class):
    """
    TrackingStorage is a wrapper for any DEFAULT_FILE_STORAGE
    that will keep track of all audio being saved
    and add them to the Recordings database.
    """

    def save(self, name, content, max_length=None):
        if self._is_audio(name):
            real_path = super().save(name, content, max_length)
            text = self._strip_extension(content.name)
            Recording(text=text, url=self.url(real_path)).save()
            return real_path
        else:
            return super().save(name, content)

    @staticmethod
    def _is_audio(name):
        return name.endswith('.wav')

    @staticmethod
    def _strip_extension(name):
        return os.path.splitext(name)[0]
