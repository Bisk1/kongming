import os
from selenium import webdriver
import time
from selenium.common.exceptions import WebDriverException, TimeoutException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

class Window(object):
    def __init__(self, driver=None):
        if not driver:
            if os.name == "posix":
                driver_name = "chromedriver"
            else:
                driver_name = "chromedriver.exe"

            chrome_options = Options()
            chrome_options.add_argument("--use-fake-ui-for-media-stream")
            self.driver = webdriver.Chrome(executable_path="./" + driver_name, port=5673, chrome_options=chrome_options)
        else:
            self.driver = driver
        self.driver.implicitly_wait(5)

    def load(self):
        pass

    def exit(self):
        self.driver.close()

    def wait_for_loading(self, timeout=10, time_step=0.5):
        while timeout > 0:
            try:
                active_number = self.driver.execute_script("return jQuery.active")
            except WebDriverException:
                return
            if active_number == 0:
                return
            timeout -= time_step
            time.sleep(time_step)
        raise TimeoutException("Timed out waiting for loading")

    def wait_for_element(self, selector, by=By.CSS_SELECTOR, timeout=10):
        WebDriverWait(self.driver, timeout).until(
            expected_conditions.visibility_of_element_located((by, selector)),
            'Timeout when waiting for element with selector: ' + selector)

    def wait_and_click(self, selector, by=By.CSS_SELECTOR, timeout=10):
        self.wait_for_element(selector, by, timeout)
        try:
            self.driver.find_element(by, selector).click()
        except WebDriverException:
            time.sleep(1)
            self.driver.find_element(by, selector).click()


    def refresh(self):
        self.driver.refresh()