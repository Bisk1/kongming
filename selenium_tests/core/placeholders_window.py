from selenium.webdriver.common.by import By
from selenium_tests.core.window import Window


class PlaceholdersWindow(Window):
    cleanup_audios_css = "#cleanup_audios"

    def clear_orphan_audios(self):
        self.wait_and_click(self.cleanup_audios_css)

    def record_audio(self, placeholder_name):
        record_button_xpath = self.get_record_button_xpath(placeholder_name)
        start_button_xpath = self.get_first_button_xpath(placeholder_name)
        stop_button_xpath = start_button_xpath   # same xpath anyway
        confirm_button_xpath = start_button_xpath   # and here

        self.wait_and_click(by=By.XPATH, selector=record_button_xpath)
        self.wait_and_click(by=By.XPATH, selector=start_button_xpath)
        self.wait_and_click(by=By.XPATH, selector=stop_button_xpath)
        self.wait_and_click(by=By.XPATH, selector=confirm_button_xpath)

    def get_record_button_xpath(self, placeholder_name):
        return "//tr/td[1][contains(text(), '" + placeholder_name + "')]/../td[3]/button"

    def get_first_button_xpath(self, placeholder_name):
        return "//tr/td[1][contains(text(), '" + placeholder_name + "')]/../td[3]/div/button"

