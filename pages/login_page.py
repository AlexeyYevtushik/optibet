from pages.base_page import BasePage

class LoginPage(BasePage):
    USERNAME_INPUT = "#username"
    PASSWORD_INPUT = "#password"
    LOGIN_BUTTON = "button[type='submit']"
    ERROR_MESSAGE = ".error-message"

    def navigate_to_login(self):
        self.navigate("/en/login")

    def fill_username(self, username):
        self.page.fill(self.USERNAME_INPUT, username)

    def fill_password(self, password):
        self.page.fill(self.PASSWORD_INPUT, password)

    def click_login(self):
        self.page.click(self.LOGIN_BUTTON)

    def get_error_message(self):
        if self.page.locator(self.ERROR_MESSAGE).is_visible():
            return self.page.locator(self.ERROR_MESSAGE).text_content()
        return None
