from selenium_tests.tests.test_base import TestBase


class TestAddWordZh(TestBase):
    def setUp(self):
        super(TestAddWordZh, self).setUp()
        self.number_of_lesson = "4"
        self.category = "word_zh"
        self.new_word = "Nowe slowo"
        self.pinyin = "AA"
        self.translations = "BB"
        self.number = "11"
        self.new_word_value = None

    def test(self):
        words = self.main_window.words()
        words.type_word_to_search("hello")
        words.add()
        words.type_first_translation_text("你好")
        words.type_first_translation_pinyin("nǐhǎo")
        words.save()
        words.refresh()
        words.type_word_to_search("hello")
        words_hints = words.get_autocomplete_hints()
        if "hello" not in words_hints:
            assert "Adding word has failed"

    def tearDown(self):
        if self.new_word_value:
            if not self.modify_lesson.delete_word(self.new_word_value):
                assert "Deleting word has failed"
        self.main_window.exit()
