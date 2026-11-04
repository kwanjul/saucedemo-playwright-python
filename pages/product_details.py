from playwright.sync_api import Page, Locator

class ProductDetailsPage:

    def __init__(self, page: Page) -> None:
        self.page: Page = page
        self.cart_badge = self.page.locator(".shopping_cart_badge")
        self.add_to_cart_button = self.page.locator("#add-to-cart")

    def get_displayed_product_name(self) -> Locator:
        return self.page.locator(".inventory_details_name")

    def get_displayed_product_description(self) -> Locator:
        return self.page.get_by_test_id("inventory-item-desc")

    def get_displayed_product_price(self) -> Locator:
        return self.page.locator(".inventory_details_price")

    def add_displayed_product_to_cart(self) -> None:
        self.add_to_cart_button.click()

    def remove_displayed_product_from_cart(self) -> None:
        self.page.locator("#remove").click()

    def return_to_inventory_page(self) -> None:
        self.page.locator("#back-to-products").click()
