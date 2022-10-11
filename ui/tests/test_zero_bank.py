import allure

from ui.model import app
from ui.model.data import full_name, password, email_random, text_random, comment


@allure.description('Zero Bank UI tests')
@allure.tag('UI')
@allure.title("Search test")
def test_zero_bank_search(setup_browser):
    browser = setup_browser

    with allure.step("Open Zero Bank page"):
        app.given_zero_bank_opened()

    with allure.step("Input money text"):
        app.form.fill_input('money')

    with allure.step("Search money text"):
        app.form.check_query_results('money')


@allure.title("Check services test")
def test_zero_bank_check_services(setup_browser):
    browser = setup_browser

    with allure.step("Open Zero Bank page"):
        app.given_zero_bank_opened()

    with allure.step('Push More Services button'):
        app.form.check_services()

    with allure.step('Check results on a page'):
        app.form.check_results(1)

    with allure.step('Check results in collection'):
        app.form.check_results_in_collection(6)


@allure.title("Check Sign in form test")
def test_zero_bank_check_sing_in_form(setup_browser):
    browser = setup_browser

    with allure.step("Open Zero Bank page"):
        app.given_zero_bank_opened()

    with allure.step('Go to Sing in form'):
        app.form.click_to_sing_in()

    with allure.step('Fill login'):
        app.form.fill_login_input(full_name)

    with allure.step('Fill password'):
        app.form.fill_password_input(password)

    with allure.step('Click submit button'):
        app.form.click_submit()

    with allure.step('Check error message'):
        app.form.check_error_message('Login and/or password are wrong.')


@allure.title("Check Forgot your password form")
def test_zero_bank_check_forgot_password_form(setup_browser):
    browser = setup_browser
    message = 'Your password will be sent to the following email: '
    email = email_random

    with allure.step("Open Zero Bank page"):
        app.given_zero_bank_opened()

    with allure.step('Go to Sing in form'):
        app.form.click_to_sing_in()

    with allure.step('Click "Forgot your password" link'):
        app.form.click_forgot_your_password_link()

    with allure.step('Fill password'):
        app.form.fill_email_input(email_random)

    with allure.step('Click submit button'):
        app.form.click_submit()

    with allure.step('Check message'):
        app.form.check_message(message, email_random)


@allure.title("Check Feedback form")
def test_zero_bank_check_feedback_form(setup_browser):
    browser = setup_browser

    with allure.step("Open Zero Bank page"):
        app.given_zero_bank_opened()

    with allure.step('Go to Feedback form'):
        app.form.click_to_feedback()

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
