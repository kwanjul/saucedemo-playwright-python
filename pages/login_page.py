from playwright.sync_api import Page
from config import BASE_URL

class LoginPage:

    def __init__(self, page: Page) -> None:
        self.page: Page = page
        self.username_field = self.page.locator("#user-name")
        self.password_field = self.page.locator("#password")
        self.login_button = self.page.locator("#login-button")
        self.error_message = self.page.get_by_test_id("error")

    def login(self, username: str, password: str) -> None:
        self.username_field.fill(username)
        self.password_field.fill(password)
        self.login_button.click()

    def navigate(self) -> None:
        self.page.goto(BASE_URL)
