from playwright.sync_api import expect, Page
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_information_page import CheckoutInformationPage

def test_checkout_with_valid_information(page: Page) -> None:
    login_page = LoginPage(page)
    login_page.navigate()
    login_page.login("standard_user", "secret_sauce")

    inventory_page = InventoryPage(page)
    inventory_page.add_product_to_cart("Sauce Labs Backpack")
    inventory_page.open_cart()

    cart_page = CartPage(page)
    cart_page.proceed_to_checkout()

    checkout_information_page = CheckoutInformationPage(page)
    expect(checkout_information_page.checkout_header).to_be_visible()
    checkout_information_page.enter_customer_information("John", "Smith", "07628")
    checkout_information_page.continue_checkout()

    expect(page).to_have_url("https://www.saucedemo.com/checkout-step-two.html")
    expect(page.get_by_text("Checkout: Overview", exact=True)).to_be_visible()

def test_checkout_missing_first_name(page: Page) -> None:
    login_page = LoginPage(page)
    login_page.navigate()
    login_page.login("standard_user", "secret_sauce")

    inventory_page = InventoryPage(page)
    inventory_page.add_product_to_cart("Sauce Labs Backpack")
    inventory_page.open_cart()

    cart_page = CartPage(page)
    cart_page.proceed_to_checkout()

    checkout_information_page = CheckoutInformationPage(page)
    expect(checkout_information_page.checkout_header).to_be_visible()
    checkout_information_page.enter_customer_information("", "Smith", "07628")
    checkout_information_page.continue_checkout()
    expect(checkout_information_page.error_message).to_have_text("Error: First Name is required")
    expect(page).to_have_url("https://www.saucedemo.com/checkout-step-one.html")

def test_checkout_missing_last_name(page: Page) -> None:
    login_page = LoginPage(page)
    login_page.navigate()
    login_page.login("standard_user", "secret_sauce")

    inventory_page = InventoryPage(page)
    inventory_page.add_product_to_cart("Sauce Labs Backpack")
    inventory_page.open_cart()

    cart_page = CartPage(page)
    cart_page.proceed_to_checkout()

    checkout_information_page = CheckoutInformationPage(page)
    expect(checkout_information_page.checkout_header).to_be_visible()
    checkout_information_page.enter_customer_information("Dean", "", "07628")
    checkout_information_page.continue_checkout()
    expect(checkout_information_page.error_message).to_have_text("Error: Last Name is required")
    expect(page).to_have_url("https://www.saucedemo.com/checkout-step-one.html")

def test_checkout_missing_postal_code(page: Page) -> None:
    login_page = LoginPage(page)
    login_page.navigate()
    login_page.login("standard_user", "secret_sauce")

    inventory_page = InventoryPage(page)
    inventory_page.add_product_to_cart("Sauce Labs Backpack")
    inventory_page.open_cart()

    cart_page = CartPage(page)
    cart_page.proceed_to_checkout()

    checkout_information_page = CheckoutInformationPage(page)
    expect(checkout_information_page.checkout_header).to_be_visible()
    checkout_information_page.enter_customer_information("Dean", "Johnson", "")
    checkout_information_page.continue_checkout()
    expect(checkout_information_page.error_message).to_have_text("Error: Postal Code is required")
    expect(page).to_have_url("https://www.saucedemo.com/checkout-step-one.html")
