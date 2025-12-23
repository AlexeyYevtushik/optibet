from pages.base_page import BasePage


class PromotionsPage(BasePage):
    PROMOTION_CARDS = "//*[contains(@class,'promotion-preview___')]"
    FILTER_BUTTONS = "//*[@data-role='tags']/*[contains(@class, 'header-extender__promotions-tag-button___')]"
    
    # PROMO_TITLE = ".promo-title"
    # READ_MORE_BUTTON = ".read-more"


    def are_promotion_cards_visible(self):
        self.wait_for_selector(self.PROMOTION_CARDS)
        return self.is_visible(self.PROMOTION_CARDS)

    def get_filters(self):
        self.wait_for_selector(self.FILTER_BUTTONS)
        return self.page.locator(self.FILTER_BUTTONS).all()

    def get_promotion_cards(self):
        return self.page.locator(self.PROMOTION_CARDS).all()
