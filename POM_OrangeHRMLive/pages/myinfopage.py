from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class MyInfoPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 15)
        # SPECIFIC: Targets only the 'My Info' link
        self.my_info_menu = (By.XPATH, "//span[text()='My Info']/parent::a")
        self.tabs_container = (By.CLASS_NAME, "orangehrm-tabs")
        self.sub_menu_items = (By.CLASS_NAME, "orangehrm-tabs-item")

    def navigate_to_my_info(self):
        # Wait for the sidebar link
        menu_element = self.wait.until(EC.element_to_be_clickable(self.my_info_menu))

        # Use a JS click to avoid the "renderer timeout" you saw earlier
        self.driver.execute_script("arguments[0].click();", menu_element)

        # Verify transition
        self.wait.until(EC.url_contains("viewPersonalDetails"))

    def get_all_sub_menu_names(self):
        self.wait.until(EC.visibility_of_element_located(self.tabs_container))
        elements = self.wait.until(EC.presence_of_all_elements_located(self.sub_menu_items))

        # RETURN: Must return the list of text strings
        return [el.text.strip() for el in elements if el.text.strip()]

    def click_sub_menu_item(self, item_name):
        # DYNAMIC: Find the link that specifically contains the item_name text
        xpath = f"//a[contains(text(), '{item_name}')]"
        self.wait.until(EC.element_to_be_clickable((By.XPATH, xpath))).click()