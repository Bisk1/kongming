from selenium_tests.core.main_window import MainWindow
from selenium_tests.core.window import Window


class LoginWindow(Window):
    user_input_css = "#id_username"
    password_input_css = "#id_password"
    submit_button_css = 'input[type="submit"]'

    def __init__(self, url):
        super(LoginWindow, self).__init__()
        self.url = url

    def load(self):
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.wait_for_loading()

    def login(self, username, password):
        username_input = self.driver.find_element_by_css_selector(self.user_input_css)
        password_input = self.driver.find_element_by_css_selector(self.password_input_css)
        submit_button = self.driver.find_element_by_css_selector(self.submit_button_css)

        username_input.send_keys(username)
        password_input.send_keys(password)
        submit_button.click()

        main_window = MainWindow(driver=self.driver)
        main_window.load()
        return main_window