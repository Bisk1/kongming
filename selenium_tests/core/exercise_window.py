import time
from selenium_tests.core.form_window import FormWindow
import selenium_tests.core.lesson_window

class ExerciseWindow(FormWindow):
    def save(self):
        super().save()
        return selenium_tests.core.lesson_window.LessonWindow(self.driver)


class ExplanationWindow(ExerciseWindow):

    redactor_field_css = ".redactor-editor"
    audio_button_css = ".icon-music"
    placeholder_text_css = "#placeholder-recording-text"
    create_placeholder_button_css = "#create-placeholder"

    def fill_placeholder(self, content):
        content_field = self.driver.find_element_by_css_selector(self.redactor_field_css)
        time.sleep(0.5)
        content_field.send_keys(content)

    def create_audio_placeholder(self, name):
        self.wait_and_click(self.audio_button_css)
        self.driver.find_element_by_css_selector(self.placeholder_text_css).send_keys(name)
        self.wait_and_click(self.create_placeholder_button_css)

    def read_content(self):
        content_field = self.driver.find_element_by_css_selector(self.redactor_field_css)
        return content_field.text