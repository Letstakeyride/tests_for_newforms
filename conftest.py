import pytest
from selene.support.shared import browser


@pytest.fixture(scope='session')
def browser_manager():
    browser.driver.set_window_size(1200, 900)
    browser.open("https://demoqa.com")
    yield
    browser.quit()
