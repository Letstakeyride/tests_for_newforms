from selene import have
from selene.support.shared import browser

from data.users import Users


class SimpleRegistrationPage:
    def __init__(self):
        self.full_name = browser.element("#userName")
        self.email = browser.element("#userEmail")
        self.current_address = browser.element("#currentAddress")
        self.permanent_address = browser.element("#permanentAddress")
        self.output_name = browser.element("[id=output] [id=name]")
        self.output_email = browser.element("[id=output] [id=email]")
        self.output_current_address = browser.element("[id=output] [id=currentAddress]")
        self.output_permanent_address = browser.element("[id=output] [id=permanentAddress]")
        self.submit = browser.element("#submit")

    def register(self, user: Users):
        self.full_name.set_value(user.full_name)
        self.email.set_value(user.email)
        self.current_address.set_value(user.address)
        self.permanent_address.set_value(user.permanent_address)
        self.submit.click()

    def should_have_registered(self, user: Users):
        self.output_name.should(have.text(user.full_name))
        self.output_email.should(have.text(user.email))
        self.output_current_address.should(have.text(user.address))
        self.output_permanent_address.should(have.text(user.permanent_address))
