import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selene import browser

from utils import attach


@pytest.fixture(scope="session", autouse=True)
def browser_settings():
    browser.config.base_url = 'https://demoqa.com'
    browser.config.window_height = 1080
    browser.config.window_width = 1920
    selenoid_login = 'user1'
    selenoid_pass = '1234'
    selenoid_url = 'selenoid.autotests.cloud'

    options = Options()
    selenoid_capabilities = {
        "browserName": "chrome",
        "browserVersion": "100.0",
        "selenoid:options": {
            "enableVNC": True,
            "enableVideo": True
        }
    }

    options.page_load_strategy = 'eager'
    options.capabilities.update(selenoid_capabilities)
    driver = webdriver.Remote(
        command_executor=f"https://{selenoid_login}:{selenoid_pass}@{selenoid_url}/wd/hub",
        options=options)

    browser.config.driver = driver
    yield browser

    attach.add_screenshot(browser)
    attach.add_logs(browser)
    attach.add_html(browser)
    attach.add_video(browser)

    browser.quit()
