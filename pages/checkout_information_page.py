from playwright.sync_api import Page

class CheckoutInformationPage:

    def __init__(self, page: Page) -> None:
        self.page: Page = page
        self.checkout_header = self.page.get_by_text("Checkout: Your Information", exact=True)
        self.first_name_field = self.page.get_by_test_id("firstName")
        self.last_name_field = self.page.get_by_test_id("lastName")
        self.postal_code_field = self.page.get_by_test_id("postalCode")
        self.continue_button = self.page.get_by_role("button", name="Continue")
        self.cancel_button = self.page.get_by_role("button", name="Cancel")
        self.error_message = self.page.get_by_test_id("error")

    def enter_customer_information(self, first_name: str, last_name: str, postal_code: str) -> None:
        self.first_name_field.fill(first_name)
        self.last_name_field.fill(last_name)
        self.postal_code_field.fill(postal_code)

    def continue_checkout(self) -> None:
        self.continue_button.click()

    def cancel_checkout(self) -> None:
        self.cancel_button.click()
