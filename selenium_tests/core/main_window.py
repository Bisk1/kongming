from selenium_tests.core.management_window import LessonManagementWindow
from selenium_tests.core.window import Window


class MainWindow(Window):
    navbar_header_css = "div.navbar-header"
    lesson_management_css = 'a[href="/lessons/"]'

    def __init__(self, driver):
        super(MainWindow, self).__init__(driver=driver)

    def load(self):
        self.wait_for_loading()
        self.wait_for_element(css_selector=self.navbar_header_css)

    def lesson_management(self):
        self.wait_for_element(self.lesson_management_css)
        self.driver.find_element_by_css_selector(self.lesson_management_css).click()
        lesson_management = LessonManagementWindow(driver=self.driver)
        lesson_management.load()
        return lesson_management