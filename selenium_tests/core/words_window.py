from selenium_tests.core.window import Window

class WordsWindow(Window):
    word_to_search_input_css = "#word_to_search"
    first_translation_text_css = "table#translations_table tr:first-child > td:nth-child(2) > input"
    first_translation_pinyin_css = "table#translations_table tr:first-child > td:nth-child(4) > input"
    edit_button_css = "#edit"
    add_translation_button_css = "#add_translation_button"
    save_button_css = "#save_button"
    autocomplete_ui_css = "ul.ui-autocomplete"
    any_autocomplete_position_css = "ul.ui-autocomplete > li"

    def __init__(self, driver):
        super(WordsWindow, self).__init__(driver=driver)

    def type_word_to_search(self, text):
        self.driver.find_element_by_css_selector(self.word_to_search_input_css).send_keys(text)

    def type_first_translation_text(self, text):
        self.driver.find_element_by_css_selector(self.first_translation_text_css).send_keys(text)

    def type_first_translation_pinyin(self, text):
        self.driver.find_element_by_css_selector(self.first_translation_pinyin_css).send_keys(text)

    def get_autocomplete_hints(self):
        self.wait_for_element(self.autocomplete_ui_css)
        autocomplete_positions = self.driver.find_elements_by_css_selector(self.any_autocomplete_position_css)
        return [position.text for position in autocomplete_positions]

    def edit(self):
        self.driver.find_element_by_css_selector(self.edit_button_css).click()

    def add(self):
        self.driver.find_element_by_css_selector(self.add_translation_button_css).click()

    def save(self):
        self.driver.find_element_by_css_selector(self.save_button_css).click()
