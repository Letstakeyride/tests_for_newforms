from data.users import test_user
from models.pages.registration_page import RegistrationPage


def test_registration():
    registration_page = RegistrationPage(test_user)

    registration_page.open()

    registration_page.register(test_user)

    registration_page.should_have_registered(test_user)
