from playwright.sync_api import Page

class CheckoutOverviewPage:

    def __init__(self, page: Page) -> None:
        self.page: Page = page
        self.checkout_overview_header = self.page.get_by_text("Checkout: Overview", exact=True)
        self.payment_information_label = self.page.get_by_text("Payment Information:", exact=True)
        self.shipping_information_label = self.page.get_by_text("Shipping Information:", exact=True)
        self.price_total_label = self.page.get_by_text("Price Total", exact=True)
        self.cancel_button = self.page.get_by_role("button", name="Cancel")
        self.finish_button = self.page.get_by_role("button", name="Finish")

    def is_checkout_overview_displayed(self) -> bool:
        return self.checkout_overview_header.is_visible()

    def is_payment_information_displayed(self) -> bool:
        return self.payment_information_label.is_visible()

    def is_shipping_information_displayed(self) -> bool:
        return self.shipping_information_label.is_visible()

    def is_price_total_displayed(self) -> bool:
        return self.price_total_label.is_visible()

    def get_item_subtotal(self) -> float:
        return float(self.page.get_by_test_id("subtotal-label").text_content().replace("Item total: $",""))

    def get_tax_amount(self) -> float:
        return float(self.page.get_by_test_id("tax-label").text_content().replace("Tax: $",""))

    def get_order_total(self) -> float:
        return float(self.page.get_by_test_id("total-label").text_content().replace("Total: $",""))

    def get_product_names(self) -> list[str]:
        return self.page.get_by_test_id("inventory-item-name").all_inner_texts()

    def get_product_quantities(self) -> list[int]:
        return [int(value) for value in self.page.get_by_test_id("item-quantity").all_inner_texts()]

    def get_product_prices(self) -> list[float]:
        return [float(value.replace("$","")) for value in self.page.get_by_test_id("inventory-item-price").all_inner_texts()]

    def get_payment_information(self) -> str:
        return self.page.get_by_test_id("payment-info-value").inner_text()

    def get_shipping_information(self) -> str:
        return self.page.get_by_test_id("shipping-info-value").inner_text()

    def cancel_checkout(self) -> None:
        self.cancel_button.click()
    
    def finish_checkout(self) -> None:
        self.finish_button.click()
