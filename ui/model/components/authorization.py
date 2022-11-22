from selene import have
from selene.support import by
from selene.support.shared import browser


class Authorization:
    def click_to_sing_in(self):
        browser.element(by.css('.icon-signin')).click()
        return self

    def fill_login_input(self, value):
        browser.element(by.css('#user_login')).type(value)
        return self

    def fill_password_input(self, value):
        browser.element(by.css('#user_password')).type(value)
        return self

    def click_submit(self):
        browser.element(by.name('submit')).click()
        return self

    def check_error_message(self, value):
        browser.element(by.css('#login_form')).should(have.text(value))
        return self