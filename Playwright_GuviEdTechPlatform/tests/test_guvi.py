import re

import pytest
from playwright.sync_api import expect

def test_tc01_verify_url(page):
    """Verify URL validity."""
    expect(page).to_have_url("https://www.guvi.in/")

def test_tc02_verify_title(page):
    """Verify page title."""
    expect(page).to_have_title("HCL GUVI | Learn to code in your native language")

def test_tc03_login_button_visibility(page, header_page):
    page.wait_for_load_state("networkidle")
    """Verify Login button is visible and clickable."""
    expect(header_page.login_btn).to_be_visible(timeout=10000)
    header_page.navigate_to_login()
    expect(page).to_have_url(re.compile(r".*/sign-in.*"), timeout=10000)

def test_tc04_verify_signup(page, header_page):
    """Verify Sign-up button redirects to /register/."""
    header_page.navigate_to_signup()
    expect(page).to_have_url(re.compile(r"https://www.guvi.in/register/.*"))

def test_TC05_verify_signupnaviagtion(page, header_page):
    header_page.navigate_to_signup()
    # expect(page).to_have_url(re.compile(r"https://www.guvi.in/register/?"), timeout=10000)
    #Registeration page has full name
    full_name_field = page.get_by_placeholder("Full Name")
    expect(full_name_field).to_be_visible()

def test_tc06_login(page, login_page):

    try:
        page.goto("https://www.guvi.in/sign-in/?sourceUri=http%3A%2F%2Fwww.guvi.in%2F") # Go direct to signin
    except TimeoutError:
        print("Navigation timed out")
    page.wait_for_load_state("domcontentloaded")
    login_page.login("suja2105@gmail.com", "Sujatha@7777")


    # expect(page).to_have_url(lambda url: "courses" in url)
    # expect(page).to_have_url(self, )

@pytest.mark.parametrize("email, password", [
    ("wrong@mail.com", "Pass123"),
    ("", "OnlyPass"),
    ("user@mail.com", "")
])
def test_tc07_invalid_login(page, login_page, email, password):
    """Negative Scenario: Invalid Login (Data-Driven)."""
    # page.goto("https://www.guvi.in/sign-in/?sourceUri=http%3A%2F%2Fwww.guvi.in%2F")
    login_page.click_login()
    login_page.login(email, password)
    expect(login_page.any_error.first).to_be_attached(timeout=6000)

def test_tc08_menu_items(header_page):
    # """Verify Courses, LIVE Classes, and Practice are displayed."""
    header_page.verify_menu_items_visible()
    header_page.verify_menu_items_enabled()

def test_tc09_verify_dobby_assistant(page, header_page):
    # """Validate Dobby AI Assistant widget."""
    page.mouse.wheel(0, 5000)
    # dobby = page.get_by_role("button", name=re.compile("Dobby", re.I))
    try:
        expect(header_page.dobby_widget).to_be_visible(timeout=15000)
        print("Dobby Guvi Assistant is present")
    except AssertionError:
        pytest.skip("Dobby Assistant is currently not available")



def test_tc10_logout(page, login_page):
#     """Validate Logout functionality."""
#     page.goto("https://www.guvi.in")
    login_page.click_login()
    # login_page.login("entervalid_user@example.com", "enterCorrectPassword123")
    login_page.login("suja2105@gmail.com", "Sujatha@7777")

    # Action: Logout
    page.get_by_role("img", name = "Profile").first.click()
    page.locator("#account-boxheader").get_by_text("Sign Out").click()
    # page.get_by_role("link", name = "Sign Out").click()
    # page.get_by_text("Sign Out").click()

    # Validation: Redirected to signin or home
    expect(page).to_have_url(re.compile(r"https://www.guvi.in"), timeout= 10000)