from selenium.webdriver.common.by import By
from pages.basepage import BasePage

class LoginPage(BasePage):
    # Locators
    USERNAME_FIELD = (By.ID, "user-name")
    PASSWORD_FIELD = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-button")
    ERROR_MSG = (By.CSS_SELECTOR, "h3[data-test='error']")

    def login(self, username, password):
        # FIX: Call the helper methods, OR pass the correct LOCATOR
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()

    def enter_username(self, username):
        self.type_text(self.USERNAME_FIELD, username)  # Correct: Passing the locator tuple

    def enter_password(self, password):
        self.type_text(self.PASSWORD_FIELD, password)

    def click_login(self):
        self.click_element(self.LOGIN_BUTTON)

    def get_error_message(self):
        return self.get_text(self.ERROR_MSG)