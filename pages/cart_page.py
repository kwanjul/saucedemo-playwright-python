from playwright.sync_api import Page

class CartPage:

    def __init__(self, page: Page) -> None:
        self.page: Page = page
        self.cart_header = self.page.get_by_text("Your Cart", exact=True)
        self.continue_shopping_button = self.page.get_by_role("button", name="Continue Shopping")
        self.checkout_button = self.page.get_by_role("button", name="Checkout")
        self.cart_badge = self.page.locator(".shopping_cart_badge")

    def get_cart_item_count(self) -> int:
        return self.page.locator(".inventory_item_name").count()

    def get_cart_product_names(self) -> list[str]:
        return self.page.locator(".inventory_item_name").all_text_contents()

    def continue_shopping(self) -> None:
        self.continue_shopping_button.click()

    def remove_product_from_cart(self, product_name: str) -> None:
        self.page.locator(".cart_item").filter(has_text=product_name).get_by_role("button", name="Remove").click()

    def proceed_to_checkout(self) -> None:
        self.checkout_button.click()
        