from selenium_tests.core.lesson_window import LessonWindow
from selenium_tests.core.window import Window


class LessonManagementWindow(Window):
    new_lesson_css = "#new_lesson"
    modify_lesson_css = 'a[href="/lessons/modify_lesson/%s/"]'

    def __init__(self, driver):
        super(LessonManagementWindow, self).__init__(driver=driver)

    def load(self):
        self.wait_for_loading()
        self.wait_for_element(self.new_lesson_css)

    def modify_lesson(self, lesson_id):
        self.wait_and_click(self.modify_lesson_css % lesson_id)
        modify_lesson = LessonWindow(driver=self.driver)
        modify_lesson.load()
        return modify_lesson

    def add_lesson(self):
        self.wait_and_click(self.new_lesson_css)
        return LessonWindow(self.driver)