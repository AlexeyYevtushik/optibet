from pages.base_page import BasePage
import re


class HeaderPage(BasePage):
    LOGO = "//*[contains(@class,'logo_')]"
    NAVIGATION_ITEMS = "//ul[@data-role='navMainMenu']//a"
    LANGUAGE_SWITCHER = f"//div[contains(@class, 'language-menu____')]"
    ACTIVE_LANGUAGE = "//*[contains(@class,'language-menu__label___')]"
    LOGIN = "//*[@data-role='loginHeaderButton']"
    REGISTER = "//*[@data-role='signupHeaderButton']"


    def is_logo_visible(self):
        return self.is_visible(self.LOGO)

    def get_navigation_menu_items(self):
        # self.wait_for_selector(self.NAVIGATION_ITEMS)
        return self.page.locator(self.NAVIGATION_ITEMS).evaluate_all("elements => elements.map(e => e.getAttribute('href'))")

    def switch_language(self, lang_code):
        self.page.click(f"{self.LANGUAGE_SWITCHER}")
        self.page.click(f"//*[text()='{lang_code}']")

    def get_active_language(self):
        return self.page.locator(self.ACTIVE_LANGUAGE).text_content().strip().lower()
    
    def go_to_login_page(self):
        self.page.click(self.LOGIN)
                        
    def go_to_register_page(self):
        self.page.click(self.REGISTER)