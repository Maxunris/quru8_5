import pytest
from selene import browser

@pytest.fixture(scope='function', autouse=True)
def browser_setup():
    browser.config.base_url = "https://demoga.com"
    browser.config.window_width = 600
    browser.config.window_height = 900

    yield

    browser.quit()