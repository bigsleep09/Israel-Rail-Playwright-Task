import re
from playwright.sync_api import Page, expect

def test_has_title(page: Page):
    page.goto("https://www.saucedemo.com/")

    # Expect a title "to contain" a substring.
    expect(page).to_have_title(re.compile("Swag Labs"))

def test_get_login_wrapper(page: Page):
    page.goto("https://www.saucedemo.com/")

    # Click the get started link.
    expect(page.locator("[data-test='login-container']")).to_be_visible()

    