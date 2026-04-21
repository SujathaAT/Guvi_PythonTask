from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

class CommonKeywords:
    def __init__(self):
        self.driver = None

    def open_browser(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

    def launch_url(self, url):
        self.driver.get(url)

    def enter_text(self, locator, value):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.visibility_of_element_located((By.XPATH, locator)))
        element.clear()
        element.send_keys(value)

    def click(self, locator):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable((By.XPATH, locator))).click()

    def verify_page(self, expected_title):
        wait = WebDriverWait(self.driver, 10)
        # For OrangeHRM, wait for a specific dashboard element to confirm login
        try:
            wait.until(EC.title_contains(expected_title))
            return True
        except:
            return False

    def close_browser(self):
        if self.driver:
            self.driver.quit()

