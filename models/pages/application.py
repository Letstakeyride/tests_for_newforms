from selene.support.shared import browser

from models.Components.left_panel import LeftPanel
from models.pages.simple_registrationpage import SimpleRegistrationPage


class Application:
    def __init__(self):
        self.left_panel = LeftPanel()
        self.simple_registration_form = SimpleRegistrationPage()

    @staticmethod
    def open():
        browser.open("/forms")


app = Application()