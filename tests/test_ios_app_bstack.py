import allure
import pytest
from appium.webdriver.common.appiumby import AppiumBy
from selene import browser, have

from src.utils.config import config


@pytest.mark.skipif(config.is_local or config.platform_name.lower() != 'ios', reason="iOS specific test")
def test_ios_sample_app():
    with allure.step('Click Text Button'):
        browser.element((AppiumBy.ACCESSIBILITY_ID, "Text Button")).click()

    with allure.step('Type text input'):
        browser.element((AppiumBy.ACCESSIBILITY_ID, "Text Input")).type('Hello Appium!').press_enter()

    with allure.step('Verify text output'):
        browser.element((AppiumBy.ACCESSIBILITY_ID, "Text Output")).should(have.text('Hello Appium!'))
