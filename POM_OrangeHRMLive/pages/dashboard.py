from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class DashboardPage:
    def __init__(self, driver):
        self.driver = driver

    def is_menu_item_clickable(self, menu_name):
        locator = (By.XPATH, f"//span[text()= '{menu_name}']")
        try:
            element = WebDriverWait(self.driver,10).until(EC.element_to_be_clickable(locator))
            return element.is_enabled()
        except:
            return False
