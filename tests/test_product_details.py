from playwright.sync_api import expect, Page
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.product_details import ProductDetailsPage

def test_product_details_displayed_correctly(page: Page) -> None:
    login_page = LoginPage(page)
    login_page.navigate()
    login_page.login("standard_user", "secret_sauce")

    inventory_page = InventoryPage(page)
    inventory_page.open_product_details("Sauce Labs Backpack")

    product_details_page = ProductDetailsPage(page)
    expect(product_details_page.get_displayed_product_name()).to_have_text("Sauce Labs Backpack")
    expect(product_details_page.get_displayed_product_description()).not_to_be_empty()
    expect(product_details_page.get_displayed_product_price()).to_have_text("$29.99")
    product_details_page.return_to_inventory_page()

    expect(page).to_have_url("https://www.saucedemo.com/inventory.html")
    expect(inventory_page.products_header).to_be_visible()

def test_add_remove_product_from_details(page: Page) -> None:
    login_page = LoginPage(page)
    login_page.navigate()
    login_page.login("standard_user", "secret_sauce")

    inventory_page = InventoryPage(page)
    inventory_page.open_product_details("Sauce Labs Backpack")

    product_details_page = ProductDetailsPage(page)
    expect(product_details_page.get_displayed_product_name()).to_have_text("Sauce Labs Backpack")
    product_details_page.add_displayed_product_to_cart()
    expect(product_details_page.cart_badge).to_have_text("1")
    product_details_page.remove_displayed_product_from_cart()
    expect(product_details_page.cart_badge).to_have_count(0)
    expect(product_details_page.add_to_cart_button).to_be_visible()
