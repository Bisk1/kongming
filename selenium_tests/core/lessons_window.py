from selenium_tests.core.delete_window import DeleteWindow
from selenium_tests.core.form_window import FormWindow
from selenium_tests.core.lesson_window import LessonWindow
from selenium_tests.core.window import Window


class LessonsWindow(Window):
    new_lesson_css = "#new_lesson"
    modify_lesson_css = 'a[href="/lessons/%s/modify/"]'
    delete_lesson_css = 'a[href="/lessons/%s/delete/"]'

    def load(self):
        self.wait_for_loading()
        self.wait_for_element(self.new_lesson_css)

    def create_lesson(self, topic, exercises_number=0, requirement=None):
        self.wait_and_click(self.new_lesson_css)
        new_lesson_form = LessonWindow(driver=self.driver)
        new_lesson_form.set_field('topic', topic)
        new_lesson_form.set_field('exercises_number', exercises_number)
        if requirement:
            new_lesson_form.set_field('requirement', requirement)
        new_lesson_form.save()
        return LessonWindow(driver=self.driver)

    def modify_lesson(self, id):
        self.driver.find_element_by_css_selector(self.modify_lesson_css % id).click()
        modify_lesson = LessonWindow(driver=self.driver)
        modify_lesson.load()
        return modify_lesson

    def delete_lesson(self, id):
        self.driver.find_element_by_css_selector(self.delete_lesson_css % id).click()
        return DeleteWindow(driver=self.driver)