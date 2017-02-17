from selenium_tests.core.window import Window


class FormWindow(Window):

    save_button_css = "#submit-id-submit"

    def get_field(self, field_name):
        id_selector = "id_" + field_name
        input = self.driver.find_element_by_id(id_selector)
        input.get_attribute('value')

    def set_field(self, field_name, field_value):
        id_selector = "id_" + field_name
        input = self.driver.find_element_by_id(id_selector)
        input.clear()
        input.send_keys(field_value)

    def save(self):
        self.wait_and_click(self.save_button_css)
