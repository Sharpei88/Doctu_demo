import pytest
from selene.support.shared import browser
from selenium import webdriver

from utils import attach


@pytest.fixture(scope='function')
def setup_browser_1920_1080():
    driver_options = webdriver.ChromeOptions()
    driver_options.add_argument('--headless')
    browser.config.driver_options = driver_options

    browser.config.window_width = 1920
    browser.config.window_height = 1080
    browser.config.base_url = "https://doctu.ru"

    yield browser

    attach.add_html(browser)
    attach.add_logs(browser)
    attach.add_screenshot(browser)
    attach.add_video(browser)

    browser.quit()


@pytest.fixture(scope='function')
def setup_browser_960_1080():
    driver_options = webdriver.ChromeOptions()
    driver_options.add_argument('--headless')
    browser.config.driver_options = driver_options

    browser.config.window_width = 960
    browser.config.window_height = 1080
    browser.config.base_url = "https://doctu.ru"

    yield browser

    attach.add_html(browser)
    attach.add_logs(browser)
    attach.add_screenshot(browser)
    attach.add_video(browser)

    browser.quit()
