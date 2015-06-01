from selenium import webdriver
import time
from selenium.common.exceptions import WebDriverException, TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Window(object):
    def __init__(self, driver=None):
        if not driver:
            self.driver = webdriver.Chrome()
        else:
            self.driver = driver

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

    def wait_for_element(self, css_selector, timeout=10):
        WebDriverWait(self.driver, timeout).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, css_selector)))