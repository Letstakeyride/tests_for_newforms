import pytest
from selene.support.shared import browser


def test_for_registration(browser_manager):
    browser.open("/automation-practice-form")
    browser.element("#firstName").send_keys('Andrei')
    browser.element("#lastName").send_keys('Gargalyk')
    browser.element('#userEmail').send_keys('baka@mail.com')