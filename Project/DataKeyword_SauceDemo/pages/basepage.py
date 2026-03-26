from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)

    def find_element(self, locator):
        return self.wait.until(EC.presence_of_element_located(locator))

    def type_text(self, locator, text):
        element = self.find_element(locator)  # Calls find_element above
        element.clear()
        element.send_keys(text)

    # def find_element(self, locator):
    #     """Resilient element finding with explicit wait."""
    #     try:
    #         return self.wait.until(EC.presence_of_element_located(locator))
    #     except TimeoutException:
    #         print(f"Error: Element {locator} not found within timeout.")
    #         return None

    def find_elements(self, locator):
        try:
            return self.wait.until(EC.presence_of_all_elements_located(locator))
        except TimeoutException:
            return []

    def click_element(self, locator):
        element = self.wait.until(EC.element_to_be_clickable(locator))
        element.click()

    # def type_text(self, locator, text):
    #     try:
    #         # Wait for element to be ready for interaction
    #         element = self.wait.until(EC.element_to_be_clickable(locator))
    #         element.clear()
    #         element.send_keys(text)
    #         # Verify text was actually entered (Optional but helpful for debugging)
    #         if element.get_attribute("value") != text:
    #             element.send_keys(text)
    #     except Exception as e:
    #         print(f"Failed to type '{text}' into {locator}: {e}")
    #         raise e


    def get_text(self, locator):
        return self.find_element(locator).text

    def get_current_url(self):
        return self.driver.current_url