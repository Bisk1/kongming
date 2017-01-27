from selenium_tests.tests.test_base import TestBase


class TestAddTextTranslation(TestBase):
    def setUp(self):
        super(TestAddTextTranslation, self).setUp()

    def test(self):
        texts = self.main_window.texts()
        texts.type_text_to_search("Where is he?")
        texts.type_first_translation_text("他在那里？")
        texts.save()
        texts.refresh()
        texts.type_text_to_search("Where")
        texts_hints = texts.get_autocomplete_hints()
        self.assertTrue("Where is he?" in texts_hints, "New text is not shown in autocomplete box!")

    def tearDown(self):
        self.main_window.exit()
