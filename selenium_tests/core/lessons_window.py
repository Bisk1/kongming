from selenium_tests.core.form_window import FormWindow
from selenium_tests.core.modify_lesson_window import ModifyLessonWindow
from selenium_tests.core.window import Window


class LessonsWindow(Window):
    new_lesson_css = "#new_lesson"
    modify_lesson_css = 'a[href="/lessons/modify_lesson/%s/"]'

    def __init__(self, driver):
        super(LessonsWindow, self).__init__(driver=driver)

    def load(self):
        self.wait_for_loading()
        self.wait_for_element(self.new_lesson_css)

    def create_lesson(self, topic, exercises_number=0, requirement=None):
        self.wait_and_click(self.new_lesson_css)
        new_lesson_form = FormWindow(driver=self.driver)
        new_lesson_form.set_field('topic', topic)
        new_lesson_form.set_field('exercises_number', exercises_number)
        if requirement:
            new_lesson_form.set_field('requirement', requirement)
        new_lesson_form.save()
        return ModifyLessonWindow(driver=self.driver)

    def modify_lesson(self, id):
        self.driver.find_element_by_css_selector(self.modify_lesson_css % id).click()
        modify_lesson = ModifyLessonWindow(driver=self.driver)
        modify_lesson.load()
        return modify_lesson
