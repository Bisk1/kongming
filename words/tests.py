# coding=utf-8

from django.test import TestCase
from words.models import WordZH, WordEN
from words import translator
from translations.utils import Languages


class WordTranslationTest(TestCase):

    def test_english_word_exists_with_one_translation(self):
        """
        exists should return true for translation if it exists as the only one
        """
        word_zh = WordZH.objects.create(word="好")
        word_en = WordEN.objects.create(word="good")
        word_zh.WordEN_set.add(word_en)

        english_word_list = WordEN.objects.filter(word="good")
        self.assertEqual(len(english_word_list), 1)
        chinese_translations = english_word_list[0].wordzh_set
        self.assertEqual(len(chinese_translations.all()), 1)
        self.assertEqual(chinese_translations.all()[0].word, "好")

        chinese_word_list = WordZH.objects.filter(word="好")
        self.assertTrue(len(chinese_word_list) == 1)
        english_translations = chinese_word_list[0].WordEN_set
        self.assertEqual(len(english_translations.all()), 1)
        self.assertEqual(english_translations.all()[0].word, "good")

    def test_exists_with_many_translation(self):
        """
        exists should return true for translation if it exists as one of many
        """
        word_zh1 = WordZH.objects.create(word="好")
        word_zh2 = WordZH.objects.create(word="很")
        word_en1 = WordEN.objects.create(word="good")
        word_en2 = WordEN.objects.create(word="very")

        word_zh1.WordEN_set.add(word_en1)
        word_zh1.WordEN_set.add(word_en2)
        word_zh2.WordEN_set.add(word_en2)

        english_word_list1 = WordEN.objects.filter(word="good")
        self.assertEqual(len(english_word_list1), 1)
        chinese_translations1 = english_word_list1[0].wordzh_set
        self.assertEqual(len(chinese_translations1.all()), 1)
        self.assertEqual(chinese_translations1.all()[0].word, "好")

        english_word_list2 = WordEN.objects.filter(word="very")
        self.assertEqual(len(english_word_list2), 1)
        chinese_translations2 = english_word_list2[0].wordzh_set
        self.assertEqual(len(chinese_translations2.all()), 2)
        self.assertIn(chinese_translations2.all()[0].word, ["好", "很"])
        self.assertIn(chinese_translations2.all()[1].word, ["好", "很"])
        self.assertNotEqual(chinese_translations2.all()[0].word, chinese_translations2.all()[1].word)

        chinese_word_list1 = WordZH.objects.filter(word="好")
        self.assertEqual(len(chinese_word_list1), 1)
        english_translations1 = chinese_word_list1[0].WordEN_set
        self.assertEqual(len(english_translations1.all()), 2)
        self.assertIn(english_translations1.all()[0].word, ["good", "very"])
        self.assertIn(english_translations1.all()[1].word, ["good", "very"])
        self.assertNotEqual(english_translations1.all()[0].word, english_translations1.all()[1].word)

        chinese_word_list2 = WordZH.objects.filter(word="很")
        self.assertEqual(len(chinese_word_list2), 1)
        english_translations2 = chinese_word_list2[0].WordEN_set
        self.assertEqual(len(english_translations2.all()), 1)
        self.assertEqual(english_translations2.all()[0].word, "very")

    def test_exists_with_no_translation(self):
        """
        exists should return false for translation if there is no translation including these words
        """
        word_zh = WordZH.objects.create(word="好")
        word_en = WordEN.objects.create(word="good")

        english_word_list = WordEN.objects.filter(word="good")
        self.assertEqual(len(english_word_list), 1)
        chinese_translations1 = english_word_list[0].wordzh_set
        self.assertEqual(len(chinese_translations1.all()), 0)

        chinese_word_list = WordZH.objects.filter(word="好")
        self.assertEqual(len(chinese_word_list), 1)
        english_translations1 = chinese_word_list[0].WordEN_set
        self.assertEqual(len(english_translations1.all()), 0)

    def test_exists_with_no_words(self):
        """
        exists should return false for translation if there is no words specified in the database
        """
        english_word_list = WordEN.objects.filter(word="good")
        self.assertEqual(len(english_word_list), 0)

        chinese_word_list = WordZH.objects.filter(word="好")
        self.assertEqual(len(chinese_word_list), 0)


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
        word_zh.WordEN_set.create(word='some_word_en')
        word_en = translator.translate('some_word_zh', Languages.chinese)
        self.assertEqual(word_en, 'some_word_en')

    def test_can_translate_english_word_with_db(self):
        word_en = WordEN(word='test_word_en')
        word_en.save()
        word_en.wordzh_set.create(word='test_word_zh', pinyin='test_word_zh_pinyin')
        word_zh = translator.translate('test_word_en', Languages.english)
        self.assertEqual(word_zh, 'test_word_zh')