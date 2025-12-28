import pytest
from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

class basePage:

    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    def sendkeys(self, locator, value="", field=""):
        try:
            element = self.wait.until(EC.visibility_of_element_located(locator))
            element.clear()
            element.send_keys(value)
            print("Entered Value in " + field)
        except:
            pytest.fail("Could not enter value in " + field)

    def click(self, locator, field=""):
        try:
            self.wait.until(EC.element_to_be_clickable(locator)).click()
            print(field+" was clicked")
        except TimeoutException as ex:
            pytest.fail(field+ " could not be clicked")

    def wait_until_element_visible(self, locator):
        try:
            return self.wait.until(EC.visibility_of_element_located(locator))
        except:
            pytest.fail("Element is not visible")

    def checkPagetitle(self,page_title, message):
        actual_title = self.driver.title
        print(actual_title)
        assert actual_title == page_title, message

    def checkPageurlnavigation(self,expectedurl_text, message):
        #actual_url = self.driver.current_url
        try:
            self.wait.until(EC.url_contains(expectedurl_text))
            print("Current page is  " + message )
        except TimeoutException as ex:
            pytest.fail("Couldnot navigate to page" + message)


    def checkFields(self, locator, field=""):
        try:
            element = self.wait.until(EC.visibility_of_element_located(locator))

            if (element.is_displayed() and element.is_enabled()):
                print(field + "is available")
        except:
            pytest.fail("Unable to find ")


    def checkButton(self, locator, field=""):
        try:
            element = self.wait.until(EC.element_to_be_clickable(locator))
            if (element.is_enabled()):
                print(field + "is enabled" + field)
        except:
            pytest.fail(field + "is disabled ")
