from pages.base_page import BasePage
import re


class HeaderPage(BasePage):
    LOGO = ".logo"
    NAVIGATION_ITEMS = "nav.main-menu a"
    LANGUAGE_SWITCHER = f"//div[contains(@class, 'language-menu____')]"
    ACTIVE_LANGUAGE = ".language-switcher .active"


    def is_logo_visible(self):
        return self.is_visible(self.LOGO)

    def get_navigation_menu_items(self):
        self.wait_for_selector(self.NAVIGATION_ITEMS)
        return self.page.locator(self.NAVIGATION_ITEMS).all_text_contents()

    def switch_language(self, lang_code):
        self.page.click(f"{self.LANGUAGE_SWITCHER}")
        self.page.click(f"//*[text()='{lang_code}']")

    def get_active_language(self):
        return self.page.locator(self.ACTIVE_LANGUAGE).text_content().strip().lower()