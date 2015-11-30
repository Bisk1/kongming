from selenium.webdriver.common.by import By
from selenium_tests.core.management_window import LessonManagementWindow
from selenium_tests.core.texts_window import TextsWindow
from selenium_tests.core.window import Window
from selenium_tests.core.words_window import WordsWindow


class MainWindow(Window):
    navbar_header_css = "div.navbar-header"
    lesson_management_css = 'a[href="/lessons/"]'

    words_translations_css = 'li#words_menu > a'
    words_translations_en_css = 'li#words_menu_en > a'
    words_translations_zh_css = 'li#words_menu_zh > a'

    texts_translations_css = 'li#texts_menu > a'
    texts_translations_en_css = 'li#texts_menu_en > a'
    texts_translations_zh_css = 'li#texts_menu_zh > a'

    def __init__(self, driver):
        super(MainWindow, self).__init__(driver=driver)

    def load(self):
        self.wait_for_loading()
        self.wait_for_element(self.navbar_header_css)

    def lesson_management(self):
        self.wait_for_element(self.lesson_management_css)
        self.driver.find_element_by_css_selector(self.lesson_management_css).click()
        lesson_management = LessonManagementWindow(driver=self.driver)
        lesson_management.load()
        return lesson_management

    def words(self):
        self.wait_and_click(self.words_translations_css)
        self.wait_and_click(self.words_translations_en_css)
        words = WordsWindow(driver=self.driver)
        return words

    def texts(self):
        self.wait_and_click(self.texts_translations_css)
        self.wait_and_click(self.texts_translations_en_css)
        texts = TextsWindow(driver=self.driver)
        return texts