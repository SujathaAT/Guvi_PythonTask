from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from utils.common_util import verify_fields_presence


class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

        self.username_field = (By.NAME, "username")
        self.password_field = (By.NAME, "password")
        self.login_button = (By.XPATH, "//button[@type='submit']")
        self.user_dropdown = (By.XPATH, "//p[@class = 'oxd-userdropdown-name']")
        self.logout_link = (By.XPATH, "//a[contains(text(), 'Logout')]")
        self.forgot_password_link = (By.XPATH, "//p[contains(@class, 'login-forgot-header')]")

    def login(self, user, pwd):
        self.wait.until(EC.visibility_of_element_located(self.username_field)).send_keys(user)
        self.driver.find_element(*self.password_field).send_keys(pwd)
        self.driver.find_element(*self.login_button).click()


    def verify_login_fields_presence(self):
        username_flag = verify_fields_presence(self.driver, self.username_field)
        pwd_flag = verify_fields_presence(self.driver, self.password_field)

        assert username_flag is True
        assert pwd_flag is True

        return username_flag and pwd_flag


    def is_login_button_displayed(self):
        # Check  login button is displayed
        try:
            element = WebDriverWait(self.driver, 20).until(
                EC.visibility_of_element_located(self.login_button)
            )
            return element.is_displayed()
        except:
            return False


    def logout(self):
        self.wait.until(EC.element_to_be_clickable(self.user_dropdown)).click()
        self.wait.until(EC.element_to_be_clickable(self.logout_link)).click()

    def click_forgot_password(self):
        # self.driver.find_element(*self.forgot_password_link).click()
        self.wait.until(EC.element_to_be_clickable(self.forgot_password_link)).click()