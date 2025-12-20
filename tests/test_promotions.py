import allure
from pages.promotions_page import PromotionsPage

@allure.feature("Promotions")
class TestPromotions:
    @allure.story("Filtering and Content Validation")
    def test_filter_and_validate_promotions(self, page):
        promotions_page = PromotionsPage(page)
        promotions_page.navigate("/promotions")
        
        with allure.step("Verify promotion cards are visible"):
            assert promotions_page.are_promotion_cards_visible(), "Promotion cards are not visible"
            
        filters = ["all", "sport", "casino"]
        for f in filters:
            with allure.step(f"Apply filter '{f}'"):
                promotions_page.apply_filter(f)
                
            with allure.step(f"Verify promotions for filter '{f}'"):
                cards = promotions_page.get_promotion_cards()
                if len(cards) > 0:
                    for card in cards:
                        assert promotions_page.get_card_title(card), "Card title is missing"
                        assert promotions_page.get_card_read_more_button(card), "Read more button is missing"
                else:
                    # It's okay if some filters have no promotions, but we should note it.
                    print(f"No promotions found for filter '{f}'")

