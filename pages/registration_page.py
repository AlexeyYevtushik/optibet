from pages.base_page import BasePage


class RegistrationPage(BasePage):
    EMAIL_INPUT = "//*[@data-role='signupEmail']"
    PASSWORD_INPUT = "//*[@data-role='signupPassword']"
    SUBMIT_BUTTON = "button[type='submit']"
    EMAIL_ERROR_MESSAGE = "//*[@data-role='signupEmail']/../../*[@data-role = 'validationError']"
    CHECKBOX_TERMS = "//*[@data-role='tnc-checkbox-input']/.."
    CHECKBOX_PRIVACY = "//*[@data-role='playerAgreement-input']/.."
    CHECKBOX_PROMOTIONS = "//*[@data-role='promotions-checkbox-input']/.."
    VALIDATION_RULE = '//li[@data-role="validation-rule"]'

    def navigate_to_registration(self):
        self.navigate("/en/register")

    def fill_email(self, email):
        self.page.fill(self.EMAIL_INPUT, email)

    def fill_password(self, password):
        self.page.fill(self.PASSWORD_INPUT, password)

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

    def is_submit_button_visible(self):
        return self.is_visible(self.SUBMIT_BUTTON)
    
    def check_checkboxes(self):
        self.page.check(self.CHECKBOX_TERMS)
        self.page.check(self.CHECKBOX_PRIVACY)
        self.page.check(self.CHECKBOX_PROMOTIONS)

    def check_terms_checkbox(self):
        self.page.check(self.CHECKBOX_TERMS)
    
    def check_privacy_checkbox(self):
        self.page.check(self.CHECKBOX_PRIVACY)
    
    def check_promotions_checkbox(self):
        self.page.check(self.CHECKBOX_PROMOTIONS)

    def check_submit_is_active(self):
        return self.page.locator(self.SUBMIT_BUTTON).is_enabled()

    def get_valid_validation_rules_count(self):
        return self.page.locator(self.VALIDATION_RULE).evaluate_all(
            "elements => elements.filter(e => getComputedStyle(e).backgroundColor.replace(/\\s/g, '') === 'rgb(19,193,111)').length"
        )