import time

import pytest
import yaml
import random

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Load Data-Driven values from YAML
with open("testdata/common_data.yaml", "r") as f:
    config = yaml.safe_load(f)


def get_credentials():
    # with open("testdata/common_data.yaml", "r") as f:
    #     data = yaml.safe_load(f)
    return config['verify_credentials']

def get_sorting_data():
    return config['sorting_test_data']

# --- TC-1: Login with various predefined users (Data-Driven) ---
@pytest.mark.parametrize("user", config['test_users'])
def test_tc1_predefined_user_login(driver, keywords, user):
    """Verify login behavior for different roles (Standard, Locked, Glitch)."""
    is_success = keywords.keyword_login_and_verify(user['username'], user['password'])

    if user['type'] == "valid":
        assert is_success, f"Valid user {user['username']} failed to login."
        assert "inventory.html" in driver.current_url
    else:
        # Expected failure for locked_out_user
        assert not is_success, f"Invalid user {user['username']} logged in unexpectedly."
        assert "locked out" in keywords.login_page.get_error_message().lower()


# --- TC-2: Login with invalid credentials (Data-Driven) ---
@pytest.mark.parametrize("invalid", config['invalid_credentials'])
def test_tc2_invalid_credentials(keywords, invalid):
    """Attempt login with non-standard credentials and validate denial."""
    keywords.login_page.login(invalid['username'], invalid['password'])
    error_text = keywords.login_page.get_error_message()
    assert "Username and password do not match" in error_text


# # --- TC-3: Validate logout functionality ---
@pytest.mark.parametrize("verify", config['verify_credentials'])
def test_tc3_logout_validation(driver, keywords, verify):
    """Check if logout button works and redirects to login screen."""
    # keywords.keyword_login_and_verify("standard_user", "secret_sauce")
    keywords.keyword_login_and_verify(verify['username'], verify['password'])

    # Keyword-driven logout via POM
    keywords.inventory_page.logout()

    #Wait for URL to change to Login page
    # WebDriverWait(driver, 10).until(EC.url_to_be("https://www.saucedemo.com"))
    WebDriverWait(driver, 10).until(EC.url_contains("saucedemo.com"))

    # Verify redirection to login page
    assert driver.current_url == "https://www.saucedemo.com/" or "index.html" in driver.current_url
    assert keywords.login_page.find_element(keywords.login_page.LOGIN_BUTTON).is_displayed()

#
# # --- TC-4: Check cart icon visibility ---
@pytest.mark.parametrize("verify", config['verify_credentials'])
def test_tc4_cart_icon_visibility(keywords, verify):
    """Verify cart icon is visible on the product listing page post login."""
    keywords.keyword_login_and_verify(verify['username'], verify['password'])
    # time.sleep(5)
    # Validation of UI element visibility via POM locator
    cart_element = keywords.inventory_page.find_element(keywords.inventory_page.CART_ICON)
    assert cart_element.is_displayed(), "Cart icon is missing after login."

#
# # --- TC-5: Random selection of products and data extraction ---
@pytest.mark.parametrize("verify", config['verify_credentials'])
def test_tc5_random_product_selection(keywords, verify):
    """Randomly select 4 products and fetch their names and prices."""
    keywords.keyword_login_and_verify(verify['username'], verify['password'])

    # POM logic handles the random sampling of 4 out of 6 items
    product_data = keywords.inventory_page.get_random_products_and_add(count=4)

    # Verify exactly 4 products were extracted
    assert len(product_data) == 4

    # Log data for the report (use pytest -s to see this output)
    print("\n--- Extracted Product Data ---")
    for item in product_data:
        print(f"Product: {item['name']} | Price: {item['price']}")
        assert item['name'] != "", "Product name should not be empty."
        assert "$" in item['price'], "Price format is incorrect."

# @pytest.mark.parametrize("verify", config['verify_credentials'])
@pytest.mark.parametrize("verify", get_credentials())
def test_tc6_tc7_tc8_cart_and_checkout(keywords, verify, driver):
    # TC-6: Add random products
    keywords.keyword_login_and_verify(verify['username'], verify['password'])
    inventory = keywords.inventory_page
    added_items = inventory.get_random_products_and_add(4)
    assert inventory.get_cart_count() == "4"

    # TC-7: Validate details in cart
    inventory.click_element(inventory.CART_ICON)
    cart = keywords.cart_page
    displayed_names = cart.get_cart_item_names()
    for item in added_items:
        assert item['name'] in displayed_names

    # TC-8: Checkout and Summary
    # cart.proceed_to_checkout("John", "Doe", "12345")
    checkout_info = config['checkout_data']

    keywords.cart_page.proceed_to_checkout(
        checkout_info['first_name'],
        checkout_info['last_name'],
        checkout_info['zip_code']
    )
    driver.save_screenshot("screenshots/order_summary.png")
    cart.finish_order()
    assert "Thank you" in cart.get_confirmation_msg()

@pytest.mark.parametrize("sort_data", get_sorting_data())
@pytest.mark.parametrize("verify", config['verify_credentials'])
def test_tc9_sorting(keywords, verify, sort_data):
    keywords.keyword_login_and_verify(verify['username'], verify['password'])
    inventory = keywords.inventory_page

    actual_list = keywords.keyword_verify_sorting(sort_data['option'])
    time.sleep(5)
    # Assert: Verify sorting logic
    if sort_data['type'] == "alphabetical_desc":
        expected_list = sorted(actual_list, reverse=True)
        print(f"expected_list: {expected_list}")
        assert actual_list == expected_list, f"Alpha Z-A sort failed: {actual_list}"

    elif sort_data['type'] == "price_asc":
        expected_list = sorted(actual_list)
        assert actual_list == expected_list, f"Price Low-High sort failed: {actual_list}"

@pytest.mark.parametrize("verify", config['verify_credentials'])
def test_tc10_reset_state(driver, keywords, verify):
    keywords.keyword_login_and_verify(verify['username'], verify['password'])
    inventory = keywords.inventory_page
    inventory.get_random_products_and_add(2)

    inventory.reset_app_state()
    driver.refresh()  # Refresh to see UI update
    assert inventory.get_cart_count() == "0"
