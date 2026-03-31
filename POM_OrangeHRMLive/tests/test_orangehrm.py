import os
import random
import string
import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

from pages.dashboard import DashboardPage
from pages.loginpage import LoginPage
from pages.adminpage import AdminPage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.forgotpasswordpage import ForgotPasswordPage
from pages.myinfopage import MyInfoPage
from pages.leavepage import LeavePage
from pages.claimpage import ClaimPage

from utils.common_util import savescreenshot, click_element_by_text
from utils.excel_resder import DataHandler
#
#
# def test_TC1_ValidateLogin(driver):
#     current_dir = os.path.dirname(os.path.abspath(__file__))
#     test_data_path = os.path.join(current_dir, '..', 'testdata', 'testdata.csv')
#     test_data_path = os.path.normpath(test_data_path)
#
#     # Initialize components
#     handler = DataHandler(test_data_path)
#     test_data = handler.get_test_rows()
#
#     # driver = webdriver.Chrome()
#     login_pg = LoginPage(driver)
#
#     #Emptying already stored results
#     for row in test_data:
#         tc_id  = row['Test_id']
#         cleanup_text = "<Result>"
#
#         #Cleanup previously store results - last run
#         handler.save_result(tc_id, cleanup_text)
#         print(f"Initialized results: {tc_id} -> {cleanup_text}")
#
#     for row in test_data:
#         tc_id  = row['Test_id']
#         user_name = str(row['Username'])
#         pwd = str(row['Password'])
#
#         try:
#             # driver.get("https://opensource-demo.orangehrmlive.com")
#             login_pg.login(user_name, pwd)
#
#             # Explicit wait for login pass or fail
#             WebDriverWait(driver, 7).until(
#                 lambda d: "dashboard" in d.current_url or
#                           len(d.find_elements(By.XPATH, "//*[contains(@class, 'oxd-alert')]")) > 0
#             )
#
#             if "dashboard" in driver.current_url.lower():
#                 result_text = "PASS"
#                 login_pg.logout()
#             else:
#                 result_text = "Pass: Invalid Credentials"
#
#         except Exception:
#             result_text = "FAIL: Timeout/Error"
#
#         # Write back to CSV result column
#         handler.save_result(tc_id , result_text)
#         print(f"Update: {tc_id } -> {result_text}")
#
#         if "dashboard" not in driver.current_url:
#             # Generate a unique filename using a timestamp
#             timestamp = time.strftime("%Y%m%d-%H%M%S")
#             file_name = f"TC1_login_failure_{timestamp}.png"
#
#             # Save the screenshot
#             driver.save_screenshot(file_name)
#             print(f"Login failed. Screenshot saved as: {file_name}")
#
#     driver.quit()
#
# def test_TC2_ValidateURLAccessibility(driver):
#     url_match = "orangehrmlive.com"
#     url = driver.current_url
#     login_pg = LoginPage(driver)
#
#     assert login_pg.is_login_button_displayed(), "Fail Login button is not displayed"
#     try:
#         assert url_match in url, f" Fail URL {url} did not match"
#         print("Success: URL is accessible")
#     except AssertionError as e:
#
#         timestamp = time.strftime("%Y%m%d-%H%M%S")
#         file_name = f"TC2_URL_Accessible_{timestamp}.png"
#
#         # Save the screenshot
#         driver.save_screenshot(file_name)
#         raise e
#
# def test_TC3_ValidateLoginfieldsPresence(driver):
#     TC_Name = "TC3_login_presence"
#     login_pg = LoginPage(driver)
#
#     check_status = login_pg.verify_login_fields_presence()
#     try:
#         assert check_status is True
#
#     except AssertionError as e:
#         savescreenshot(driver,TC_Name )
#         raise AssertionError(f"{TC_Name} Validation failed for login fields as presence is: {check_status}")
#
# def test_TC4_ValidateMenuItems(driver, get_yamldata):
#     login_pg = LoginPage(driver)
#     user = get_yamldata['username']
#     pwd = get_yamldata['password']
#     login_pg.login(user, pwd)
#     dashboard_pg = DashboardPage(driver)
#     menu_items = ["Admin", "PIM", "Leave", "Time",
#         "Recruitment", "My Info", "Performance", "Dashboard"]
#
#     non_clickable_items = []
#     for item in menu_items:
#         dashboard_pg.is_menu_item_clickable(item)
#         if not dashboard_pg.is_menu_item_clickable(item):
#             non_clickable_items.append(item)
#
#     assert len(non_clickable_items) == 0, f"Fail {non_clickable_items}- were not clickable"
# 
# def test_TC5_CreateUser(driver, get_yamldata):
#     login_pg = LoginPage(driver)
#     admin_pg = AdminPage(driver)
#
#     random_suffix = ''.join(random.choices(string.digits, k=5))
#     user = get_yamldata['username']
#     pwd = get_yamldata['password']
#
#     new_user = get_yamldata['new_user']
#     new_pwd = get_yamldata['new_pwd']
#     emp_name = get_yamldata['emp_name']
#     new_user = f"{new_user}_{random_suffix}"
#     login_pg.login(user, pwd)
#
#     click_element_by_text(driver, "Admin","span")
#
#     admin_pg.create_user(emp_name,new_user,new_pwd)
#     login_pg.logout()
#     login_pg.login(new_user, new_pwd)
#     WebDriverWait(driver, 10).until(EC.url_contains("dashboard"))
#     assert "dashboard" in driver.current_url

