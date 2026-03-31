import re

from playwright.sync_api import Page, expect

class HeaderPage():
    def __init__(self, page: Page):
        self.page = page
        # Define Locators
        # self.login_btn = page.get_by_role("link", name="Login")
        # self.login_btn = page.get_by_role("link", name=re.compile("login", re.IGNORECASE))
        self.login_btn = page.locator("#login-btn").first
        self.signup_btn = page.get_by_role("button", name="Sign up")
        self.courses_menu = page.get_by_role("link", name="Courses", exact=True)
        self.live_classes_menu = page.get_by_role("link", name="LIVE Classes")
        self.practice_menu = page.get_by_role("link", name="Practice Platforms")
        self.dobby_widget = page.get_by_role("button", name=re.compile("dobby", re.I))
        # self.signup_btn = page.get_by_role("link", name=re.compile(r"sign up", re.I)).first

    def navigate_to_login(self):
        self.login_btn.click()

    def navigate_to_signup(self):
        self.signup_btn.click()

    def verify_menu_items_visible(self):
        expect(self.courses_menu).to_be_visible()
        expect(self.live_classes_menu).to_be_visible()
        expect(self.practice_menu).to_be_visible()

    def verify_menu_items_enabled(self):
        """Validates that menu items are accessible (clickable)."""
        expect(self.courses_menu).to_be_enabled()
        expect(self.live_classes_menu).to_be_enabled()
        expect(self.practice_menu).to_be_enabled()