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
        registration_page = RegistrationPage(page)
        registration_page.navigate_to_registration()

        with allure.step(f"Fill form with weak password: {password}"):
            registration_page.fill_email(self.email_for_test)
            registration_page.fill_password(password)
            registration_page.submit()

        with allure.step("Verify password error message"):
            assert error_message in registration_page.get_password_error().lower()

    def test_required_field_empty(self, page):
        registration_page = RegistrationPage(page)
        registration_page.navigate_to_registration()

        with allure.step("Submit form with empty required field"):
            registration_page.submit()

        with allure.step("Verify email error message for required field"):
            assert "is required" in registration_page.get_email_error().lower()
