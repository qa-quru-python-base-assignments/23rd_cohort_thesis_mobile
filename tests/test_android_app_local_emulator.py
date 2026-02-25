import allure
import pytest
from appium.webdriver.common.appiumby import AppiumBy
from selene import browser, have

from src.utils.config import config


@pytest.mark.skipif(config.is_bstack or config.platform_name.lower() == 'ios', reason="Android specific test")
def test_wikipedia_onboarding():
    with allure.step('Onboarding Screen 1'):
        browser.element(
            (AppiumBy.ID, 'org.wikipedia.alpha:id/primaryTextView')
        ).should(have.text('The Free Encyclopedia'))
        browser.element(
            (AppiumBy.ID, 'org.wikipedia.alpha:id/fragment_onboarding_forward_button')
        ).click()

    with allure.step('Onboarding Screen 2'):
        browser.element(
            (AppiumBy.ID, 'org.wikipedia.alpha:id/primaryTextView')
        ).should(have.text('New ways to explore'))
        browser.element(
            (AppiumBy.ID, 'org.wikipedia.alpha:id/fragment_onboarding_forward_button')
        ).click()

    with allure.step('Onboarding Screen 3'):
        browser.element(
            (AppiumBy.ID, 'org.wikipedia.alpha:id/primaryTextView')
        ).should(have.text('Reading lists with sync'))
        browser.element(
            (AppiumBy.ID, 'org.wikipedia.alpha:id/fragment_onboarding_forward_button')
        ).click()

    with allure.step('Onboarding Screen 4'):
        browser.element(
            (AppiumBy.ID, 'org.wikipedia.alpha:id/primaryTextView')
        ).should(have.text('Data & Privacy'))
        browser.element(
            (AppiumBy.ID, 'org.wikipedia.alpha:id/fragment_onboarding_done_button')
        ).click()
