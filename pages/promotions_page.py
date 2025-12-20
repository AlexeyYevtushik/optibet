from pages.base_page import BasePage
from playwright.sync_api import Locator
from typing import List


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
        # It's a good practice to wait for the content to update after filtering
        self.page.wait_for_load_state("networkidle")

    def get_promotion_cards(self) -> List[Locator]:
        return self.page.locator(self.PROMOTION_CARDS).all()

    def get_card_title(self, card: Locator) -> str:
        return card.locator(self.PROMO_TITLE).text_content()

    def get_card_read_more_button(self, card: Locator) -> Locator:
        # This makes the check more robust by ensuring the button exists within the card
        button = card.locator(self.READ_MORE_BUTTON)
        button.wait_for(state="visible", timeout=1000) # Wait up to 1s for visibility
        return button
