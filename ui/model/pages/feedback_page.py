from allure_commons._allure import step
from selene import by, have
from selene.support.shared import browser


class FeedBackPage:

    @step
    def fill_input_name(self, value):
        browser.element(by.css('#name')).type(value)
        return self

    @step
    def fill_input_email(self, value):
        browser.element(by.css('#email')).type(value)
        return self

    @step
    def fill_input_subject(self, value):
        browser.element(by.css('#subject')).type(value)
        return self

    @step
    def fill_input_comment(self, value):
        browser.element(by.css('#comment')).type(value)
        return self

    @step
    def press_submit(self):
        browser.element(by.name('submit')).click()
        return self

    @step
    def press_clear(self):
        browser.element(by.name('clear')).click()
        return self

    @step
    def check_message_sent(self):
        browser.elements(by.css('.container')).should(have.size_greater_than(0))
        return self
