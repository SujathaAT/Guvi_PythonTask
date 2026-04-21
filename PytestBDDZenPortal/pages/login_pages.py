import time

from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from utils.common import *


class LoginPage():
    def __init__(self, driver):
        # super().__init__(driver)
        self.driver = driver
        self.__usernameTxtBx = "//div/input[@placeholder='Enter your mail']"
        self.__passwordTxtBx = "//div/input[@placeholder='Enter your password ']"
        self.__loginBtn = "//button[@class ='primary-btn sign-in-pad']"
        # self.__usernameTxtBx = "email"
        # self.__passwordTxtBx = "password"
        # self.__loginBtn = "//button[@type='submit']"

    def enter_credentials(self, username, pwd):
        # time.sleep(2)
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.XPATH, self.__usernameTxtBx)))
        self.driver.find_element(By.XPATH, self.__usernameTxtBx).clear()
        self.driver.find_element(By.XPATH, self.__passwordTxtBx).clear()
        self.driver.find_element(By.XPATH, self.__usernameTxtBx).send_keys(username)
        self.driver.find_element(By.XPATH, self.__passwordTxtBx).send_keys(pwd)
        # # WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.NAME, self.__usernameTxtBx)))
        # # self.driver.find_element(By.NAME, self.__usernameTxtBx).clear()
        # # self.driver.find_element(By.NAME, self.__passwordTxtBx).clear()
        # # self.driver.find_element(By.NAME, self.__usernameTxtBx).send_keys(username)
        # # self.driver.find_element(By.NAME, self.__passwordTxtBx).send_keys(pwd)
        #
        # # wait = WebDriverWait(self.driver, 10)
        # user_field = self.driver.find_element(*self.__passwordTxtBx)
        # # wait.until(EC.visibility_of_element_located(*self.__usernameTxtBx))
        #
        # user_field.clear()
        # user_field.send_keys(username)
        #
        # pass_field = self.driver.find_element(*self.__passwordTxtBx)
        # pass_field.clear()
        # pass_field.send_keys(pwd)

    def click_login(self):
        self.driver.find_element(By.XPATH, self.__loginBtn).click()
        time.sleep(5)

    def validate_zenportalfields(self):
        checkFields(self.driver,(By.XPATH, self.__usernameTxtBx), "Username")
        checkFields(self.driver,(By.XPATH, self.__passwordTxtBx), "Password")
        # checkFields(self, (By.NAME, self.__usernameTxtBx), "Username")
        # checkFields(self, (By.NAME, self.__passwordTxtBx), "Password")

    def validate_zensubmit(self):
        verifyButton(self.driver,(By.XPATH, self.__loginBtn), "Submit ")

    def validate_zennavigation(self):
        self.checkPagetitle("GUVI", "User successfully navigated to Zen Dashboard")

    def verify_unsuccessfullogin(self):
        # checkPageurlnavigation(self,"login", "Login")
        actual_url = self.driver.current_url
        assert "login" in actual_url, f"Expected to be on login page but was at {actual_url}"

    def checkPagetitle(self,page_title, message):
        actual_title = self.driver.title
        print(f"Actual Title: {actual_title}")
        # assert actual_title == page_title, message
        assert actual_title in page_title, f"{message}. Expected '{actual_title}' to be in '{page_title}'"