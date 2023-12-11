import pytest
from selene.support.shared import browser
from selenium import webdriver


@pytest.fixture(scope='function')
def setup_browser_1920_1080():
    driver_options = webdriver.ChromeOptions()
    driver_options.add_argument('--headless')
    browser.config.driver_options = driver_options

    browser.config.window_width = 1920
    browser.config.window_height = 1080
    browser.config.base_url = "https://doctu.ru"

    yield

    browser.quit()


@pytest.fixture(scope='function')
def setup_browser_974_1080():
    driver_options = webdriver.ChromeOptions()
    driver_options.add_argument('--headless')
    browser.config.driver_options = driver_options

    browser.config.window_width = 960
    browser.config.window_height = 1080
    browser.config.base_url = "https://doctu.ru"

    yield

    browser.quit()


