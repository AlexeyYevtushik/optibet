import pytest
import allure
import os

def pytest_addoption(parser):
    parser.addoption("--base_url", action="store", help="base URL for the application under test")
    parser.addini("base_url", help="base URL for the application under test", default="https://www.optibet.lt/")

@pytest.fixture
def page(browser, request):
    base_url = request.config.getoption("--base_url") or request.config.getini("base_url")
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