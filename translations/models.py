from django.db import models

from . import comparators
from translations.utils import Languages


class BusinessText(models.Model):
    """
    Text with specified language and translations
    """
    text = models.CharField(max_length=255)
    language = models.CharField(max_length=2)
    translations = models.ManyToManyField("self", symmetrical=True)

    class Meta:
        unique_together = ["text", "language"]

    def __str__(self):
        return self.language + " - " + self.text

    def __repr__(self):
        return str(self)

    def check_translation(self, proposition):
        """
        Check if the proposition is acceptable as a translation for this text
        :param proposition: translation to verify
        :return: true if this translation is acceptable
        """
        for translation in self.translations.all():
            if comparators.texts_difference(translation.text, proposition) == 0:
                return True
        return False

    def add_translation(self, translation_text):
        translation_language = Languages.other_language(Languages(self.language))
        business_translation, _ = BusinessText.objects.get_or_create(text=translation_text,
                                                                     language=translation_language.value)
        self.translations.add(business_translation)
