import allure
from pages.login_page import LoginPage
from pages.header_page import HeaderPage

@allure.feature("Login")
class TestLogin:

    @allure.story("Negative Scenarios")
    def test_invalid_login(self, page):
        header_page = HeaderPage(page)
        header_page.navigate("/")
        header_page.go_to_login_page()
        login_page = LoginPage(page)

        with allure.step("Fill login form with non-existent credentials"):
            login_page.fill_username("test@test.ru")
            login_page.fill_password("invalidpassword")
            login_page.click_login()

        with allure.step("Verify error message"):
            assert login_page.get_error_message() is not None
            assert "oi, kažkas nutiko! :(" in login_page.get_error_message().lower()

