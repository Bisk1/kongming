from selenium_tests.core.form_window import FormWindow


class DeleteWindow(FormWindow):
    def confirm(self):
        self.save()
