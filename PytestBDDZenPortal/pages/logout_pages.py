import allure
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By

from steps.test_loginsteps import login_page
from utils.common import *
from pages.login_pages import *
class LogoutPage(LoginPage):
    def __init__(self, driver):
        # self.driver = driver
        super().__init__(driver)
        self.__PROFILE_ICON = (By.XPATH, "//div[@class = 'profile-click-icon-div']")
        self.__LOGOUT = (By.XPATH, "//div[contains(text(), 'Log out')]")

    def logsout(self):
        wait = WebDriverWait(self.driver, 20)
        try:
            profile = wait.until(EC.presence_of_element_located(self.__PROFILE_ICON))
            self.driver.execute_script("arguments[0].scrollIntoView(true);", profile)
            self.driver.execute_script("arguments[0].click();", profile)
            logout_btn = wait.until(EC.element_to_be_clickable(self.__LOGOUT))
            self.driver.execute_script("arguments[0].click();", logout_btn)

        except (Exception,TimeoutException) as e:
            allure.attach(self.driver.get_screenshot_as_png(), name="Failure_Logout_Timedout")
            raise e

        # self.driver.find_element(*self.__PROFILE_ICON).click() #, "Profile Icon")
        # self.driver.find_element(*self.__LOGOUT).click()#, "Logout")

        # wait = WebDriverWait(self.driver, 15)
        # try:
        #     profile = wait.until(EC.element_to_be_clickable(self.__PROFILE_ICON))
        #     profile.click()
        #     logout_btn = wait.until(EC.visibility_of_element_located(self.__LOGOUT))
        #     logout_btn.click()
        # except (TimeoutException, NoSuchElementException) as e:
        #     allure.attach(self.driver.get_screenshot_as_png(),
        #               name="logout_error",
        #               attachment_type=allure.attachment_type.PNG)
        #     raise Exception(f"Logout failed due to: {str(e)}")

    def checkLogout_functionality(self):
        wait = WebDriverWait(self.driver, 15)
        try:
            wait.until(EC.presence_of_element_located((By.NAME, "email")))
            print("Log out is successful")
        except TimeoutException:
            allure.attach(self.driver.get_screenshot_as_png(), name="Logout_Verification_Failed")
            pytest.fail(f"Logout failed. Actual title was: {self.driver.title}")

    # def checkLogout_functionality(self):
    #     # LoginPage.checkPagetitle(self,"GUVI", "Log out is successful")
    #     wait = WebDriverWait(self.driver, 10)
    #     wait.until(EC.title_contains("GUVI"))
    #     # wait.until(EC.presence_of_element_located((By.XPATH, self.__usernameTxtBx)))
    #     self.checkPagetitle("GUVI", "Log out is successful")
    #
