from playwright.sync_api import expect, Page
from pages.inventory_page import InventoryPage
from pages.product_details import ProductDetailsPage
from urllib.parse import urljoin
from config import BASE_URL
import pytest

pytestmark = pytest.mark.regression

def test_product_details_displayed_correctly(logged_in_page: Page) -> None:
    inventory_page = InventoryPage(logged_in_page)
    inventory_page.open_product_details("Sauce Labs Backpack")

    product_details_page = ProductDetailsPage(logged_in_page)
    expect(product_details_page.get_displayed_product_name()).to_have_text("Sauce Labs Backpack")
    expect(product_details_page.get_displayed_product_description()).not_to_be_empty()
    expect(product_details_page.get_displayed_product_price()).to_have_text("$29.99")
    product_details_page.return_to_inventory_page()

    expect(logged_in_page).to_have_url(urljoin(BASE_URL, "inventory.html"))
    expect(inventory_page.products_header).to_be_visible()

def test_add_remove_product_from_details(logged_in_page: Page) -> None:
    inventory_page = InventoryPage(logged_in_page)
    inventory_page.open_product_details("Sauce Labs Backpack")

    product_details_page = ProductDetailsPage(logged_in_page)
    expect(product_details_page.get_displayed_product_name()).to_have_text("Sauce Labs Backpack")
    product_details_page.add_displayed_product_to_cart()
    expect(product_details_page.cart_badge).to_have_text("1")
    product_details_page.remove_displayed_product_from_cart()
    expect(product_details_page.cart_badge).to_have_count(0)
    expect(product_details_page.add_to_cart_button).to_be_visible()
