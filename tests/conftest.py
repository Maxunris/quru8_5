import pytest
from selene import browser

@pytest.fixture(scope='function', autouse=True)
def browser_setup():
    browser.config.base_url = "https://demoqa.com"
    browser.config.window_width = 700
    browser.config.window_height = 700

    yield

    browser.quit()