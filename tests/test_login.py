from playwright.sync_api import expect, Page
from pages.login_page import LoginPage

def test_login_page_loads(page: Page) -> None:
    login_page = LoginPage(page)
    login_page.navigate()

    expect(login_page.username_field).to_be_visible()
    expect(login_page.password_field).to_be_visible()

def test_successful_login(page: Page) -> None:
    login_page = LoginPage(page)
    login_page.navigate()
    login_page.login("standard_user", "secret_sauce")
    expect(page).to_have_url("https://www.saucedemo.com/inventory.html")
    expect(page.get_by_text("Products", exact=True)).to_be_visible()

def test_invalid_login(page: Page) -> None:
    login_page = LoginPage(page)
    login_page.navigate()
    login_page.login("invalid_user", "wrong_password")
    expect(login_page.error_message).to_have_text("Epic sadface: Username and password do not match any user in this service")
    expect(page).to_have_url("https://www.saucedemo.com/")
    expect(login_page.username_field).to_be_visible()
    expect(login_page.password_field).to_be_visible()

def test_locked_out_user(page: Page) -> None:
    login_page = LoginPage(page)
    login_page.navigate()
    login_page.login("locked_out_user", "secret_sauce")
    expect(login_page.error_message).to_have_text("Epic sadface: Sorry, this user has been locked out.")
    expect(page).to_have_url("https://www.saucedemo.com/")
    expect(login_page.username_field).to_be_visible()
    expect(login_page.password_field).to_be_visible()
