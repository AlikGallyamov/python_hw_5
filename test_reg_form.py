from selene import browser, have, be, query, command
import pytest


def test_registration():
    browser.open('https://app.qa.guru/automation-practice-form/')
    browser.element('[data-testid=ClearIcon]').click()
    browser.element('[id=":r0:"]').should(be.blank).type('Ivan')
    browser.element('[id=":r1:"]').should(be.blank).type('Ivanov')
    browser.element('[id=":r2:"]').should(be.blank).type('supernatural@mail.ru')
    browser.element('[data-testid="phone"]').type('9999999999')
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
    browser.element('[value=Sports]').click()
    browser.element('[value=Reading]').click()
    browser.element('[value=Music]').click()
    browser.all('[class*=css-16dka97]>div').first.click()
    browser.element('[data-value=Dance]').click()
    browser.element('[data-value=Music]').click()
    browser.element('[data-value=Sports]').click()
    browser.element('[role=listbox]').press_escape()
    browser.element('[class="MuiStack-root css-1t62lt9"]>div').perform(command.js.scroll_into_view)
    browser.all('[class="MuiStack-root css-1t62lt9"]>div').first.click()

    browser.element('[data-value="Delaware"]').click()
    browser.all('[class*=css-1t62lt9]>div').second.click()
    browser.all('.css-r8u8y9>li').should(have.size(4)).second.click()
    browser.element('.css-1gqubxi input').set_value('')
    browser.element('[data-testid="address"]').should(be.blank).type('Baker Street')
    browser.element('//button[contains(text(), "Submit")]').double_click()
    browser.all('[class="MuiGrid-root css-1tz2jme"]').should(have.texts(
        'Ivan',
        'Iasdo'
    ))

