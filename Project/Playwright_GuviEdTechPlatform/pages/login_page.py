import pytest
from playwright.sync_api import Page, expect


class LoginPage():
    def __init__(self, page: Page):
        self.page = page
        # Define Locators
        # self.dashboard_login_btn = self.page.locator("//button[text(), 'Login'][1]")
        self.dashboard_login_btn = self.page.get_by_role("button", name="Login").first
        self.email = self.page.locator("//input[@id = 'email']")
        self.password = self.page.locator("//input[@id = 'password']")
        self.login_btn = self.page.locator("//a[@id ='login-btn']")
        # self.errormsg = page.locator("//div[contains(@class, 'invalid-feedback')]")
        self.chat_window = "//span[@class= 'siqico-chat zsiq-chat-icn']"
        self.errormsg = page.get_by_text("Incorrect Email or Password", exact=False)
        # self.error_message = page.locator(".error-message-class") # Update with actual site class

    def login(self, email, password):
        self.any_error = self.page.locator("//div[@id='emailgroup']/div | //div[@id='passwordGroup']/div")

        self.email.fill(email)
        self.password.fill(password)

        try:
            self.login_btn.is_visible()
            self.login_btn.click()
            self.page.locator(self.chat_window).is_visible()
        except:
            pytest.fail("Could not click login button")

    def click_login(self):
        self.dashboard_login_btn.click()
        self.page.wait_for_load_state("networkidle")
        # expect(self.page.wait_for_load_state("networkidle")).is_not_none()

    def get_error_text(self,errorlocator):
        return self.errormsg
                # .inner_text())
        # return self.errormsg.text_content()
