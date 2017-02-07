from selenium_tests.tests.test_base import TestBase


class TestCrudLesson(TestBase):
    def test(self):
        lessons_window = self.main_window.lesson_management()
        modify_lesson_window = lessons_window.create_lesson(topic='Test 1')
        self.assertEqual(modify_lesson_window.get_field('topic'), 'Test 1')
