from selenium.webdriver.common.by import By

from pages.basePage import  basePage

class LogoutPage(basePage):
    PROFILE_ICON = (By.XPATH, "//div[@class = 'profile-click-icon-div']")
    LOGOUT = (By.XPATH, "//div[contains(text(), 'Log out')]")

    def logout(self):
        self.click(self.PROFILE_ICON , "Profile Icon")
        self.click(self.LOGOUT, "Logout")

    def checkLogout_functionality(self):
        self.checkPagetitle("GUVI", "Log out is successful")

