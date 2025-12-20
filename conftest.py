import pytest
from playwright.sync_api import sync_playwright
import allure
import os

def pytest_addoption(parser):
    parser.addoption("--base_url", action="store", default="https://www.optibet.lv/", help="base URL for the application under test")
    parser.addoption("--headless", action="store_true", default=False, help="run tests in headless mode")

@pytest.fixture(scope="session")
def browser(request):
    headless = request.config.getoption("--headless")
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=headless)
        yield browser
        browser.close()

@pytest.fixture
def page(browser, request):
    base_url = request.config.getoption("--base_url")
    page = browser.new_page(base_url=base_url)
    yield page
    page.close()

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    if rep.when == "call" and rep.failed:
        if "page" in item.funcargs:
            page = item.funcargs["page"]
            screenshot_dir = "allure-results/screenshots"
            if not os.path.exists(screenshot_dir):
                os.makedirs(screenshot_dir)
            screenshot_path = os.path.join(screenshot_dir, f"{item.nodeid.replace('::', '_')}.png")
            page.screenshot(path=screenshot_path)
            allure.attach.file(screenshot_path, name="screenshot", attachment_type=allure.attachment_type.PNG)