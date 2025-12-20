from pages.base_page import BasePage


class HeaderPage(BasePage):
    LOGO = "a.logo"
    NAVIGATION_MENU = "[data-test-id='main-navigation']"  # Assuming a more stable selector
    LANGUAGE_SWITCHER = ".language-switcher"  # Assuming a class for the language switcher


    def is_logo_visible(self):
        return self.is_visible(self.LOGO)

    def get_navigation_menu_items(self):
        return self.page.locator(f"{self.NAVIGATION_MENU} > li > a").all_text_contents()

    def switch_language(self, language_code):
        self.page.click(f"{self.LANGUAGE_SWITCHER} [data-lang='{language_code}']")

    def get_active_language(self):
        return self.page.locator(f"{self.LANGUAGE_SWITCHER} .active").get_attribute("data-lang")
