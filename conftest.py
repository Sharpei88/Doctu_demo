import pytest

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selene import browser

from utils import attach


@pytest.fixture(scope='function')
def setup_browser_1920_1080():
    options = Options()
    selenoid_capabilities = {
        "browserName": "chrome",
        "browserVersion": "100.0",
        "selenoid:options": {
            "enableVNC": True,
            "enableVideo": True
        }
    }
    options.capabilities.update(selenoid_capabilities)
    driver = webdriver.Remote(
        command_executor=f"https://user1:1234@selenoid.autotests.cloud/wd/hub",
        options=options
    )

    browser.config.driver = driver
    browser.config.window_width = 1920
    browser.config.window_height = 1080
    browser.config.base_url = "https://doctu.ru"

    yield browser

    attach.add_screenshot(browser)
    attach.add_logs(browser)
    attach.add_html(browser)
    attach.add_video(browser)

    browser.quit()


'''@pytest.fixture(scope='function')
def setup_browser_190_1080():
    driver_options = webdriver.ChromeOptions()
    driver_options.add_argument('--headless')
    browser.config.driver_options = driver_options

    browser.config.window_width = 1920
    browser.config.window_height = 1080
    browser.config.base_url = "https://doctu.ru"

    yield

    browser.quit()
'''


@pytest.fixture(scope='function')
def setup_browser_960_1080():
    options = Options()
    selenoid_capabilities = {
        "browserName": "chrome",
        "browserVersion": "100.0",
        "selenoid:options": {
            "enableVNC": True,
            "enableVideo": True
        }
    }
    options.capabilities.update(selenoid_capabilities)
    driver = webdriver.Remote(
        command_executor=f"https://user1:1234@selenoid.autotests.cloud/wd/hub",
        options=options
    )

    browser.config.driver = driver
    browser.config.window_width = 960
    browser.config.window_height = 1080
    browser.config.base_url = "https://doctu.ru"

    yield browser

    attach.add_screenshot(browser)
    attach.add_logs(browser)
    attach.add_html(browser)
    attach.add_video(browser)

    browser.quit()