from selene import browser, be, have
import os


def test_registration_form():
    browser.open("/automation-practice-form")

    browser.element("#firstName").type("Max")
    browser.element("#lastName").type("Cheshire")
    browser.element("#userEmail").type("MaxCheshire@gmail.com")
    browser.element('[for="gender-radio-1"]').click()
    browser.element("#userNumber").type("79991231234")
    browser.element("#dateOfBirthInput").click()
    browser.element('.react-datepicker__month-select').click().element('option[value="1"]').click()
    browser.element()

