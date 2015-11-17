from django.db import models
from . import comparators
from translations.utils import Languages
from words.models import to_word_model, WordEN, WordZH


class BusinessText(models.Model):
    """
    Text with specified language and translations
    """
    text = models.CharField(max_length=255)
    language = models.CharField(max_length=2)
    translations = models.ManyToManyField("self", symmetrical=True)
    words_en = models.ManyToManyField(WordEN)
    words_zh = models.ManyToManyField(WordZH)

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

    def get_words(self):
        if self.language == Languages.chinese.value:
            return self.words_zh
        elif self.language == Languages.english.value:
            return self.words_en
        else:
            raise Exception("Unknown language: " + self.language)

    def auto_tokenize(self):
        """
        Tokenize the business text into words, create their objects
        if necessary and link the business text to them
        """
        tokens = Languages.tokenize(self.language, self.text)
        word_model = to_word_model(self.language)
        self.get_words().clear()
        for token in tokens:
            word_object = word_model.get_or_create_with_google(word=token)[0]
            self.get_words().add(word_object)

    @classmethod
    def get_or_create_and_auto_tokenize(cls, *args, **kwargs):
        """
        Same as get_or_create, but if created, tokenize the text
        :return: tuple (object, created)
        """
        object, created = BusinessText.objects.get_or_create(*args, **kwargs)
        if created:
            object.auto_tokenize()
        return object, created
