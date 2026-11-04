from playwright.sync_api import expect, Page
from pages.checkout_information_page import CheckoutInformationPage
from urllib.parse import urljoin
from config import BASE_URL

def test_checkout_with_valid_information(
    logged_in_page: Page,
    checkout_information_page: CheckoutInformationPage
) -> None:
    checkout_information_page.enter_customer_information("John", "Smith", "07628")
    checkout_information_page.continue_checkout()

    expect(logged_in_page).to_have_url(urljoin(BASE_URL, "checkout-step-two.html"))
    expect(logged_in_page.get_by_text("Checkout: Overview", exact=True)).to_be_visible()

def test_checkout_missing_first_name(
    logged_in_page: Page,
    checkout_information_page: CheckoutInformationPage
) -> None:
    checkout_information_page.enter_customer_information("", "Smith", "07628")
    checkout_information_page.continue_checkout()
    expect(checkout_information_page.error_message).to_have_text("Error: First Name is required")
    expect(logged_in_page).to_have_url(urljoin(BASE_URL, "checkout-step-one.html"))

def test_checkout_missing_last_name(
    logged_in_page: Page,
    checkout_information_page: CheckoutInformationPage
) -> None:
    checkout_information_page.enter_customer_information("Dean", "", "07628")
    checkout_information_page.continue_checkout()
    expect(checkout_information_page.error_message).to_have_text("Error: Last Name is required")
    expect(logged_in_page).to_have_url(urljoin(BASE_URL, "checkout-step-one.html"))

def test_checkout_missing_postal_code(
    logged_in_page: Page,
    checkout_information_page: CheckoutInformationPage
) -> None:
    checkout_information_page.enter_customer_information("Dean", "Johnson", "")
    checkout_information_page.continue_checkout()
    expect(checkout_information_page.error_message).to_have_text("Error: Postal Code is required")
    expect(logged_in_page).to_have_url(urljoin(BASE_URL, "checkout-step-one.html"))
