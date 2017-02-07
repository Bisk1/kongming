from selenium_tests.core.login_window import LoginWindow
from django.test import TestCase


class TestBase(TestCase):
    def setUp(self):
        window = LoginWindow(url="localhost:8000")
        window.load()
        self.addCleanup(window.exit)
        window = window.login(username="admin", password="abcdef")
        self.main_window = window