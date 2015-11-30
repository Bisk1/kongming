import unittest
from selenium_tests.core.login_window import LoginWindow


class BaseTest(unittest.TestCase):
    def setUp(self):
        login_window = LoginWindow(url="localhost:8000")
        login_window.load()
        self.main_window = login_window.login(username="admin", password="abcdef")

    def tearDown(self):
        print("Trying to tearDown")
        self.main_window.exit()
