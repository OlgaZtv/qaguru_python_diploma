from allure_commons._allure import step
from selene import by, have
from selene.support.shared import browser


class MainPage:

    @step
    def fill_input(self, value):
        browser.element(by.css('#searchTerm')).type(value).press_enter()
        return self

    @step
    def check_services(self):
        browser.element(by.css("#online-banking")).click()
        return self

    @step
    def check_query_results(self, value):
        browser.element(by.css('.top_offset')).should(have.text(value))
        return self

    @step
    def click_to_feedback(self):
        browser.element(by.css('#feedback')).click()
        return self





