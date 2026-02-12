import pytest

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class Commonutils:

    def __init__(self, driver, timeout = 5):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, timeout)

    def checkElement_availability(self, locator, field):
        checkElement_availability = False
        try:
            ele = self.wait.until(EC.visibility_of_element_located(locator))
            if (ele.is_displayed() == True):
                # print(field + "is available")
                return ele.is_displayed()


        except Exception as e:
            print(e)
            pytest.fail("Unable to find " + field)

