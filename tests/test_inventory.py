from playwright.sync_api import expect, Page
from pages.inventory_page import InventoryPage

def test_inventory_page_loads(logged_in_page: Page) -> None:
    inventory_page = InventoryPage(logged_in_page)
    expect(inventory_page.get_inventory_items()).to_have_count(6)
    assert "Sauce Labs Backpack" in inventory_page.get_product_names()

def test_all_inventory_products_displayed(logged_in_page: Page) -> None:
    inventory_page = InventoryPage(logged_in_page)
    expected_products = {
        "Sauce Labs Backpack", 
        "Sauce Labs Bike Light", 
        "Sauce Labs Bolt T-Shirt", 
        "Sauce Labs Fleece Jacket", 
        "Sauce Labs Onesie", 
        "Test.allTheThings() T-Shirt (Red)"
    }
    expect(inventory_page.get_inventory_items()).to_have_count(6)
    assert set(inventory_page.get_product_names()) == expected_products

def test_sort_products_by_name(logged_in_page: Page) -> None:
    inventory_page = InventoryPage(logged_in_page)
    expected_products = [
        "Sauce Labs Backpack", 
        "Sauce Labs Bike Light", 
        "Sauce Labs Bolt T-Shirt", 
        "Sauce Labs Fleece Jacket", 
        "Sauce Labs Onesie", 
        "Test.allTheThings() T-Shirt (Red)"
    ]

    actual_products = inventory_page.get_product_name_elements()

    inventory_page.sort_products("Name (Z to A)")
    expect(actual_products).to_have_text(sorted(expected_products, reverse=True))

    inventory_page.sort_products("Name (A to Z)")
    expect(actual_products).to_have_text(sorted(expected_products))

def test_sort_products_by_price(logged_in_page: Page) -> None:
    inventory_page = InventoryPage(logged_in_page)
    
    expected_prices = [29.99, 9.99, 15.99, 49.99, 7.99, 15.99] 
    actual_prices = inventory_page.get_product_price_elements()

    inventory_page.sort_products("Price (high to low)")
    expect(actual_prices).to_have_text([f"${price:.2f}" for price in sorted(expected_prices, reverse=True)])

    inventory_page.sort_products("Price (low to high)")
    expect(actual_prices).to_have_text([f"${price:.2f}" for price in sorted(expected_prices)])

def test_add_product_to_cart(logged_in_page: Page) -> None:
    inventory_page = InventoryPage(logged_in_page)
    expect(inventory_page.products_header).to_be_visible()

    inventory_page.add_product_to_cart("Sauce Labs Backpack")
    expect(inventory_page.cart_badge).to_have_text("1")

def test_add_remove_multiple_products(logged_in_page: Page) -> None:
    inventory_page = InventoryPage(logged_in_page)
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
