from selene import browser, be, have
import os


def test_registration_form():
    browser.open("/")
