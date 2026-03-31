import time
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LeavePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 15)

        # Locators
        self.leave_menu = (By.XPATH, "//span[text() = 'Leave']")
        self.assign_leave_tab = (By.XPATH, "//a[contains(text(), 'Assign Leave')]")
        self.employee_name_input = (By.XPATH, "//input[@placeholder='Type for hints...']")
        self.employee_dropdown_option = (By.XPATH, "//div[@role='listbox']//span")
        self.leave_type_dropdown = (By.CLASS_NAME, "oxd-select-text")
        self.leave_type_option = (By.XPATH, "//div[@role='listbox']//div[@role='option']")
        self.from_date_input = (By.XPATH, "(//input[@placeholder='yyyy-dd-mm'])[1]")
        self.to_date_input = (By.XPATH, "(//input[@placeholder='yyyy-dd-mm'])[2]")
        self.assign_button = (By.XPATH, "//button[@type='submit']")
        self.confirm_ok_button = (By.XPATH, "//div[@role='document']//button[contains(translate(., 'OK', 'ok'), 'ok')]")
        self.success_toast = (By.CLASS_NAME, "oxd-toast-content")

    def navigate_to_assign_leave(self):
        self.wait.until(EC.element_to_be_clickable(self.leave_menu)).click()
        self.wait.until(EC.element_to_be_clickable(self.assign_leave_tab)).click()

    def fill_assign_leave_form(self, partial_name, start_date, end_date):
        # Employee Hint Dropdown
        emp_input = self.wait.until(EC.visibility_of_element_located(self.employee_name_input))
        emp_input.send_keys(partial_name)
        time.sleep(2)  # Wait for AJAX hints to load
        self.wait.until(EC.element_to_be_clickable(self.employee_dropdown_option)).click()

        # Leave Type
        # self.driver.find_element(*self.leave_type_dropdown).click()
        # self.wait.until(EC.element_to_be_clickable(self.leave_type_option)).click()
        self.wait.until(EC.element_to_be_clickable(self.leave_type_dropdown)).click()
        options = self.wait.until(EC.presence_of_all_elements_located(self.leave_type_option))
        if len(options) > 1:
            options[1].click()
        else:
            options[0].click()

        # Dates (Clear with CTRL+A to handle pre-filled values)
        for selector, value in [(self.from_date_input, start_date), (self.to_date_input, end_date)]:
            date_field = self.wait.until(EC.element_to_be_clickable(selector))
            date_field.send_keys(Keys.CONTROL + "a")
            date_field.send_keys(Keys.BACKSPACE)
            date_field.send_keys(value)
            date_field.send_keys(Keys.ESCAPE)

    def submit_assignment(self):
        self.wait.until(EC.element_to_be_clickable(self.assign_button)).click()
        try:
            pop_up_button = self.wait.until(EC.element_to_be_clickable(self.confirm_ok_button))
            time.sleep(0.5)
            pop_up_button.click()
            print("Insufficient balance pop-up appears")
        except:
            print("No balance pop-up appeared; proceeding to success check.")

    def is_success_message_displayed(self):
        try:
            return self.wait.until(EC.visibility_of_element_located(self.success_toast)).is_displayed()
        except:
            return False