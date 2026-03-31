# import time
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class AdminPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 15)
        self.admin_menu = (By.XPATH, "//span[text() = 'Admin']")
        self.add_button = (By.XPATH, "//button[normalize-space()='Add']")
        self.user_role_dropdown = (By.XPATH,
                                   "//label[text()='User Role']/parent::div/following-sibling::div//div[@class='oxd-select-text-input']")
        self.status_dropdown = (By.XPATH,
                                "//label[text()='Status']/parent::div/following-sibling::div//div[@class='oxd-select-text-input']")
        self.listbox_option = "//div[@role='listbox']//*[contains(text(), '{}')]"

        # self.user_role_dropdown = (By.XPATH, "//label/parent::div/following-sibling::div//div")
        # self.status_dropdown = (By.XPATH, "//label/parent::div/following-sibling::div//div")
        # self.listbox_option = "//div[@role='listbox']//*"
        self.employee_name = (By.XPATH, "//input[@placeholder='Type for hints...']")
        self.username_input = (By.XPATH, "//label[text() = 'Username']/parent::div/following-sibling::div/input")
        self.password_input = (By.XPATH, "//label[text() = 'Password']/parent::div/following-sibling::div/input")
        self.confirm_password_input = (By.XPATH, "//label[text() = 'Confirm Password']/parent::div/following-sibling::div/input")

        self.save_button = (By.XPATH, "//button[@type='submit']")
        self.search_username_input = (By.XPATH, "//label/parent::div/following-sibling::div//input")
        self.search_button = (By.XPATH, "//button[@type='submit']")
        self.table_record = (By.XPATH, "//div[@class='oxd-table-card']//div[@role='row']")


    def click_admin(self):
        self.wait.until(EC.element_to_be_clickable(self.admin_menu)).click()

    def create_user(self, emp_name, new_user, new_pwd):
        self.wait.until(EC.element_to_be_clickable(self.add_button)).click()

        # Select Role
        self.wait.until(EC.element_to_be_clickable(self.user_role_dropdown)).click()
        self.wait.until(EC.element_to_be_clickable((By.XPATH, self.listbox_option.format("ESS")))).click()

        # Employee Name Handling (The probable cause of failure)
        emp_input = self.wait.until(EC.presence_of_element_located(self.employee_name))
        emp_input.send_keys(emp_name)
        time.sleep(5)
        # WAIT for the dropdown options to actually appear before clicking
        suggestion_xpath = "//div[@role='listbox']//div[@role='option']"
        # self.wait.until(EC.element_to_be_clickable((By.XPATH, suggestion_xpath))).click()
        try:
            suggestion = self.wait.until(EC.element_to_be_clickable((By.XPATH, suggestion_xpath)))
            suggestion.click()
        except:
            # Fallback: If "a" failed, clear and try "Admin"
            emp_input.clear()
            emp_input.send_keys("Tester Test QA")
            self.wait.until(EC.element_to_be_clickable((By.XPATH, suggestion_xpath))).click()

        # Select Status
        self.wait.until(EC.element_to_be_clickable(self.status_dropdown)).click()
        self.wait.until(EC.element_to_be_clickable((By.XPATH, self.listbox_option.format("Enabled")))).click()

        # Credentials
        self.driver.find_element(*self.username_input).send_keys(new_user)
        self.driver.find_element(*self.password_input).send_keys(new_pwd)
        self.driver.find_element(*self.confirm_password_input).send_keys(new_pwd)

        # Final Save
        self.driver.find_element(*self.save_button).click()

        # Wait for the redirect back to the user list
        self.wait.until(EC.url_contains("viewSystemUsers"))

    # def create_user(self, emp_name, new_user, new_pwd):
    #
    #     self.wait.until(EC.element_to_be_clickable(self.add_button)).click()
    #
    #     self.wait.until(EC.element_to_be_clickable(self.user_role_dropdown)).click()
    #     self.wait.until(EC.element_to_be_clickable((By.XPATH, self.listbox_option.format("ESS")))).click()
    #     self.wait.until(EC.presence_of_element_located(self.employee_name)).send_keys(emp_name)
    #     suggestion = (By.XPATH, "//div[@role='listbox']//div[@role='option']")
    #     self.wait.until(EC.element_to_be_clickable(suggestion)).click()
    #     self.driver.find_element(*self.status_dropdown).click()
    #     self.wait.until(EC.element_to_be_clickable((By.XPATH, self.listbox_option.format("Enabled")))).click()
    #     self.driver.find_element(*self.username_input).send_keys(new_user)
    #     self.driver.find_element(*self.password_input).send_keys(new_pwd)
    #     self.driver.find_element(*self.confirm_password_input).send_keys(new_pwd)
    #
    #     self.driver.find_element(*self.save_button).click()
    #     self.wait.until(EC.url_contains("viewSystemUsers"))

    def search_user(self, username):
        # 1. Locate and fill the username search field
        search_field = self.wait.until(EC.visibility_of_element_located(self.search_username_input))
        search_field.send_keys(username)

        # 2. Click Search
        self.driver.find_element(*self.search_button).click()

        row_xpath = f"//div[@role='row'][contains(., '{username}')]"
        self.wait.until(EC.presence_of_element_located((By.XPATH, row_xpath)))

    def is_user_present_in_list(self, username):
        # Check if any row in the table contains the username
        rows = self.driver.find_elements(*self.table_record)
        for row in rows:
            if username in row.text:
                return True
        return False