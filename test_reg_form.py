from selene import browser, have, be
import pytest


def test_registration(window_size):
    browser.open('https://app.qa.guru/automation-practice-form/')
    browser.element('[data-testid=ClearIcon]').click()
    browser.element('[id=":r0:"]').should(be.blank).type('Ivan')
    browser.element('[id=":r1:"]').should(be.blank).type('Ivanov')
    browser.element('[id=":r2:"]').should(be.blank).type('test@mail.ru')
    browser.element('[data-testid="phone"]').type('11111111111111')
    browser.element('[role="button"]').click()
    browser.all('[class*=css-r8u8y9]>li').should(have.size(5))
    browser.element('[data-value="Russian"]').click()
    browser.element('[role="button"]').should(have.text('Russian'))
    browser.element('[data-testid="CalendarIcon"]').click()
    browser.element('[class*=css-sldnn]').click()
    browser.element('//button[contains(text(),"1996")]').click()
    browser.element('//button[contains(text(),"Feb")]').click()
    browser.element('//button[contains(text(),"22")]').click()
    browser.element('[data-testid="dateOfBirth"]').element('[value="22/02/1996"]')
    browser.element('[value=Male]').click()
    browser.element('[]').should(have.css_class('.Mui-checked.css-jl9ecy [value=Male]'))
