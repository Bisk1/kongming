from translations.models import BusinessText
from translations.utils import Languages
from words.models import WordEN
from words.models import WordZH


class WordsTranslationsService():

    def set_word_translations(self, source_word_text, source_word_model, translations, pinyins):
        """
        Set translations of the source word in source language to the specified translations
        :param source_word_text: text of the word to translate
        :param source_word_model: language-specific model of the source word
        :param translations: translations of the word to translate
        """
        source_word, _ = source_word_model.objects.get_or_create(word=source_word_text) # TODO: user should specify pinyin of source word?
        source_word.get_translations().clear()
        if source_word_model == WordEN:
            for (translation, pinyin) in zip(translations, pinyins):
                new_word_zh, _ = WordZH.objects.get_or_create(word=translation, pinyin=pinyin)
                source_word.wordzh_set.add(new_word_zh)
        else:
            for translation in translations:
                result = WordEN.objects.get_or_create(word=translation)
                new_word_en, _ = result
                source_word.worden_set.add(new_word_en)
        return

    def get_word_matches(self, source_word, source_word_model):
        """
        Get words that start with the specified source word in specified language
        :param source_word: word that matches should start with
        :param source_word_model: language-specific model of the source word
        :return: matching words
        """
        matching_words = source_word_model.objects.filter(word__startswith=source_word)[:5].values_list('word', flat=True)
        return list(matching_words)

    def get_word_translations(self, source_word, source_word_model):
        """
        Get translations of the specified word in specified language
        :param source_word: word to translate
        :param source_word_model: language-specific model of the source word
        :return: translations
        """
        word_to_translate = source_word_model.objects.get(word=source_word)
        translations = word_to_translate.get_translations().order_by('pk').values('word')
        return [translation['word'] for translation in translations]


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
        :return: matching texts
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
        translations = business_text_to_translate.translations.order_by('pk').values('text')
        return [translation['text'] for translation in translations]


