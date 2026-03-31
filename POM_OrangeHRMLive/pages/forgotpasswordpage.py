from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class ForgotPasswordPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)
        self.username_input = (By.NAME, "username")
        self.reset_button = (By.XPATH, "//button[@type='submit']")
        self.success_title = (By.TAG_NAME, "h6")

    def enter_username(self, username):
        # self.driver.find_element(*self.username_input).send_keys(username)
        element = self.wait.until(EC.visibility_of_element_located(self.username_input))
        element.send_keys(username)

    def click_reset_password(self):
        # self.driver.find_element(*self.reset_button).click()
        # self.wait.until(EC.element_to_be_clickable(self.reset_button)).click()
        button = self.wait.until(EC.presence_of_element_located(self.reset_button))
        self.driver.execute_script("arguments[0].click();", button)

    def get_confirmation_text(self):
        # return self.driver.find_element(*self.success_title).text
        element = self.wait.until(EC.visibility_of_element_located(self.success_title))
        return element.text