from allure_commons._allure import step
from selene import by, have
from selene.support.shared import browser


class ForgottenPasswordPage:

    @step
    def click_forgot_your_password_link(self):
        browser.element(by.text('Forgot your password ?')).click()
        return self

    @step
    def fill_email_input(self, value):
        browser.element(by.css('#user_email')).type(value)
        return self

    @step
    def check_message(self, message, email):
        message = message
        email = email
        browser.element(by.text(message + email)).should(have.text(message + email))
        return self
