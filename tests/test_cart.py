from playwright.sync_api import expect, Page
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from urllib.parse import urljoin
from config import BASE_URL
import pytest

pytestmark = pytest.mark.regression

def test_cart_displays_added_products(logged_in_page: Page) -> None:
    inventory_page = InventoryPage(logged_in_page)
    inventory_page.add_product_to_cart("Sauce Labs Backpack")
    inventory_page.add_product_to_cart("Sauce Labs Bike Light")
    inventory_page.add_product_to_cart("Sauce Labs Onesie")
    inventory_page.open_cart()

    cart_page = CartPage(logged_in_page)
    expect(cart_page.cart_header).to_be_visible()
    expect(cart_page.get_cart_items()).to_have_count(3)

    expected_products = {
        "Sauce Labs Backpack", 
        "Sauce Labs Bike Light", 
        "Sauce Labs Onesie" 
    }
    assert set(cart_page.get_cart_product_names()) == expected_products

def test_continue_shopping(logged_in_page: Page) -> None:
    inventory_page = InventoryPage(logged_in_page)
    inventory_page.add_product_to_cart("Sauce Labs Backpack")
    inventory_page.add_product_to_cart("Sauce Labs Bike Light")
    inventory_page.open_cart()

    cart_page = CartPage(logged_in_page)
    expect(cart_page.cart_header).to_be_visible()
    expect(cart_page.get_cart_items()).to_have_count(2)
    cart_page.continue_shopping()

    expect(logged_in_page).to_have_url(urljoin(BASE_URL, "inventory.html"))
    expect(inventory_page.products_header).to_be_visible()
    expect(inventory_page.cart_badge).to_have_text("2")

def test_remove_products_from_cart(logged_in_page: Page) -> None:
    inventory_page = InventoryPage(logged_in_page)
    inventory_page.add_product_to_cart("Sauce Labs Backpack")
    inventory_page.add_product_to_cart("Sauce Labs Bike Light")
    inventory_page.add_product_to_cart("Sauce Labs Onesie")
    inventory_page.open_cart()

    cart_page = CartPage(logged_in_page)
    expect(cart_page.cart_header).to_be_visible()
    expect(cart_page.cart_badge).to_have_text("3")
    expect(cart_page.get_cart_items()).to_have_count(3)
    cart_page.remove_product_from_cart("Sauce Labs Bike Light")
    expect(cart_page.cart_badge).to_have_text("2")
    expect(cart_page.get_cart_items()).to_have_count(2)
    cart_page.remove_product_from_cart("Sauce Labs Backpack")
    expect(cart_page.cart_badge).to_have_text("1")
    expect(cart_page.get_cart_items()).to_have_count(1)
    cart_page.remove_product_from_cart("Sauce Labs Onesie")
    expect(cart_page.cart_badge).to_have_count(0)
    expect(cart_page.get_cart_items()).to_have_count(0)
    assert cart_page.get_cart_product_names() == []
