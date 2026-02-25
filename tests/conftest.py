import allure_commons
import pytest
from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.options.ios import XCUITestOptions
from selene import browser, support

from src.utils.allure import attach_video_from_browserstack
from src.utils.config import config


@pytest.fixture(autouse=True)
def mobile_management():
    if config.platform_name.lower() == "ios":
        options = XCUITestOptions()
    else:
        options = UiAutomator2Options()

    capabilities = {
        "platformName": config.platform_name,
        "platformVersion": config.platform_version,
        "deviceName": config.device_name,
        "appium:app": config.appium_app,
        "appium:automationName": config.appium_automation_name,
    }

    if config.app_package:
        capabilities["appium:appPackage"] = config.app_package
    if config.app_activity:
        capabilities["appium:appActivity"] = config.app_activity

    if config.is_bstack:
        capabilities['bstack:options'] = config.bstack_options

    options.load_capabilities(capabilities)

    browser.config.driver = webdriver.Remote(config.remote_url, options=options)

    browser.config._wait_decorator = support._logging.wait_with(
        context=allure_commons._allure.StepContext
    )

    yield

    browser.quit()

    if config.is_bstack:
        attach_video_from_browserstack()