#
# def test_TC6_ValidateUserInList(driver, get_yamldata):
#     login_pg = LoginPage(driver)
#     admin_pg = AdminPage(driver)
#
#     random_suffix = ''.join(random.choices(string.digits, k=5))
#     new_user = f"{get_yamldata['new_user']}_{random_suffix}"
#     emp_name = "a"  # Use 'a' to ensure a valid hint selection
#
#     login_pg.login(get_yamldata['username'], get_yamldata['password'])
#     admin_pg.click_admin()
#     admin_pg.create_user(emp_name, new_user, get_yamldata['new_pwd'])
#
#     admin_pg.search_user(new_user)
#
#     found = admin_pg.is_user_present_in_list(new_user)
#     assert found is True, f"User {new_user} was not found in the admin list!"

# def test_TC7_Verifyforgotuser(driver):
#     driver.get("https://opensource-demo.orangehrmlive.com/")
#     login_page = LoginPage(driver)
# 
#     login_page.click_forgot_password()
# 
#     # Enter registered username and submit
#     forgot_pw_page = ForgotPasswordPage(driver)
#     forgot_pw_page.enter_username("Admin")
#     forgot_pw_page.click_reset_password()
# 
#     # Verify confirmation message
#     expected_message = "Reset Password link sent successfully"
#     actual_message = forgot_pw_page.get_confirmation_text()
# 
#     assert expected_message in actual_message, f"Expected {expected_message}, but got {actual_message}"
#     assert "sendPasswordReset" in driver.current_url, "User was not redirected to the reset confirmation page"

def test_TC8_Verify_MyInfoMenuItems(driver):
    # driver.get("https://opensource-demo.orangehrmlive.com/")
    login_page = LoginPage(driver)
    login_page.login("Admin", "admin123")

    my_info = MyInfoPage(driver)
    my_info.navigate_to_my_info()

    # Define Sub-Menu Items
    expected_items = [
        "Personal Details",
        "Contact Details",
        "Emergency Contacts",
        "Dependents",
        "Immigration",
        "Job",
        "Salary"
    ]

    actual_items = my_info.get_all_sub_menu_names()
    for item in expected_items:
        assert item in actual_items, f"Menu item '{item}' not found in My Info section"

    my_info.click_sub_menu_item("Contact Details")
    assert "contactDetails" in driver.current_url, "Failed to navigate to Contact Details page"

def test_TC9_Assignleave(driver):
    login_page = LoginPage(driver)
    login_page.login("Admin", "admin123")

    # Navigate and Fill Form
    leave_page = LeavePage(driver)
    leave_page.navigate_to_assign_leave()

    # Dates should be in future to avoid "Balance Not Sufficient" or "Past Date" errors
    leave_page.fill_assign_leave_form("a", "2026-10-10", "2026-10-12")

    # Submit and Assert
    leave_page.submit_assignment()

    assert leave_page.is_success_message_displayed(), "Success message for leave assignment was not found"

def test_TC10_InitiateClaim(driver, get_yamldata):

    login_page = LoginPage(driver)
    user = get_yamldata['username']
    pwd = get_yamldata['password']
    event = get_yamldata['event_ind']
    currency = get_yamldata['curr_index']
    remark = get_yamldata['remarks']
    login_page.login(user,pwd)

    # Navigate and Fill Initial Claim Form
    claim_page = ClaimPage(driver)
    claim_page.navigate_to_submit_claim()

    # Select second event and currency from dropdowns
    claim_page.initiate_new_claim(event, currency, remark)

    # Submit Request
    claim_page.submit_request()

    assert claim_page.is_success_message_displayed(), "Claim submission success message was not found"