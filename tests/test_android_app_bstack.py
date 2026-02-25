import allure
import pytest
from appium.webdriver.common.appiumby import AppiumBy
from selene import browser, have

from src.utils.config import config


@pytest.mark.skipif(config.is_local and config.platform_name.lower() == 'ios', reason="Android specific test")
def test_wikipedia_search():
    with allure.step('Type search'):
        browser.element((AppiumBy.ACCESSIBILITY_ID, "Search Wikipedia")).click()
        browser.element((AppiumBy.ID, "org.wikipedia.alpha:id/search_src_text")).type('Appium')

    with allure.step('Verify content found'):
        results = browser.all((AppiumBy.ID, 'org.wikipedia.alpha:id/page_list_item_title'))
        results.should(have.size_greater_than(0))
        results.first.should(have.text('Appium'))


@pytest.mark.skipif(config.is_local and config.platform_name.lower() == 'ios', reason="Android specific test")
def test_open_article():
    with allure.step('Type search'):
        browser.element((AppiumBy.ACCESSIBILITY_ID, "Search Wikipedia")).click()
        browser.element((AppiumBy.ID, "org.wikipedia.alpha:id/search_src_text")).type('Python')

    with allure.step('Verify content found'):
        results = browser.all((AppiumBy.ID, 'org.wikipedia.alpha:id/page_list_item_title'))
        results.should(have.size_greater_than(0))

    with allure.step('Open first article'):
        results.first.click()
