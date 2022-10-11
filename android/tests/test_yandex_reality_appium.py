import allure
from allure_commons._allure import step
from appium.webdriver.common.appiumby import AppiumBy
from selene import have, be
from selene.support.shared import browser

from android.tests.conftest import driver_management


@allure.tag('Appium mobile diploma')
@allure.title('Yandex reality change cart to list test')
def test_change_cart_to_list():
    new_browser = driver_management
    browser.config._timeout = 15

    with step('Pass first screen'):
        browser.element((AppiumBy.ID, "com.yandex.mobile.realty:id/closeButton")) \
            .click()

    with step('Change cart to list'):
        browser.element((AppiumBy.ID, 'com.yandex.mobile.realty:id/modeButton')) \
            .click()


@allure.title('Yandex reality sort by price for m2 test')
def test_sort_by_price():
    test_change_cart_to_list()

    with step('Click by sorting'):
        browser.element((AppiumBy.ID, 'com.yandex.mobile.realty:id/labelView')) \
            .click()

    with step('Choose sorting by price ascending'):
        browser.element((AppiumBy.XPATH, '//*[android.widget.RadioButton[2]]')) \
            .click()

    with step('Assert text'):
        browser.element((AppiumBy.ID, 'com.yandex.mobile.realty:id/labelView')) \
            .should(have.exact_text('цена за м² по возрастанию'))


@allure.title('Yandex reality switch filter to all reality')
def test_switch_filter_to_all_reality_button():
    test_change_cart_to_list()

    with step('Click filter button'):
        browser.element((AppiumBy.ID, 'com.yandex.mobile.realty:id/filtersButton')) \
            .click()

    with step('Click all button'):
        browser.element((AppiumBy.XPATH, '//android.widget.CompoundButton[@index="0"]')) \
            .click()

    with step('Show reality results button'):
        browser.element((AppiumBy.ID, 'com.yandex.mobile.realty:id/submitButton')) \
            .click()

    with step('Assert results'):
        browser.element((AppiumBy.ID, 'com.yandex.mobile.realty:id/snippet')) \
            .should(be.visible)


@allure.title('Yandex reality add to favorites test')
def test_add_to_favorites():
    test_change_cart_to_list()

    with step('Click by add to favorite button'):
        browser.element((AppiumBy.ID, 'com.yandex.mobile.realty:id/snippet_fav')) \
            .click()

    with step('Go to favorite page'):
        browser.element((AppiumBy.ID, 'com.yandex.mobile.realty:id/action_favorite')) \
            .click()

    with step('Assert results'):
        browser.element((AppiumBy.ID, 'com.yandex.mobile.realty:id/login')) \
            .should(be.visible)


@allure.title('Yandex reality check settings test')
def test_check_settings():
    test_change_cart_to_list()

    with step('Click profile button'):
        browser.element((AppiumBy.ID, 'com.yandex.mobile.realty:id/action_extra')) \
            .click()

    with step('Go to settings page'):
        browser.element((AppiumBy.XPATH, '//android.view.ViewGroup[@index="4"]')) \
            .click()

    with step('Go to About app page'):
        browser.element((AppiumBy.XPATH, '//android.widget.TextView[@index="18"]')) \
            .click()

    with step('Assert results'):
        browser.element((AppiumBy.XPATH, '//android.widget.TextView[@index="1"]')) \
            .should(have.text('О приложении'))
