import allure
from pages.promotions_page import PromotionsPage
from pages.header_page import HeaderPage


@allure.feature("Promotions")
class TestPromotions:
    @allure.story("Filtering and Content Validation")
    def test_filter_and_validate_promotions(self, page):
        promotions_page = PromotionsPage(page)
        promotions_page.navigate("/")
        header_page = HeaderPage(page)
        header_page.go_to_promotions_page()

        with allure.step("Verify promotion cards are visible"):
            assert promotions_page.are_promotion_cards_visible(), "Promotion cards are not visible"
            
        filters = promotions_page.get_filters()
        for filter_locator in filters:
            filter_name = (filter_locator.text_content() or "").strip()
            with allure.step(f"Apply filter '{filter_name}'"):
                filter_locator.click()
                assert "/promotion/" in page.url
                
