from allure_commons._allure import step
from selene.support.shared import browser

from ui.model.components.authorization import Authorization
from ui.model.pages.feedback_page import FeedBackPage
from ui.model.pages.main_page import MainPage
from ui.model.pages.forgotten_password_page import ForgottenPasswordPage
from ui.model.pages.online_banking_page import OnlineBankingPage

main = MainPage()
feedback = FeedBackPage()
service = OnlineBankingPage()
password = ForgottenPasswordPage()
auth = Authorization()

@step
def given_zero_bank_opened():
    url = 'http://zero.webappsecurity.com/'
    browser.open(url)
