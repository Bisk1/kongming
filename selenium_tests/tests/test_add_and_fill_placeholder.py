import time
from selenium_tests.core.main_window import MainWindow
from selenium_tests.tests.test_base import TestBase


class TestAddAndFillAudioPlaceholder(TestBase):

    def test(self):
        lesson_management = self.main_window.lesson_management()
        lesson = lesson_management.add_lesson()
        lesson = lesson.fill_and_save("TestTopic", 1)
        lesson_id = lesson.get_id()
        exercise_window = lesson.create_explanation_exercise()
        exercise_window.fill("abc")
        lesson = exercise_window.save()  # must save to create placeholder
        exercise_window = lesson.edit_explanation_exercise(1)
        exercise_window.create_audio_placeholder("TestPlaceholder")
        exercise_window.save()
        placeholders_window = self.main_window.placeholders()
        placeholders_window.record_audio("TestPlaceholder")

        lesson_window = self.main_window.lesson_management().modify_lesson(lesson_id)
        explanation_content = lesson_window.edit_explanation_exercise(1).read_content()

        self.assertNotIn("TestPlaceholder" in explanation_content, "Placeholder still present in the explanation content")
        self.assertIn(".wav" in explanation_content, "Audio not present in the explanation content")



    def tearDown(self):
        self.main_window.exit()
