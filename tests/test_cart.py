from playwright.sync_api import expect, Page
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage

def test_cart_displays_added_products(page: Page) -> None:
    login_page = LoginPage(page)
    login_page.navigate()
    login_page.login("standard_user", "secret_sauce")

    inventory_page = InventoryPage(page)
    inventory_page.add_product_to_cart("Sauce Labs Backpack")
    inventory_page.add_product_to_cart("Sauce Labs Bike Light")
    inventory_page.add_product_to_cart("Sauce Labs Onesie")
    inventory_page.open_cart()

    cart_page = CartPage(page)
    expect(cart_page.cart_header).to_be_visible()
    assert cart_page.get_cart_item_count() == 3

    expected_products = {
        "Sauce Labs Backpack", 
        "Sauce Labs Bike Light", 
        "Sauce Labs Onesie" 
    }
    assert set(cart_page.get_cart_product_names()) == expected_products

def test_continue_shopping(page: Page) -> None:
    login_page = LoginPage(page)
    login_page.navigate()
    login_page.login("standard_user", "secret_sauce")

    inventory_page = InventoryPage(page)
    inventory_page.add_product_to_cart("Sauce Labs Backpack")
    inventory_page.add_product_to_cart("Sauce Labs Bike Light")
    inventory_page.open_cart()

    cart_page = CartPage(page)
    expect(cart_page.cart_header).to_be_visible()
    assert cart_page.get_cart_item_count() == 2
    cart_page.continue_shopping()

    expect(page).to_have_url("https://www.saucedemo.com/inventory.html")
    expect(inventory_page.products_header).to_be_visible()
    expect(inventory_page.cart_badge).to_have_text("2")

def test_remove_products_from_cart(page: Page) -> None:
    login_page = LoginPage(page)
    login_page.navigate()
    login_page.login("standard_user", "secret_sauce")

    inventory_page = InventoryPage(page)
    inventory_page.add_product_to_cart("Sauce Labs Backpack")
    inventory_page.add_product_to_cart("Sauce Labs Bike Light")
    inventory_page.add_product_to_cart("Sauce Labs Onesie")
    inventory_page.open_cart()

    cart_page = CartPage(page)
    expect(cart_page.cart_header).to_be_visible()
    expect(cart_page.cart_badge).to_have_text("3")
    assert cart_page.get_cart_item_count() == 3
    cart_page.remove_product_from_cart("Sauce Labs Bike Light")
    expect(cart_page.cart_badge).to_have_text("2")
    assert cart_page.get_cart_item_count() == 2
    cart_page.remove_product_from_cart("Sauce Labs Backpack")
    expect(cart_page.cart_badge).to_have_text("1")
    assert cart_page.get_cart_item_count() == 1
    cart_page.remove_product_from_cart("Sauce Labs Onesie")
    expect(cart_page.cart_badge).to_have_count(0)
    assert cart_page.get_cart_item_count() == 0
    assert cart_page.get_cart_product_names() == []
