from selene import have
from selene.support.shared import browser


class LeftPanel:

    def __int__(self):
        self.left_panel = browser.element('.left-pannel')

    def open_form(self, group, item):
        self.left_panel.all(".header-text").element_by(have.exact_text(group)).click()
        self.left_panel.all(".text").element_by(have.exact_text(item)).click()

    def open_simple_registration_form(self):
        self.open_form("Elements", "Text Box")
