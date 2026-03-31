from playwright.sync_api import Page


class SignupPage():
    def __init__(self, page: Page):
        self.page = page
        # locators
        self.full_name_input = page.locator("#name")
        self.email_input = page.locator("#email")
        self.password_input = page.locator("#password")
        self.mobile_input = page.locator("#mobileNumber")
        self.signup_submit_btn = page.locator(".signup-btn") # Update with actual site class

    def register_user(self, name, email, password, mobile):
        self.full_name_input.fill(name)
        self.email_input.fill(email)
        self.password_input.fill(password)
        self.mobile_input.fill(mobile)
        self.signup_submit_btn.click()

