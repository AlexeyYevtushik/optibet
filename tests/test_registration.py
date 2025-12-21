import allure
import pytest
from pages.header_page import HeaderPage
from pages.registration_page import RegistrationPage

@allure.feature("Registration")
class TestRegistration:

    def setup_method(self, method):
        self.email_for_test = "testuser@example.com"

    @allure.story("Negative Scenarios")
    def test_invalid_email(self, page):
        header_page = HeaderPage(page)
        header_page.navigate("/")
        header_page.go_to_register_page()
        registration_page = RegistrationPage(page)
       
        with allure.step("Verify presence of main fields"):
            assert registration_page.is_email_field_visible(), "Email field is not visible"
            assert registration_page.is_password_field_visible(), "Password field is not visible"
            assert registration_page.is_submit_button_visible(), "Submit button is not visible"

        with allure.step("Fill form with invalid email"):
            registration_page.fill_email("test_without_at.com")
            registration_page.fill_password("ValidPassword123")
            assert registration_page.check_submit_is_active() == False, "Submit button should be inactive with invalid email"
            # registration_page.check_promotions_checkbox()
            # assert registration_page.check_submit_is_active() == True, "Submit button should be active after checking checkboxes"

        with allure.step("Verify email error message"):
            assert "įvesk galiojantį el. pašto adresą" in registration_page.get_email_error().lower()

    @pytest.mark.parametrize("password, error_message", [
        ("short", "password is too short"),
        ("nouppercase1", "password must contain at least one uppercase letter"),
        ("NOLOWERCASE1", "password must contain at least one lowercase letter"),
        ("NoNumber", "password must contain at least one number"),
    ])
    def test_weak_password(self, page, password, error_message):
        header_page = HeaderPage(page)
        header_page.navigate("/")
        header_page.go_to_register_page()
        registration_page = RegistrationPage(page)
        
        with allure.step(f"Fill form with weak password: {password}"):
            registration_page.fill_email(self.email_for_test)
            registration_page.fill_password(password)

        with allure.step("Verify password error message"):
            assert error_message in registration_page.get_password_error().lower()

        with allure.step(f"Verify validation rule for '{error_message}' is highlighted as invalid"):
            rule_color = registration_page.get_password_rule_background_color(error_message)
            # Assert that the rule color is not the 'valid' color (e.g., green).
            # You may need to adjust 'rgb(18, 156, 74)' to the actual color your app uses for a *valid* rule.
            assert "rgb(18, 156, 74)" not in rule_color, f"Rule '{error_message}' should be shown as invalid, but it is not."

    def test_required_field_empty(self, page):
        header_page = HeaderPage(page)
        header_page.navigate("/")
        header_page.go_to_register_page()
        registration_page = RegistrationPage(page)

        with allure.step("Click on pasword field"):
            registration_page.fill_email("")
            registration_page.fill_password("SomePassword123")

        with allure.step("Verify email error message for required field"):
            assert "privaloma nurodyti teisingą el. pašto adresą" in registration_page.get_email_error().lower()
