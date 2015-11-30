# coding=utf-8
from unittest import skip

from django.test import TestCase
from words.models import WordZH, WordEN
from words import translator
from translations.utils import Languages


class WordTranslationTest(TestCase):

    def test_english_word_exists_with_one_translation(self):
        """
        exists should return true for translation if it exists as the only one
        """
        hao = WordZH.objects.create(word="好")
        good = WordEN.objects.create(word="good")
        hao.worden_set.add(good)

        good = WordEN.objects.get(word="good")
        chinese_translations_of_good = [word.word for word in good.wordzh_set.all()]
        self.assertCountEqual(chinese_translations_of_good, ["好"])

        hao = WordZH.objects.get(word="好")
        english_translations_of_hao = [word.word for word in hao.worden_set.all()]
        self.assertCountEqual(english_translations_of_hao, ["good"])

    def test_exists_with_many_translation(self):
        """
        exists should return true for translation if it exists as one of many
        """
        hao = WordZH.objects.create(word="好")
        hen = WordZH.objects.create(word="很")
        good = WordEN.objects.create(word="good")
        very = WordEN.objects.create(word="very")

        hao.worden_set.add(good)
        hao.worden_set.add(very)
        hen.worden_set.add(very)

        good = WordEN.objects.get(word="good")
        chinese_translations_of_good = [word.word for word in good.wordzh_set.all()]
        self.assertCountEqual(chinese_translations_of_good, ["好"])

        very = WordEN.objects.get(word="very")
        chinese_translations_of_very = [word.word for word in very.wordzh_set.all()]
        self.assertCountEqual(chinese_translations_of_very, ["好", "很"])

        hao = WordZH.objects.get(word="好")
        english_translations_of_hao = [word.word for word in hao.worden_set.all()]
        self.assertCountEqual(english_translations_of_hao, ["good", "very"])

        hen = WordZH.objects.get(word="很")
        english_translations_of_hen = [word.word for word in hen.worden_set.all()]
        self.assertCountEqual(english_translations_of_hen, ["very"])

    def test_exists_with_no_translation(self):
        """
        exists should return false for translation if there is no translation including these words
        """
        WordZH.objects.create(word="好")
        WordEN.objects.create(word="good")

        good = WordEN.objects.get(word="good")
        chinese_translations_of_good = good.wordzh_set.all()
        self.assertEqual(len(chinese_translations_of_good), 0)

        chinese_word_list = WordZH.objects.filter(word="好")
        self.assertEqual(len(chinese_word_list), 1)
        english_translations1 = chinese_word_list[0].worden_set
        self.assertEqual(len(english_translations1.all()), 0)

    def test_exists_with_no_words(self):
        """
        exists should return false for translation if there is no words specified in the database
        """
        money_matches = WordEN.objects.filter(word="money")
        self.assertEqual(len(money_matches), 0)

        shui_matches = WordZH.objects.filter(word="水")
        self.assertEqual(len(shui_matches), 0)


@skip("Translator violates Google terms, need to find other solution")
class TranslatorTest(TestCase):

    def test_can_translate_chinese_word_with_google(self):
        text_zh = '狗'
        text_en = translator.translate(text_zh, Languages.chinese)
        self.assertEqual(text_en, 'dog')

    def test_can_translate_english_word_with_google(self):
        text_en = 'ass'
        text_zh = translator.translate(text_en, Languages.english)
        self.assertEqual(text_zh, '屁股')

    def test_can_translate_chinese_word_with_db(self):
        word_zh = WordZH(word='some_word_zh', pinyin='some_word_zh_pinyin')
        word_zh.save()
        word_zh.worden_set.create(word='some_word_en')
        word_en = translator.translate('some_word_zh', Languages.chinese)
        self.assertEqual(word_en, 'some_word_en')

    def test_can_translate_english_word_with_db(self):
        word_en = WordEN(word='test_word_en')
        word_en.save()
        word_en.wordzh_set.create(word='test_word_zh', pinyin='test_word_zh_pinyin')
        word_zh = translator.translate('test_word_en', Languages.english)
        self.assertEqual(word_zh, 'test_word_zh')