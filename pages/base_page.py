import allure

class BasePage:
    def __init__(self, page):
        self.page = page

    @allure.step("Opening page {url}")
    def navigate(self, url: str):
        self.page.goto(url)

    def wait_for_selector(self, selector: str):
        self.page.wait_for_selector(selector)

    def is_visible(self, selector: str) -> bool:
        return self.page.is_visible(selector)
