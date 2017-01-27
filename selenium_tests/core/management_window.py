from selenium_tests.core.modify_lesson_window import ModifyLessonWindow
from selenium_tests.core.window import Window


class LessonManagementWindow(Window):
    new_lesson_css = "#new_lesson"
    modify_lesson_css = 'a[href="/lessons/modify_lesson/%s/"]'

    def __init__(self, driver):
        super(LessonManagementWindow, self).__init__(driver=driver)

    def load(self):
        self.wait_for_loading()
        self.wait_for_element(self.new_lesson_css)

    def modify_lesson(self, number_of_lesson):
        self.driver.find_element_by_css_selector(self.modify_lesson_css % number_of_lesson).click()
        modify_lesson = ModifyLessonWindow(driver=self.driver, number_of_lesson=number_of_lesson)
        modify_lesson.load()
        return modify_lesson
