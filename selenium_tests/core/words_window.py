from selenium.webdriver.common.by import By
from selenium.webdriver.support.expected_conditions import text_to_be_present_in_element_value
from selenium.webdriver.support.wait import WebDriverWait
from selenium_tests.core.window import Window


class WordsWindow(Window):
    source_word_css = "#id_source_word"
    first_translation_text_css = "#id_translation_0"
    first_translation_pinyin_css = "table#translations_table tr:first-child > td:nth-child(4) > input"
    edit_button_css = "#edit"
    add_translation_button_css = "#add_translation_button"
    save_button_css = "#save_button"
    autocomplete_ui_css = "ul.ui-autocomplete"
    any_autocomplete_position_css = "ul.ui-autocomplete > li"
    save_message_css = "#save_message"

    def __init__(self, driver):
        super(WordsWindow, self).__init__(driver=driver)

    def type_text_to_search(self, text):
        self.driver.find_element_by_css_selector(self.source_word_css).send_keys(text)

    def type_first_translation_text(self, text):
        self.driver.find_element_by_css_selector(self.first_translation_text_css).send_keys(text)

    def type_first_translation_pinyin(self, text):
        self.driver.find_element_by_css_selector(self.first_translation_pinyin_css).send_keys(text)

    def get_autocomplete_hints(self):
        self.wait_for_element(self.autocomplete_ui_css)
        autocomplete_positions = self.driver.find_elements_by_css_selector(self.any_autocomplete_position_css)
        return [position.text for position in autocomplete_positions]

    def wait_for_successful_save(self):
        self.wait_for_element(self.save_message_css)
        self.driver.find_element_by_css_selector(self.save_message_css).text()
        WebDriverWait(self.driver, 10).until(
            text_to_be_present_in_element_value((By.CSS_SELECTOR, self.save_message_css), "Saved!")
        )

    def edit(self):
        self.driver.find_element_by_css_selector(self.edit_button_css).click()

    def add(self):
        self.driver.find_element_by_css_selector(self.add_translation_button_css).click()

    def save(self):
        self.wait_and_click(self.save_button_css)
