from selenium.webdriver.common.by import By

from pages.basePage import  basePage

class LoginPage(basePage):
    USERNAME = (By.XPATH, "//div/input[@id =':r1:']")
    PASSWORD = (By.XPATH, "//div/input[@id =':r2:']")
    BUTTON = (By.XPATH, "//button[@class ='primary-btn sign-in-pad']")
    LAUNCH_ALERT_CLOSE = (By.XPATH, "//button[@class = 'custom-close-button']")

    def enter_credentials(self, username, pwd):
        self.sendkeys(self.USERNAME, username, " Username")
        self.sendkeys(self.PASSWORD, pwd, " Password")

    def signin(self):
        self.click(self.BUTTON , "Submit")

    def closelaunchalert(self):
        self.click(self.LAUNCH_ALERT_CLOSE , "Close")

    def validate_zenportalfields(self):
        self.checkFields(self.USERNAME, "Username")
        self.checkFields(self.PASSWORD, "Password")

    def validate_zenportalsubmit(self):
        self.checkButton(self.BUTTON, "Submit ")

    def verify_unsuccessfullogin(self):
        self.checkPageurlnavigation("login", "Login")
