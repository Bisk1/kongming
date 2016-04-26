# coding=utf-8
from unittest import skip

from django.test import TestCase
from words.models import WordZH, WordEN
from translations.utils import Languages
from words.translator import CedictClient


class WordTranslationTest(TestCase):

    def setUp(self):
        """
        Create set of English and Chinese words and relation between them:
        "cat" and "猫" which are in 1-to-1 translation relation (none of them has any other translation)
        "good" and "very" are both translation of "好"
        "very" has also another translation: "很“
        "good" does not have any other translation
        "horse" and "鸟“ are two words with no translations
        There are no other words or relations
        """
        hao = WordZH.objects.create(word="好")
        hen = WordZH.objects.create(word="很")
        mao = WordZH.objects.create(word="猫")
        WordZH.objects.create(word="鸟")
        good = WordEN.objects.create(word="good")
        very = WordEN.objects.create(word="very")
        cat = WordEN.objects.create(word="cat")
        WordEN.objects.create(word="horse")

        hao.worden_set.add(good)
        hao.worden_set.add(very)
        hen.worden_set.add(very)
        mao.worden_set.add(cat)

    def test_one_to_one_translation(self):
        """
        exists should return true for translation if it exists as the only one
        """
        cat = WordEN.objects.get(word="cat")
        chinese_translations_of_cat = [word.word for word in cat.wordzh_set.all()]
        self.assertCountEqual(chinese_translations_of_cat, ["猫"])

        mao = WordZH.objects.get(word="猫")
        english_translations_of_mao = [word.word for word in mao.worden_set.all()]
        self.assertCountEqual(english_translations_of_mao, ["cat"])

    def test_one_to_many_translation(self):
        """
        exists should return true for translation if it exists as one of many
        """
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

    def test_no_translation(self):
        """
        exists should return false for translation if there is no translation including these words
        """
        horse = WordEN.objects.get(word="horse")
        chinese_translations_of_horse = horse.wordzh_set.all()
        self.assertEqual(len(chinese_translations_of_horse), 0)

        niao = WordZH.objects.get(word="鸟")
        english_translations_of_niao = niao.worden_set.all()
        self.assertEqual(len(english_translations_of_niao.all()), 0)

    def test_exists_with_no_words(self):
        """
        exists should return false for translation if there is no words specified in the database
        """
        money_matches = WordEN.objects.filter(word="money")
        self.assertEqual(len(money_matches), 0)

        shui_matches = WordZH.objects.filter(word="水")
        self.assertEqual(len(shui_matches), 0)


class TranslatorTest(TestCase):
    translator = CedictClient()
    def test_can_translate_chinese_word_with_cedict(self):
        text_zh = '狗'
        text_en_translations = self.translator.get_word_zh_translations(text_zh)[0]
        self.assertIn('dog', text_en_translations)

    def test_can_translate_english_word_with_cedict(self):
        text_en = 'flower'
        text_zh = self.translator.get_word_en_translations(text_en)
        print(len(text_zh))
        self.assertIn(["华","huā"], text_zh)

    def test_can_translate_chinese_word_with_db(self):
        word_zh = WordZH(word='some_word_zh', pinyin='some_word_zh_pinyin')
        word_zh.save()
        word_zh.worden_set.create(word='some_word_en')
        word_en = WordZH.objects.get(word='some_word_zh').get_translations().all()[0].word
        self.assertEqual(word_en, 'some_word_en')

    def test_can_translate_english_word_with_db(self):
        word_en = WordEN(word='test_word_en')
        word_en.save()
        word_en.wordzh_set.create(word='test_word_zh', pinyin='test_word_zh_pinyin')
        word_zh = WordEN.objects.get(word='test_word_en').get_translations().all()[0].word
        self.assertEqual(word_zh, 'test_word_zh')