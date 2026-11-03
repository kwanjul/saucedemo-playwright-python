from playwright.sync_api import expect, Page
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage

def test_inventory_page_loads(page: Page) -> None:
    login_page = LoginPage(page)
    login_page.navigate()
    login_page.login("standard_user", "secret_sauce")

    inventory_page = InventoryPage(page)
    expect(inventory_page.products_header).to_be_visible()
    assert inventory_page.get_product_count() == 6
    assert "Sauce Labs Backpack" in inventory_page.get_product_names()

def test_all_inventory_products_displayed(page: Page) -> None:
    login_page = LoginPage(page)
    login_page.navigate()
    login_page.login("standard_user", "secret_sauce")

    inventory_page = InventoryPage(page)
    expect(inventory_page.products_header).to_be_visible()
    expected_products = {
        "Sauce Labs Backpack", 
        "Sauce Labs Bike Light", 
        "Sauce Labs Bolt T-Shirt", 
        "Sauce Labs Fleece Jacket", 
        "Sauce Labs Onesie", 
        "Test.allTheThings() T-Shirt (Red)"
    }
    assert set(inventory_page.get_product_names()) == expected_products
    assert inventory_page.get_product_count() == 6

def test_sort_products_by_name(page: Page) -> None:
    login_page = LoginPage(page)
    login_page.navigate()
    login_page.login("standard_user", "secret_sauce")

    inventory_page = InventoryPage(page)
    expect(inventory_page.products_header).to_be_visible()
    expected_products = [
        "Sauce Labs Backpack", 
        "Sauce Labs Bike Light", 
        "Sauce Labs Bolt T-Shirt", 
        "Sauce Labs Fleece Jacket", 
        "Sauce Labs Onesie", 
        "Test.allTheThings() T-Shirt (Red)"
    ]

    inventory_page.sort_products("Name (Z to A)")
    assert inventory_page.get_product_names() == sorted(expected_products, reverse=True)

    inventory_page.sort_products("Name (A to Z)")
    assert inventory_page.get_product_names() == sorted(expected_products)

def test_sort_products_by_price(page: Page) -> None:
    login_page = LoginPage(page)
    login_page.navigate()
    login_page.login("standard_user", "secret_sauce")

    inventory_page = InventoryPage(page)
    expect(inventory_page.products_header).to_be_visible()

    inventory_page.sort_products("Price (high to low)")
    inventory_prices = inventory_page.get_product_prices()
    assert inventory_prices == sorted(inventory_prices, reverse=True)

    inventory_page.sort_products("Price (low to high)")
    inventory_prices = inventory_page.get_product_prices()
    assert inventory_prices == sorted(inventory_prices)

def test_add_product_to_cart(page: Page) -> None:
    login_page = LoginPage(page)
    login_page.navigate()
    login_page.login("standard_user", "secret_sauce")

    inventory_page = InventoryPage(page)
    expect(inventory_page.products_header).to_be_visible()

    inventory_page.add_product_to_cart("Sauce Labs Backpack")
    expect(inventory_page.cart_badge).to_have_text("1")

def test_add_remove_multiple_products(page: Page) -> None:
    login_page = LoginPage(page)
    login_page.navigate()
    login_page.login("standard_user", "secret_sauce")

    inventory_page = InventoryPage(page)
    expect(inventory_page.products_header).to_be_visible()
    expect(inventory_page.cart_badge).to_have_count(0)

    inventory_page.add_product_to_cart("Sauce Labs Backpack")
    expect(inventory_page.cart_badge).to_have_text("1")

    inventory_page.add_product_to_cart("Sauce Labs Bike Light")
    expect(inventory_page.cart_badge).to_have_text("2")

    inventory_page.add_product_to_cart("Sauce Labs Onesie")
    expect(inventory_page.cart_badge).to_have_text("3")

    inventory_page.remove_product_from_cart("Sauce Labs Bike Light")
    expect(inventory_page.cart_badge).to_have_text("2")

    inventory_page.remove_product_from_cart("Sauce Labs Backpack")
    expect(inventory_page.cart_badge).to_have_text("1")

    inventory_page.remove_product_from_cart("Sauce Labs Onesie")
    expect(inventory_page.cart_badge).to_have_count(0)
