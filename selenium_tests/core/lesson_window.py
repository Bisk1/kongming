import re
from selenium_tests.core import exercise_window
from selenium_tests.core.form_window import FormWindow


class LessonWindow(FormWindow):

    save_button_css = "#save"
    explanation_exercise_css = "#explanation"

    def fill_and_save(self, topic, exercises_number, requirement=None):
        self.set_field('topic', topic)
        self.set_field('exercises_number', exercises_number)
        if requirement:
            self.set_field('requirement', requirement)
        self.save()
        return self

    def create_explanation_exercise(self):
        self.wait_and_click(self.explanation_exercise_css)
        return exercise_window.ExplanationWindow(self.driver)

    def edit_explanation_exercise(self, number):
        button_selector = self.get_edit_button_css(number)
        self.wait_and_click(button_selector)
        return exercise_window.ExplanationWindow(self.driver)

    def get_edit_button_css(self, number):
        return "#exercises tbody :nth-child(" + str(number) + ") :nth-child(4) a"

    def get_id(self):
        url = self.driver.current_url
        match = re.search(r"lessons/(\d+)/modify", url)
        return match.group(1)

    def save(self):
        self.wait_and_click(self.save_button_css)