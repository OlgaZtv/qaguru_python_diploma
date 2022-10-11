from selene.support.shared import browser

from ui.model.feedback import FeedBackPage
from ui.model.pages import ZeroBankPage

form = ZeroBankPage()
feedback = FeedBackPage()


def given_zero_bank_opened():
    url = 'http://zero.webappsecurity.com/'
    browser.open(url)
