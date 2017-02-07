import re

from selenium_tests.core.form_window import FormWindow


class ModifyLessonWindow(FormWindow):
    add_button_css = "button#add"
    save_button_css = "button#save"
    category_css = '#menu > option[addr="/lessons/modify_lesson/%s/add_exercise_%s/"]'

    word_zh_css = "#id_word_zh"
    pinyin_css = "#id_pinyin"
    translations_css = "#id_translations_pl"
    number_css = "#id_number"
    delete_button_css = "#exercises button"

    def __init__(self, driver):
        super(ModifyLessonWindow, self).__init__(driver=driver)
        url = driver.current_url
        m = re.search('lessons/(\\d+)/modify', url)
        self.id = m.group(1)

    def load(self):
        self.wait_for_loading()
        self.wait_for_element(css_selector=self.add_button_css)

    def add_word(self, category, new_word, pinyin, translations, number):
        id_exercises_before = [element.get_attribute("value") for element
                               in self.driver.find_elements_by_css_selector(self.delete_button_css)]
        self.driver.find_element_by_css_selector(self.add_button_css).click()
        self.wait_for_loading()
        self.driver.find_element_by_css_selector(self.category_css % (self.id, category)).click()
        self.wait_for_loading()

        word_zh_input = self.driver.find_element_by_css_selector(self.word_zh_css)
        pinyin_input = self.driver.find_element_by_css_selector(self.pinyin_css)
        translations_input = self.driver.find_element_by_css_selector(self.translations_css)
        number_input = self.driver.find_element_by_css_selector(self.number_css)
        save_button = self.driver.find_element_by_css_selector(self.save_button_css)

        word_zh_input.send_keys(new_word)
        pinyin_input.send_keys(pinyin)
        translations_input.send_keys(translations)
        number_input.send_keys(number)

        save_button.click()
        self.wait_for_loading()

        id_exercises_after = [element.get_attribute("value") for element
                              in self.driver.find_elements_by_css_selector(self.delete_button_css)]
        if len(id_exercises_after) - len(id_exercises_before) != 1:
            return False
        new = set(id_exercises_after) - set(id_exercises_before)
        return list(new)[0]

    def delete_word(self, value):
        delete_buttons = [button for button in self.driver.find_elements_by_css_selector(self.delete_button_css)
                          if button.get_attribute("value") == value]
        if len(delete_buttons) == 0:
            return False
        delete_buttons[0].click()
        delete_buttons = [button for button in self.driver.find_elements_by_css_selector(self.delete_button_css)
                          if button.get_attribute("value") == value]
        if len(delete_buttons) > 0:
            return False
        return True

