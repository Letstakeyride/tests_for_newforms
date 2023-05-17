from data.users import test_user
from models.pages.application import app


def test_simple_registration_form():
    app.open()
    app.left_panel.open_simple_registration_form()

    app.simple_registration_form.register(test_user)

    app.simple_registration_form.should_have_registered(test_user)
