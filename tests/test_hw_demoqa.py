import time

from selene import browser, be, have
import os
asfasfqwf

def test_registration_form():
    browser.open("/automation-practice-form")

    browser.element("#firstName").type("Max")
    browser.element("#lastName").type("Cheshire")
    browser.element("#userEmail").type("MaxCheshire@gmail.com")
    browser.element('[for="gender-radio-1"]').click()
    browser.element("#userNumber").type("79991231234")
    browser.element("#dateOfBirthInput").click()
    browser.element('.react-datepicker__month-select').click().element('option[value="1"]').click()
    browser.element('.react-datepicker__year-select').click().element('option[value="1998"]').click()
    browser.element('.react-datepicker__day--026').click()
    browser.element('#subjectsInput').type('Engl').press_enter()
    browser.element('label[for="hobbies-checkbox-1"]').click()
    browser.element('label[for="hobbies-checkbox-2"]').click()
    browser.element('#uploadPicture').send_keys(os.path.abspath('picture/fier.webp'))
    browser.element('#currentAddress').type('Pyshkina-kolotushkina, Moscow, Russia')
    browser.element('#react-select-3-input').type('Utt').press_enter()
    browser.element('#react-select-4-input').type('Lu').press_enter()
    browser.element('#submit').execute_script('element.click()')
    time.sleep(20.0)





