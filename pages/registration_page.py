from pages.base_page import BasePage


class RegistrationPage(BasePage):
    EMAIL_INPUT = "#email"
    PASSWORD_INPUT = "#password"
    CONFIRM_PASSWORD_INPUT = "#confirm_password"
    SUBMIT_BUTTON = "button[type='submit']"
    EMAIL_ERROR_MESSAGE = ".email-error-message"
    PASSWORD_ERROR_MESSAGE = ".password-error-message"

    def navigate_to_registration(self):
        self.navigate("/en/register")

    def fill_email(self, email):
        self.page.fill(self.EMAIL_INPUT, email)

    def fill_password(self, password):
        self.page.fill(self.PASSWORD_INPUT, password)

    def fill_confirm_password(self, password):
        self.page.fill(self.CONFIRM_PASSWORD_INPUT, password)

    def submit(self):
        self.page.click(self.SUBMIT_BUTTON)

    def get_email_error(self):
        if self.page.locator(self.EMAIL_ERROR_MESSAGE).is_visible():
            return self.page.locator(self.EMAIL_ERROR_MESSAGE).text_content()
        return None

    def get_password_error(self):
        if self.page.locator(self.PASSWORD_ERROR_MESSAGE).is_visible():
            return self.page.locator(self.PASSWORD_ERROR_MESSAGE).text_content()
        return None

    def is_email_field_visible(self):
        return self.is_visible(self.EMAIL_INPUT)

    def is_password_field_visible(self):
        return self.is_visible(self.PASSWORD_INPUT)

    def is_confirm_password_field_visible(self):
        return self.is_visible(self.CONFIRM_PASSWORD_INPUT)

    def is_submit_button_visible(self):
        return self.is_visible(self.SUBMIT_BUTTON)
