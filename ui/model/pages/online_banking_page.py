from allure_commons._allure import step
from selene import by, have
from selene.support.shared import browser


class OnlineBankingPage:
    @step
    def check_results(self, value):
        browser.elements(by.css('#online_banking_features')).should(have.size(value))
        return self

    @step
    def check_results_in_collection(self, value):
        browser.elements(by.css('h4')).should(have.size(value))
        return self
