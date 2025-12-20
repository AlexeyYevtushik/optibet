import allure
import pytest
from pages.header_page import HeaderPage

@allure.feature("Header")
class TestHeader:
    @allure.story("Logo and Navigation")
    def test_logo_and_navigation(self, page):
        header_page = HeaderPage(page)
        header_page.navigate("/")

        with allure.step("Verify logo is visible"):
            assert header_page.is_logo_visible(), "Logo is not visible"
            
        with allure.step("Verify navigation menu items"):
            expected_items = ["SPORTS", "LIVE BETTING", "CASINO", "LIVE CASINO", "OFFERS"]
            actual_items = header_page.get_navigation_menu_items()
            assert set(expected_items).issubset(set(actual_items)), f"Navigation items do not match. Expected: {expected_items}, Actual: {actual_items}"

    @allure.story("Language Switcher")
    @pytest.mark.parametrize("lang_code, expected_url_part", [("ru", "/ru"), ("en", "/en"), ("lt", "")])
    def test_language_switcher(self, page, lang_code, expected_url_part):
        header_page = HeaderPage(page)
        header_page.navigate("/")
        
        with allure.step(f"Switch language to {lang_code}"):
            header_page.switch_language(lang_code)
            
        with allure.step(f"Verify URL and active language for {lang_code}"):
            assert expected_url_part in page.url, f"URL does not contain {expected_url_part}"
            assert header_page.get_active_language() == lang_code, f"Active language is not {lang_code}"

    @allure.story("Language Switcher Roundtrip")
    def test_language_switcher_roundtrip(self, page):
        header_page = HeaderPage(page)
        header_page.navigate("/")

        with allure.step("Switch language from RU to LV"):
            header_page.switch_language("lv")
            assert "/lv/" in page.url, "URL does not contain /lv/ after switching to LV"
            assert header_page.get_active_language() == "lv", "Active language is not LV"

        with allure.step("Switch language from LV back to RU"):
            header_page.switch_language("ru")
            assert "/ru/" in page.url, "URL does not contain /ru/ after switching back to RU"
            assert header_page.get_active_language() == "ru", "Active language is not RU"
