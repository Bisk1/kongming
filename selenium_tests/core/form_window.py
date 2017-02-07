from selenium_tests.core.window import Window


class FormWindow(Window):

    save_button_css = "button#save"

    def set_field(self, name, value):
        css_selector = "#id_" + name
        self.wait_for_element(css_selector)
        field = self.driver.find_element_by_css_selector(css_selector)
        field.send_keys(value)

    def get_field(self, name):
        css_selector = "#id_" + name
        self.wait_for_element(css_selector)
        field = self.driver.find_element_by_css_selector(css_selector)
        return field.get_attribute('value')

    def save(self):
        self.wait_and_click(self.save_button_css)