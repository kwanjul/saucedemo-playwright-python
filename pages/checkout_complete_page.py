from playwright.sync_api import Page

class CheckoutCompletePage:

    def __init__(self, page: Page) -> None:
        self.page: Page = page
        self.confirmation_heading = self.page.get_by_text("Checkout: Complete!", exact=True)
        self.order_completion_message = self.page.get_by_test_id("complete-header")

    def is_checkout_complete_displayed(self) -> bool:
        return self.confirmation_heading.is_visible()
