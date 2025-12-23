import allure

class BasePage:
    def __init__(self, page):
        self.page = page

    @allure.step("Opening page {url}")
    def navigate(self, url):
        self.page.goto(url, wait_until="commit")

        # Handle the LV -> LT redirect link if it appears
        self.page.wait_for_selector("#CybotCookiebotDialogBodyLevelButtonLevelOptinAllowAll", state="visible", timeout=5000)

        # Handle Cookiebot consent dialog if it appears
        cookie_button = self.page.locator("#CybotCookiebotDialogBodyLevelButtonLevelOptinAllowAll")
        try:
            cookie_button.wait_for(state="visible", timeout=5000)
            cookie_button.click()
        except Exception:
            pass # Cookie banner didn't appear, continue


        # lt_link = self.page.locator('a[href="https://www.optibet.lt"]')
        # try:
        #     lt_link.wait_for(state="visible", timeout=1500)
        #     lt_link.click()
        # except Exception:
        #     pass # Link didn't appear, continue

        # self.page.wait_for_selector("#CybotCookiebotDialogBodyLevelButtonLevelOptinAllowAll", state="visible", timeout=5000)
        # # Handle Cookiebot consent dialog if it appears
        # cookie_button = self.page.locator("#CybotCookiebotDialogBodyLevelButtonLevelOptinAllowAll")
        # try:
        #     cookie_button.wait_for(state="visible", timeout=5000)
        #     cookie_button.click()
        # except Exception:
        #     pass # Cookie banner didn't appear, continue
        # # Handle Cookiebot consent dialog if it appears

    def is_visible(self, selector: str) -> bool:
        return self.page.locator(selector).is_visible()

    def wait_for_selector(self, selector: str):
        self.page.locator(selector).wait_for()
