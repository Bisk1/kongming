from translations.models import BusinessText
from translations.utils import Languages


class TextsTranslationsService():

    def set_text_translations(self, source_text, source_language, translations):
        """
        Set translations of the source text in source language to the specified translations
        :param source_text: text to translate
        :param source_language: language of text to translate
        :param translations: translations of the text to translate
        :return: nothing
        """
        business_text_to_translate, _ = BusinessText.objects.get_or_create(text=source_text, language=source_language.value)
        business_text_to_translate.translations.clear()
        for translation in translations:
            translation_language = Languages.other_language(source_language)
            business_translation, _ = BusinessText.objects.get_or_create(text=translation, language=translation_language.value)
            business_text_to_translate.translations.add(business_translation)
        return

    def get_text_matches(self, source_text, source_language):
        """
        Get texts that start with the specified source text in specified language
        :param source_text: text that matches should start with
        :param source_language: languages of the matches
        :return: matching tests
        """
        matching_business_texts = BusinessText.objects.filter(text__startswith=source_text, language=source_language.value)
        matching_texts = matching_business_texts[:5].values('text')
        return [text['text'] for text in matching_texts]

    def get_text_translations(self, source_text, source_language):
        """
        Get translations of the specified text in specified language
        :param source_text: text to translate
        :param source_language: language of the text to translate
        :return: translations
        """
        business_text_to_translate = BusinessText.objects.get(text=source_text, language=source_language.value)
        translations = business_text_to_translate.translations.values('text')
        return [translation['text'] for translation in translations]