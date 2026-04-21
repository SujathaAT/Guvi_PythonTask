import allure
import pytest
from selenium import webdriver


@pytest.fixture(scope='function')
def driver():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--disable-notifications")
    chrome_options.add_argument("--disable-popup-blocking")  # Blocks separate windows

    driver = webdriver.Chrome(chrome_options)
    driver.get("https://www.zenclass.in/login")
    yield driver
    driver.quit()


def pytest_sessionstart(session):
    print("==== Test session started")

def pytest_sessionfinish(session, exitstatus):
    print("=== Test Session Finished++++")


def pytest_collection_modifyitems(config, items):
    for item in items:
        if "login" in item.nodeid:
            item.add_marker(pytest.mark.login)
        elif "logout" in item.nodeid:
            item.add_marker(pytest.mark.logout)

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    # Run all other hooks to get the report object
    outcome = yield
    report = outcome.get_result()

    # Only act on test call failures
    if report.when == "call" and report.failed:
        # Force fixture resolution here
        driver = None
        try:
            driver = item._request.getfixturevalue("driver")
        except Exception:
            pass

        if driver:
            screenshot = driver.get_screenshot_as_png()
            allure.attach(
                screenshot,
                name="screenshot_on_failure",
                attachment_type=allure.attachment_type.PNG
            )
