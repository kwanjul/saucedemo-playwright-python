import pytest
from playwright.sync_api import Page, expect
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_information_page import CheckoutInformationPage
from pages.checkout_overview_page import CheckoutOverviewPage
from config import STANDARD_USERNAME, STANDARD_PASSWORD

@pytest.fixture(scope="session", autouse=True)
def configure_test_id(playwright):
    playwright.selectors.set_test_id_attribute("data-test")

@pytest.fixture
def logged_in_page(page: Page) -> Page:
    login_page = LoginPage(page)
    login_page.navigate()
    login_page.login(STANDARD_USERNAME, STANDARD_PASSWORD)

    inventory_page = InventoryPage(page)
    expect(inventory_page.products_header).to_be_visible()
    
    return page

@pytest.fixture
def checkout_information_page(logged_in_page: Page) -> CheckoutInformationPage:
    inventory_page = InventoryPage(logged_in_page)
    inventory_page.add_product_to_cart("Sauce Labs Backpack")
    inventory_page.open_cart()

    cart_page = CartPage(logged_in_page)
    cart_page.proceed_to_checkout()

    checkout_information_page = CheckoutInformationPage(logged_in_page)
    expect(checkout_information_page.checkout_header).to_be_visible()

    return checkout_information_page

@pytest.fixture
def checkout_overview_page(logged_in_page: Page, checkout_information_page: CheckoutInformationPage) -> CheckoutOverviewPage:
    checkout_information_page.enter_customer_information("John", "Smith", "07628")
    checkout_information_page.continue_checkout()

    checkout_overview_page = CheckoutOverviewPage(logged_in_page)
    expect(checkout_overview_page.checkout_overview_header).to_be_visible()

    return checkout_overview_page
