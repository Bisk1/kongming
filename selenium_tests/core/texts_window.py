from selenium_tests.core.words_window import WordsWindow


class TextsWindow(WordsWindow):
    source_word_css = "#id_source_text"
    first_translation_css = "#id_translation_0"
    submit_id = "#submit-id-submit"

    def __init__(self, driver):
        super(WordsWindow, self).__init__(driver=driver)

    def type_text_to_search(self, text_to_search):
        self.wait_for_element(self.source_word_css)
        self.driver.find_element_by_css_selector(self.source_word_css).send_keys(text_to_search)

    def type_first_translation_text(self, translation_text):
        self.wait_for_element(self.first_translation_css)
        self.driver.find_element_by_css_selector(self.first_translation_css).send_keys(translation_text)

    def save(self):
        self.wait_and_click(self.submit_id)


