from selenium.webdriver.common.by import By
from selenium.webdriver.support.expected_conditions import text_to_be_present_in_element_value
from selenium.webdriver.support.wait import WebDriverWait
from selenium_tests.core.window import Window
from selenium_tests.core.words_window import WordsWindow


class TextsWindow(WordsWindow):
    text_to_search_input_css = "#text_to_search"

    def __init__(self, driver):
        super(WordsWindow, self).__init__(driver=driver)
