from selene import by
from selene.support.shared import browser


class FeedBackPage:
    def fill_input_name(self, value):
        browser.element(by.css('#name')).type(value)
        return self

    def fill_input_email(self, value):
        browser.element(by.css('#email')).type(value)
        return self

    def fill_input_subject(self, value):
        browser.element(by.css('#subject')).type(value)
        return self

    def fill_input_comment(self, value):
        browser.element(by.css('#comment')).type(value)
        return self

    def press_submit(self):
        browser.element(by.name('submit')).click()
        return self

    def press_clear(self):
        browser.element(by.name('clear')).click()
        return self
