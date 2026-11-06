from playwright.sync_api import expect, Page
from pages.checkout_information_page import CheckoutInformationPage
from pages.checkout_overview_page import CheckoutOverviewPage
from pages.inventory_page import InventoryPage
from pages.checkout_complete_page import CheckoutCompletePage
import pytest

pytestmark = pytest.mark.regression

def test_order_total_calculation(checkout_overview_page: CheckoutOverviewPage) -> None:
    item_subtotal = checkout_overview_page.get_item_subtotal()
    tax = checkout_overview_page.get_tax_amount()
    order_total = checkout_overview_page.get_order_total()
    assert order_total == round(item_subtotal + tax, 2)

def test_checkout_overview_sections_displayed(checkout_overview_page: CheckoutOverviewPage) -> None:
    assert checkout_overview_page.is_checkout_overview_displayed()
    assert checkout_overview_page.is_payment_information_displayed()
    assert checkout_overview_page.is_price_total_displayed()
    assert checkout_overview_page.is_shipping_information_displayed()

def test_checkout_overview_product_names(checkout_overview_page: CheckoutOverviewPage) -> None:
    product_names = checkout_overview_page.get_product_names()
    assert "Sauce Labs Backpack" in product_names
    assert len(product_names) == 1

def test_checkout_overview_product_quantities(checkout_overview_page: CheckoutOverviewPage) -> None:
    assert checkout_overview_page.get_product_quantities() == [1]

def test_checkout_overview_product_prices(checkout_overview_page: CheckoutOverviewPage) -> None:
    assert checkout_overview_page.get_product_prices() == [29.99]

def test_checkout_overview_item_subtotal(checkout_overview_page: CheckoutOverviewPage) -> None:
    product_prices = checkout_overview_page.get_product_prices()
    total_price = 0
    product_quantities = checkout_overview_page.get_product_quantities()
    for (price, quantity) in zip (product_prices, product_quantities):
        total_price += price * quantity
    assert checkout_overview_page.get_item_subtotal() == total_price

def test_checkout_overview_payment_information(checkout_overview_page: CheckoutOverviewPage) -> None:
    assert checkout_overview_page.get_payment_information() == "SauceCard #31337"

def test_checkout_overview_shipping_information(checkout_overview_page: CheckoutOverviewPage) -> None:
    assert checkout_overview_page.get_shipping_information() == "Free Pony Express Delivery!"

def test_cancel_checkout(checkout_overview_page: CheckoutOverviewPage) -> None:
    checkout_overview_page.cancel_checkout()

    inventory_page = InventoryPage(checkout_overview_page.page)
    expect(inventory_page.products_header).to_be_visible()

def test_finish_checkout(checkout_overview_page: CheckoutOverviewPage) -> None:
    checkout_overview_page.finish_checkout()

    checkout_complete_page = CheckoutCompletePage(checkout_overview_page.page)
    expect(checkout_complete_page.confirmation_heading).to_be_visible()
    expect(checkout_complete_page.order_completion_message).to_have_text("Thank you for your order!")
