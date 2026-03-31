import time

import pytest
from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import Keys

class ClaimPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 15)

        # Navigation & Actions
        self.claim_menu = (By.XPATH, "//span[text() = 'Claim']")
        self.navbar = (By.XPATH,"//nav[@aria-label='Topbar Menu']")
        self.navbar_items = (By.XPATH, "//nav[@aria-label='Topbar Menu']//li")
        self.submit_claim_tab = (By.XPATH, "//a[contains(text(), 'Submit Claim')]")
        self.create_button = (By.XPATH, "//button[contains(., 'Create')]")
        # self.submit_button = (By.XPATH, "//button[@type='submit'][contains(., 'Submit')]")
        self.submit_button = (By.XPATH, "// button[contains(., 'Submit')]")
        # self.event_dropdown = (By.XPATH, "//label[text() = 'Event']/parent::div//following-sibling::div//div[@class='oxd-select-text-input']")
        # self.currency_dropdown = (By.XPATH, "//label[text() = 'Currency']/parent::div//following-sibling::div//div[@class='oxd-select-text-input']")
        # self.dropdown_option = (By.XPATH, "//div[@role='listbox']//div[@role='option']")
        self.event_dropdown = (By.XPATH, "//label/following::div[contains(@class, 'oxd-select-wrapper')]")
        self.currency_dropdown = (By.XPATH, "//label/following::div[contains(@class, 'oxd-select-wrapper')]")
        self.dropdown_option = (By.CSS_SELECTOR, "div[role='listbox'] div[role='option']")
        self.remarks_input = (By.XPATH, "//textarea")

        # History/Verification
        self.my_claims_tab = (By.XPATH, "//a[contains(., 'My Claims')]")
        self.success_toast = (By.CLASS_NAME, "oxd-toast-content")

    def navigate_to_submit_claim(self):
        self.wait.until(EC.element_to_be_clickable(self.claim_menu)).click()

        self.wait.until(EC.visibility_of_element_located(self.navbar))
        tabs = self.driver.find_elements(*self.navbar_items)
        tab_names = [t.text for t in tabs]
        print(f"\nAvailable Tabs: {tab_names}")

        if "Submit Claim" not in tab_names:
            pytest.fail(f"User doesnot have permission. Visible tabs: {tab_names}")

        try:
            self.wait.until(EC.element_to_be_clickable(self.submit_claim_tab)).click()
        except TimeoutException:
            print("FAIL: 'Submit Claim' tab not found in the list above.")
            raise TimeoutException

    # def initiate_new_claim(self, event_index=1  , currency_index=1, remarks="Automation Claim"):
    #     # # Select Event
    #     # self.wait.until(EC.element_to_be_clickable(self.event_dropdown)).click()
    #     # # self.wait.until(EC.presence_of_all_elements_located(self.dropdown_option))[event_index].click()
    #     # time.sleep(0.5)
    #     event_field = self.wait.until(EC.presence_of_element_located(self.event_dropdown))
    #     self.driver.execute_script("arguments[0].click();", event_field)
    #
    #     options = self.wait.until(EC.visibility_of_all_elements_located(self.dropdown_option))
    #     if len(options) > event_index:
    #         options[event_index].click()
    #     else:
    #         options[0].click()
    #     time.sleep(0.5)
    #     # Currency - Wait for presence again as listbox refreshes
    #     self.wait.until(EC.element_to_be_clickable(self.currency_dropdown)).click()
    #     # self.wait.until(EC.presence_of_all_elements_located(self.dropdown_option))[currency_index].click()
    #     curr_options = self.wait.until(EC.visibility_of_all_elements_located(self.dropdown_option))
    #
    #     if len(curr_options) > currency_index:
    #         curr_options[currency_index].click()
    #     else:
    #         curr_options[0].click()
    #
    #     self.driver.find_element(*self.remarks_input).send_keys(remarks)
    #     self.driver.find_element(*self.create_button).click()

    # def initiate_new_claim(self, event_index, currency_index, remarks):
    #     # 1. Open Event Dropdown using JavaScript
    #     event_box = self.wait.until(EC.presence_of_element_located(self.event_dropdown))
    #     self.driver.execute_script("arguments[0].click();", event_box)
    #
    #     # 2. Wait for and click the option
    #     options = self.wait.until(EC.visibility_of_all_elements_located(self.dropdown_option))
    #     # Logic to skip the first "-- Select --" if necessary
    #     idx = int(event_index)
    #     options[idx].click()
    #
    #     # Ensure it's closed and let AJAX load currencies
    #     self.wait.until(EC.invisibility_of_element_located(self.dropdown_option))
    #     time.sleep(1.5)
    #
    #     # 3. Open Currency Dropdown using JavaScript
    #     curr_box = self.wait.until(EC.presence_of_element_located(self.currency_dropdown))
    #     self.driver.execute_script("arguments[0].click();", curr_box)
    #
    #     curr_options = self.wait.until(EC.visibility_of_all_elements_located(self.dropdown_option))
    #     c_idx = int(currency_index)
    #     curr_options[c_idx].click()
    #     self.wait.until(EC.invisibility_of_element_located(self.dropdown_option))
    #
    #     # 4. Fill Remarks and Create
    #     self.driver.find_element(*self.remarks_input).send_keys(str(remarks))
    #     create_btn = self.wait.until(EC.element_to_be_clickable(self.create_button))
    #     self.driver.execute_script("arguments[0].click();", create_btn)

    # def initiate_new_claim(self, event_index, currency_index, remarks):
    #     # 1. Handle Event Dropdown via Keyboard
    #     event_box = self.wait.until(EC.element_to_be_clickable(self.event_dropdown))
    #     event_box.click()
    #
    #     # Press Down Arrow 'n' times based on your index, then Enter
    #     for _ in range(int(event_index)):
    #         event_box.send_keys(Keys.ARROW_DOWN)
    #     event_box.send_keys(Keys.ENTER)
    #
    #     # Buffer for AJAX (Currency list loads based on Event)
    #     time.sleep(1.5)
    #
    #     # 2. Handle Currency Dropdown via Keyboard
    #     curr_box = self.wait.until(EC.element_to_be_clickable(self.currency_dropdown))
    #     curr_box.click()
    #
    #     for _ in range(int(currency_index)):
    #         curr_box.send_keys(Keys.ARROW_DOWN)
    #     curr_box.send_keys(Keys.ENTER)
    #
    #     # 3. Fill Remarks (Ensure it's a string)
    #     self.driver.find_element(*self.remarks_input).send_keys(str(remarks))
    #
    #     # 4. Create - Use JS Click as a safety net
    #     create_btn = self.wait.until(EC.element_to_be_clickable(self.create_button))
    #     self.driver.execute_script("arguments[0].click();", create_btn)

    # def initiate_new_claim(self, event_index, currency_index, remarks):
    #     # 1. Open Event Dropdown
    #     event_box = self.wait.until(EC.element_to_be_clickable(self.event_dropdown))
    #     event_box.click()  # Click the wrapper
    #
    #     # 2. Wait for options and click by index
    #     # We use visibility_of_all to ensure the list is actually rendered
    #     options = self.wait.until(EC.visibility_of_all_elements_located(self.dropdown_option))
    #     options[int(event_index)].click()
    #
    #     # IMPORTANT: Wait for listbox to disappear before clicking next
    #     # self.wait.until(EC.invisibility_of_element_located(self.dropdown_option))
    #     # time.sleep(1.5)  # AJAX wait for Currency load
    #     event_box = self.wait.until(EC.element_to_be_clickable(self.event_dropdown))
    #     event_box.click()
    #
    #     # 2. Wait for options and select safely
    #     options = self.wait.until(EC.visibility_of_all_elements_located(self.dropdown_option))
    #
    #     # Use requested index if possible, otherwise use index 0
    #     curr_ind = int(event_index) if len(options) > int(event_index) else 0
    #     options[curr_ind].click()
    #
    #     # Wait for dropdown to close and AJAX to load Currencies
    #     self.wait.until(EC.invisibility_of_element_located(self.dropdown_option))
    #     time.sleep(1.5)
    #     # 3. Open Currency Dropdown
    #     curr_box = self.wait.until(EC.element_to_be_clickable(self.currency_dropdown))
    #     curr_box.click()
    #
    #     curr_options = self.wait.until(EC.visibility_of_all_elements_located(self.dropdown_option))
    #     curr_options[int(currency_index)].click()
    #     self.wait.until(EC.invisibility_of_element_located(self.dropdown_option))
    #
    #     # 4. Remarks and Create
    #     self.driver.find_element(*self.remarks_input).send_keys(str(remarks))
    #
    #     # Use JS Click for 'Create' as it often gets blocked by lingering animations
    #     create_btn = self.wait.until(EC.element_to_be_clickable(self.create_button))
    #     self.driver.execute_script("arguments[0].click();", create_btn)

    def initiate_new_claim2(self, event_index, currency_index, remarks):
        # 1. Select Event using Keyboard
        event_field = self.wait.until(EC.element_to_be_clickable(self.event_dropdown))
        event_field.click()
        # Press Arrow Down based on index, then Enter to select
        for _ in range(int(event_index)):
            event_field.send_keys(Keys.ARROW_DOWN)
        event_field.send_keys(Keys.ENTER)

        # 2. WAIT FOR AJAX - Essential for Currency to populate based on Event
        time.sleep(2)

        # 3. Select Currency using Keyboard
        curr_field = self.wait.until(EC.element_to_be_clickable(self.currency_dropdown))
        curr_field.click()
        for _ in range(int(currency_index)):
            curr_field.send_keys(Keys.ARROW_DOWN)
        curr_field.send_keys(Keys.ENTER)

        # 4. Remarks and Create
        self.driver.find_element(*self.remarks_input).send_keys(str(remarks))

        # JavaScript click for Create to ensure it's not blocked by lingering dropdowns
        create_btn = self.wait.until(EC.element_to_be_clickable(self.create_button))
        self.driver.execute_script("arguments[0].click();", create_btn)

    def initiate_new_claim(self, event_index, currency_index, remarks):
        # 1. Handle Event
        event_box = self.wait.until(EC.element_to_be_clickable(self.event_dropdown))
        event_box.click()

        # Wait for options and filter out the "-- Select --" placeholder if necessary
        options = self.wait.until(EC.visibility_of_all_elements_located(self.dropdown_option))

        # Use index 1 if the list has enough items, otherwise default to the last available
        e_idx = int(event_index) if len(options) > int(event_index) else (len(options) - 1)
        options[e_idx].click()

        # 2. Wait for AJAX Sync
        # This is critical: the Currency dropdown often refreshes/re-renders based on Event
        time.sleep(2)

        # 3. Handle Currency
        curr_box = self.wait.until(EC.element_to_be_clickable(self.currency_dropdown))
        curr_box.click()

        # Re-fetch options (they are dynamic for the Currency popup)
        curr_options = self.wait.until(EC.visibility_of_all_elements_located(self.dropdown_option))

        c_idx = int(currency_index) if len(curr_options) > int(currency_index) else (len(curr_options) - 1)
        curr_options[c_idx].click()

        # 4. Fill Remarks and Create
        self.driver.find_element(*self.remarks_input).send_keys(str(remarks))
        self.wait.until(EC.element_to_be_clickable(self.create_button)).click()

    def initiate_new_claim_last(self, event_index, currency_index, remarks):
        # # Select Event
        # event_box = self.wait.until(EC.element_to_be_clickable(self.event_dropdown))
        # event_box.click()
        #
        # options = self.wait.until(EC.visibility_of_all_elements_located(self.dropdown_option))
        # e_idx = int(event_index) if len(options) > int(event_index) else 1
        # options[e_idx].click()
        #
        # # WAIT FOR AJAX SYNC
        # self.wait.until(EC.invisibility_of_element_located(self.dropdown_option))
        # time.sleep(3)  # Critical for OrangeHRM AJAX sync
        #
        # # Select Currency
        # curr_box = self.wait.until(EC.element_to_be_clickable(self.currency_dropdown))
        # curr_box.click()
        # time.sleep(0.5)
        # for _ in range(int(currency_index)):
        #     curr_box.send_keys(Keys.ARROW_DOWN)
        # curr_box.send_keys(Keys.ENTER)
        #
        # # curr_options = self.wait.until(EC.visibility_of_all_elements_located(self.dropdown_option))
        # #
        # # c_idx = int(currency_index) if len(curr_options) > int(currency_index) else 1
        # # curr_options[c_idx].click()
        # #
        # # self.wait.until(EC.invisibility_of_element_located(self.dropdown_option))

        dropdowns = self.wait.until(EC.presence_of_all_elements_located(self.event_dropdown))

        # Click the first dropdown (Event)
        dropdowns[0].click()

        # Wait for options to be visible and click by index
        event_options = self.wait.until(EC.visibility_of_all_elements_located(self.dropdown_option))
        event_options[int(event_index)].click()

        # 2. Wait for AJAX/Dynamic load of Currency
        # OrangeHRM often refreshes the Currency list based on the Event selection
        time.sleep(1.5)

        # 3. Open and Select Currency
        # Re-fetch dropdowns to avoid StaleElementReferenceException after AJAX load
        dropdowns = self.wait.until(EC.presence_of_all_elements_located(self.currency_dropdown))
        dropdowns[1].click()

        # Wait for options and click
        curr_options = self.wait.until(EC.visibility_of_all_elements_located(self.dropdown_option))
        curr_options[int(currency_index)].click()

        # 4. Remarks and Create
        self.driver.find_element(*self.remarks_input).send_keys(str(remarks))

        create_btn = self.wait.until(EC.element_to_be_clickable(self.create_button))

        try:
            create_btn.click()
        except:
            self.driver.execute_script("arguments[0].click();", create_btn)

    # def initiate_new_claim(self, event_index, currency_index, remarks):
    #     # 1. Open Event Dropdown
    #     event_box = self.wait.until(EC.element_to_be_clickable(self.event_dropdown))
    #     event_box.click()
    #
    #     # 2. Select Event Option
    #     event_options = self.wait.until(EC.visibility_of_all_elements_located(self.dropdown_option))
    #     event_options[int(event_index)].click()
    #
    #     # 3. CRITICAL: Wait for the Currency dropdown to become interactable
    #     # This gives the AJAX call time to populate the second dropdown.
    #     time.sleep(1.5)
    #
    #     # 4. Open Currency Dropdown
    #     # Use find_elements to pick the SECOND dropdown wrapper on the page
    #     curr_boxes = self.driver.find_elements(*self.currency_dropdown)
    #     curr_boxes[1].click()
    #
    #     # 5. Select Currency Option
    #     curr_options = self.wait.until(EC.visibility_of_all_elements_located(self.dropdown_option))
    #     curr_options[int(currency_index)].click()
    #
    #     # 6. Finalize
    #     self.driver.find_element(*self.remarks_input).send_keys(str(remarks))
    #     self.wait.until(EC.element_to_be_clickable(self.create_button)).click()

    def submit_request(self):
        # Click the final Submit button on the Expense details page
        submit_btn = self.wait.until(EC.element_to_be_clickable(self.submit_button))
        submit_btn.click()

    def is_success_message_displayed(self):
        try:
            return self.wait.until(EC.visibility_of_element_located(self.success_toast)).is_displayed()
        except:
            return False