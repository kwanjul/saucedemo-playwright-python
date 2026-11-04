from playwright.sync_api import Page, Locator

class InventoryPage:

    def __init__(self, page: Page) -> None:
        self.page: Page = page
        self.products_header = self.page.get_by_text("Products", exact=True)
        self.sort_by_dropdown = self.page.locator(".product_sort_container")
        self.cart_badge = self.page.locator(".shopping_cart_badge")

    def get_inventory_items(self) -> Locator:
        return self.page.locator(".inventory_item")

    def get_product_names(self) -> list[str]:
        return self.page.locator(".inventory_item_name").all_text_contents()

    def get_product_name_elements(self) -> Locator:
        return self.page.locator(".inventory_item_name")

    def sort_products(self, sort_option: str) -> None:
        self.sort_by_dropdown.select_option(label=sort_option)

    def get_product_prices(self) -> list[float]:
        inventory_item_price = self.page.locator(".inventory_item_price").all_text_contents()
        return [float(price_text.replace("$", "")) for price_text in inventory_item_price]

    def get_product_price_elements(self) -> Locator:
        return self.page.locator(".inventory_item_price")

    def add_product_to_cart(self, product_name: str) -> None:
        self.page.locator(".inventory_item").filter(has_text=product_name).locator("button").click()

    def remove_product_from_cart(self, product_name: str) -> None:
        self.page.locator(".inventory_item").filter(has_text=product_name).get_by_role("button", name="Remove").click()

    def open_cart(self) -> None:
        self.page.get_by_test_id("shopping-cart-link").click()

    def open_product_details(self, product_name: str) -> None:
        self.page.get_by_text(product_name, exact=True).click()
