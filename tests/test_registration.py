import allure
import pytest
from pages.header_page import HeaderPage
from pages.registration_page import RegistrationPage

@allure.feature("Registration")
class TestRegistration:

    @pytest.fixture(autouse=True)
    def setup_data(self):
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

        with allure.step("Verify email error message"):
            assert "įvesk galiojantį el. pašto adresą" in registration_page.get_email_error().lower()

    @pytest.mark.parametrize("password, highlighted_elements_number", [
        ("short", "3"),("testtest", "4"), ("1Aa", "5")])
    def test_weak_password(self, page, password, highlighted_elements_number):
        header_page = HeaderPage(page)
        header_page.navigate("/")
        header_page.go_to_register_page()
        registration_page = RegistrationPage(page)
        
        with allure.step(f"Fill form with weak password: {password}"):
            registration_page.fill_email(self.email_for_test)
            registration_page.fill_password(password)

        with allure.step(f"Verify highlighted validation buttons count:'{highlighted_elements_number}'"):
            buttons_highlighted = registration_page.get_valid_validation_rules_count()
            assert int(highlighted_elements_number) == int(buttons_highlighted), f"Highlighted '{buttons_highlighted}, expected '{highlighted_elements_number}'"

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
