import pytest
from selenium.common import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# from conftest import driver


#
# class Common:
#
#     def __init__(self, driver, timeout=10):
#         self.driver = driver
#         self.wait = WebDriverWait(driver, timeout)

@pytest.mark.usefixtures("driver")
def checkFields(driver, locator, field=""):
    try:
        element = WebDriverWait(driver, timeout=15).until(EC.visibility_of_element_located(locator))

        if element.is_displayed() and element.is_enabled():
            print(field + "is available")
    except:
        pytest.fail(f"FAIL: Timed out waiting for {field}")

@pytest.mark.usefixtures("driver")
def verifyButton(driver, locator,field=""):
    try:
        element = WebDriverWait(driver, timeout=5).until(EC.element_to_be_clickable(locator))
        if element.is_displayed():
            print(field + "is available")
    except:
        pytest.fail(field + "is not available ")

# @pytest.mark.usefixtures("driver")
# def checkPagetitle(driver,page_title, message):
#     actual_title = driver.title
#     print(f"Actual Title: {actual_title}")
#     assert actual_title == page_title, message

@pytest.mark.usefixtures("driver")
def checkPageurlnavigation(driver,expectedurl_text, message):
    #actual_url = self.driver.current_url
    try:
        WebDriverWait(driver, 10).until(EC.url_contains(expectedurl_text))
        print("Current page is  " + message )
    except TimeoutException as ex:
        pytest.fail("Couldnot be on page" + message)
