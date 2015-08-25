# coding=utf-8

from django.test import TestCase
from translations.models import WordZH, WordPL, WordTranslation


class WordTranslationTest(TestCase):

    def test_polish_word_exists_with_one_translation(self):
        """
        exists should return true for translation if it exists as the only one
        """
        word_zh = WordZH.objects.create(word="hao")
        word_pl = WordPL.objects.create(word="dobrze")
        WordTranslation.objects.create(word_zh=word_zh, word_pl=word_pl)

        polish_word_list = WordPL.objects.filter(word="dobrze")
        self.assertEqual(len(polish_word_list), 1)
        chinese_translations = polish_word_list[0].wordzh_set
        self.assertEqual(len(chinese_translations.all()), 1)
        self.assertEqual(chinese_translations.all()[0].word, "hao")

        chinese_word_list = WordZH.objects.filter(word="hao")
        self.assertTrue(len(chinese_word_list) == 1)
        polish_translations = chinese_word_list[0].wordpl_set
        self.assertEqual(len(polish_translations.all()), 1)
        self.assertEqual(polish_translations.all()[0].word, "dobrze")

    def test_exists_with_many_translation(self):
        """
        exists should return true for translation if it exists as one of many
        """
        word_zh1 = WordZH.objects.create(word="hao")
        word_zh2 = WordZH.objects.create(word="hen")
        word_pl1 = WordPL.objects.create(word="dobrze")
        word_pl2 = WordPL.objects.create(word="bardzo")
        WordTranslation.objects.create(word_zh=word_zh1, word_pl=word_pl1)
        WordTranslation.objects.create(word_zh=word_zh1, word_pl=word_pl2)
        WordTranslation.objects.create(word_zh=word_zh2, word_pl=word_pl2)

        polish_word_list1 = WordPL.objects.filter(word="dobrze")
        self.assertEqual(len(polish_word_list1), 1)
        chinese_translations1 = polish_word_list1[0].wordzh_set
        self.assertEqual(len(chinese_translations1.all()), 1)
        self.assertEqual(chinese_translations1.all()[0].word, "hao")

        polish_word_list2 = WordPL.objects.filter(word="bardzo")
        self.assertEqual(len(polish_word_list2), 1)
        chinese_translations2 = polish_word_list2[0].wordzh_set
        self.assertEqual(len(chinese_translations2.all()), 2)
        self.assertIn(chinese_translations2.all()[0].word, ["hao", "hen"])
        self.assertIn(chinese_translations2.all()[1].word, ["hao", "hen"])
        self.assertNotEqual(chinese_translations2.all()[0].word, chinese_translations2.all()[1].word)

        chinese_word_list1 = WordZH.objects.filter(word="hao")
        self.assertEqual(len(chinese_word_list1), 1)
        polish_translations1 = chinese_word_list1[0].wordpl_set
        self.assertEqual(len(polish_translations1.all()), 2)
        self.assertIn(polish_translations1.all()[0].word, ["dobrze", "bardzo"])
        self.assertIn(polish_translations1.all()[1].word, ["dobrze", "bardzo"])
        self.assertNotEqual(polish_translations1.all()[0].word, polish_translations1.all()[1].word)

        chinese_word_list2 = WordZH.objects.filter(word="hen")
        self.assertEqual(len(chinese_word_list2), 1)
        polish_translations2 = chinese_word_list2[0].wordpl_set
        self.assertEqual(len(polish_translations2.all()), 1)
        self.assertEqual(polish_translations2.all()[0].word, "bardzo")

    def test_exists_with_no_translation(self):
        """
        exists should return false for translation if there is no translation including these words
        """
        word_zh = WordZH.objects.create(word="hao")
        word_pl = WordPL.objects.create(word="dobrze")

        polish_word_list = WordPL.objects.filter(word="dobrze")
        self.assertEqual(len(polish_word_list), 1)
        chinese_translations1 = polish_word_list[0].wordzh_set
        self.assertEqual(len(chinese_translations1.all()), 0)

        chinese_word_list = WordZH.objects.filter(word="hao")
        self.assertEqual(len(chinese_word_list), 1)
        polish_translations1 = chinese_word_list[0].wordpl_set
        self.assertEqual(len(polish_translations1.all()), 0)

    def test_exists_with_no_words(self):
        """
        exists should return false for translation if there is no words specified in the database
        """
        polish_word_list = WordPL.objects.filter(word="dobrze")
        self.assertEqual(len(polish_word_list), 0)

        chinese_word_list = WordZH.objects.filter(word="hao")
        self.assertEqual(len(chinese_word_list), 0)

