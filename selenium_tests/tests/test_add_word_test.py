from selenium_tests.tests.test_base_test import BaseTest


class AddWordZhTest(BaseTest):
    def setUp(self):
        super(AddWordZhTest, self).setUp()
        self.number_of_lesson = "4"
        self.category = "word_zh"
        self.new_word = "Nowe slowo"
        self.pinyin = "AA"
        self.translations = "BB"
        self.number = "11"
        self.new_word_value = None

    def test(self):
        lesson_management = self.main_window.lesson_management()
        self.modify_lesson = lesson_management.modify_lesson(number_of_lesson=self.number_of_lesson)
        self.new_word_value = self.modify_lesson.add_word(category=self.category, new_word=self.new_word, pinyin=self.pinyin,
                                                translations=self.translations, number=self.number)
        if not self.new_word_value:
            assert "Adding word has failed"

    def tearDown(self):
        if self.new_word_value:
            if not self.modify_lesson.delete_word(self.new_word_value):
                assert "Deleting word has failed"
        self.main_window.exit()
