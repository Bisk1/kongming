from selenium_tests.tests.test_base import TestBase


class TestAddWordTranslation(TestBase):
    def setUp(self):
        super(TestAddWordTranslation, self).setUp()

    # FIXME
    # def test(self):
    #     words = self.main_window.words()
    #     words.type_text_to_search("hello")
    #     words.add()
    #     words.type_first_translation_text("你好")
    #     words.type_first_translation_pinyin("nǐhǎo")
    #     words.save()
    #     words.refresh()
    #     words.type_text_to_search("hello")
    #     words_hints = words.get_autocomplete_hints()
    #     self.assertTrue("hello" in words_hints, "New word is not shown in autocomplete box!")

    def tearDown(self):
        self.main_window.exit()
