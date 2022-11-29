import allure
from allure_commons.types import Severity

from ui.model import app
from ui.model.data import full_name, password, email_random, text_random, comment


@allure.description('Zero Bank UI tests')
@allure.tag('UI', 'WEB')
@allure.label('owner', 'zatulivetrova')
@allure.feature('UI')
@allure.story('Search')
class TestsSearch:
    @allure.severity(Severity.NORMAL)
    @allure.title('Check the search is working on main page')
    def test_search(self):
        # GIVEN
        browser = self

        # WHEN
        with allure.step("Open Zero Bank page"):
            app.given_zero_bank_opened()

        with allure.step("Input money text"):
            app.main.fill_input('money')

        # THEN
        with allure.step("Search money text"):
            app.main.check_query_results('money')


@allure.description('Zero Bank UI tests')
@allure.tag('UI', 'WEB')
@allure.label('owner', 'zatulivetrova')
@allure.feature('UI')
@allure.story('Service page')
class TestServicePage:
    @allure.severity(Severity.NORMAL)
    @allure.title("Check services test")
    def test_check_services(self):
        # GIVEN
        browser = self

        with allure.step("Open Zero Bank page"):
            app.given_zero_bank_opened()

        # WHEN
        with allure.step('Push More Services button'):
            app.main.check_services()

        # THEN
        with allure.step('Check results on a page'):
            app.service.check_results(1)

        with allure.step('Check results in collection'):
            app.service.check_results_in_collection(6)


@allure.description('Zero Bank UI tests')
@allure.tag('UI', 'WEB')
@allure.label('owner', 'zatulivetrova')
@allure.feature('UI')
@allure.story('Forms tests')
class TestsForms:
    @allure.severity(Severity.CRITICAL)
    @allure.title("Check Sign in form test")
    def test_check_sing_in_form(setup_browser):
        # GIVEN
        browser = setup_browser
        with allure.step("Open Zero Bank page"):
            app.given_zero_bank_opened()

        # WHEN
        with allure.step('Go to Sing in form'):
            app.auth.click_to_sing_in()

        with allure.step('Fill login'):
            app.auth.fill_login_input(full_name)

        with allure.step('Fill password'):
            app.auth.fill_password_input(password)

        with allure.step('Click submit button'):
            app.auth.click_submit()

        # THEN
        with allure.step('Check error message'):
            app.auth.check_error_message('Login and/or password are wrong.')

    @allure.severity(Severity.CRITICAL)
    @allure.title("Check Forgot your password form")
    def test_check_forgot_password_form(self):
        # GIVEN
        browser = self
        message = 'Your password will be sent to the following email: '
        email = email_random

        with allure.step("Open Zero Bank page"):
            app.given_zero_bank_opened()

        # WHEN
        with allure.step('Go to Sing in form'):
            app.auth.click_to_sing_in()

        with allure.step('Click "Forgot your password" link'):
            app.forgottenPasswordPage.click_forgot_your_password_link()

        with allure.step('Fill password'):
            app.forgottenPasswordPage.fill_email_input(email_random)

        with allure.step('Click submit button'):
            app.auth.click_submit()

        # THEN
        with allure.step('Check message'):
            app.forgottenPasswordPage.check_message(message, email_random)

    @allure.severity(Severity.NORMAL)
    @allure.title("Check Feedback form")
    def test_check_feedback_form(self):
        # GIVEN
        browser = self

        with allure.step("Open Zero Bank page"):
            app.given_zero_bank_opened()

        # WHEN
        with allure.step('Go to Feedback form'):
            app.main.click_to_feedback()

        with allure.step('Fill name in Feedback form'):
            app.feedback.fill_input_name(full_name)

        with allure.step('Fill email in Feedback form'):
            app.feedback.fill_input_email(email_random)

        with allure.step('Fill subject Feedback form'):
            app.feedback.fill_input_subject(text_random)

        with allure.step('Fill comment in Feedback form'):
            app.feedback.fill_input_comment(comment)

        with allure.step('Press submit button on Feedback form'):
            app.feedback.press_submit()

        # THEN
        with allure.step('Check that our feedback was sending'):
            app.feedback.check_message_sent()
