import pytest
from pytest_bdd import scenarios, given, when, then, parsers
from pages.login_pages import LoginPage
from pages.logout_pages import LogoutPage

# Link to the feature file
scenarios("..//features/authentication.feature")

@pytest.fixture
def login_page(driver):
    """Fixture to initialize LoginPage"""
    return LoginPage(driver)

@pytest.fixture
def logout_page(driver):
    """Fixture to initialize LogoutPage"""
    return LogoutPage(driver)


@given("user is on zen portal login page")
def zen_launch(driver):
    # The URL navigation is handled by your conftest.py driver fixture
    pass

@given("user validates user name and password")
def validate_authenticationfields(login_page):
    # Validates visibility and state of input boxes (OOPs + Exceptions)
    login_page.validate_zenportalfields()

@given("user validates submit button")
def validate_submit_button(login_page):
    # Validates if submit button is working/enabled
    login_page.validate_zensubmit()


@when(parsers.cfparse('user keys in username "{username}" and password "{password}"'))
def enter_logincredentials(login_page, username, password):
    login_page.enter_credentials("", "")
    login_page.enter_credentials(username, password)

@when(parsers.cfparse('user keys username "{username}" and invalid password "{password}"'))
def enter_invalid_credentials(login_page, username, password):
    login_page.enter_credentials(username, password)

@when("clicks on the login button")
def click_login_button(login_page):
    login_page.click_login()


@then("user should be navigated to zen dashboard")
def verify_user_loggedin(login_page):
    # Validates successful navigation
    login_page.validate_zennavigation()

@then("user should be not be navigated to zen dashboard")
def check_failed_login(login_page):
    # Validates unsuccessful login functionality
    login_page.verify_unsuccessfullogin()

@then("user logsout of zen dashboard")
def user_logout(logout_page):
    # Handles profile click and logout button click
    logout_page.logsout()

@then("user should be redirected to login page")
def user_redirect(logout_page):
    # Validates logout functionality by checking URL/Title
    logout_page.checkLogout_functionality()