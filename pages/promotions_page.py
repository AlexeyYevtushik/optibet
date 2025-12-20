from pages.base_page import BasePage


class PromotionsPage(BasePage):
    PROMOTION_CARDS = ".promotion-card"
    FILTER_BUTTONS = ".filters"
    PROMO_TITLE = ".promo-title"
    READ_MORE_BUTTON = ".read-more"


    def are_promotion_cards_visible(self):
        self.wait_for_selector(self.PROMOTION_CARDS)
        return self.is_visible(self.PROMOTION_CARDS)

    def apply_filter(self, filter_name):
        self.page.click(f"{self.FILTER_BUTTONS} [data-filter='{filter_name}']")

    def get_promotion_cards(self):
        return self.page.locator(self.PROMOTION_CARDS).all()

    def get_card_title(self, card):
        return card.locator(self.PROMO_TITLE).text_content()

    def get_card_read_more_button(self, card):
        return card.locator(self.READ_MORE_BUTTON)
