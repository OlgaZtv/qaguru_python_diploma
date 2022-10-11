from selene import by, have
from selene.support.shared import browser


class ZeroBankPage:

    def fill_input(self, value):
        browser.element(by.css('#searchTerm')).type(value).press_enter()
        return self

    def check_services(self):
        browser.element(by.css("#online-banking")).click()
        return self

    def check_query_results(self, value):
        browser.element(by.css('.top_offset')).should(have.text(value))
        return self

    def check_results(self, value):
        browser.elements(by.css('#online_banking_features')).should(have.size(value))
        return self

    def check_results_in_collection(self, value):
        browser.elements(by.css('h4')).should(have.size(value))
        return self

    def click_to_sing_in(self):
        browser.element(by.css('.icon-signin')).click()
        return self

    def click_to_feedback(self):
        browser.element(by.css('#feedback')).click()
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

    def click_forgot_your_password_link(self):
        browser.element(by.text('Forgot your password ?')).click()
        return self

    def fill_email_input(self, value):
        browser.element(by.css('#user_email')).type(value)
        return self

    def check_message(self, message, email):
        message = message
        email = email
        browser.element(by.text(message + email)).should(have.text(message + email))
        return self


