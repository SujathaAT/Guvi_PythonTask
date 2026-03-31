import os
from pathlib import Path

import allure
import pytest
import yaml
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.fixture(scope='function')
def driver():
    options = Options()
    options.add_argument("--disable-notifications")
    options.add_argument("--start-maximized")
    options.page_load_strategy = 'eager'
    options.add_experimental_option("detach", True)
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    driver = webdriver.Chrome(options=options)
    # driver.set_page_load_timeout(30)
    driver.set_script_timeout(10)
    driver.get("https://opensource-demo.orangehrmlive.com")
    driver.maximize_window()
    yield driver
    driver.quit()


def pytest_sessionstart(session):
    print("==== Test session started")
    print("   Orange HRM Automation    ")

def pytest_sessionfinish(session, exitstatus):
    print("=== Test Session Finished====")


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    # Execute the actual test and get the result
    outcome = yield
    report = outcome.get_result()

    # We only care about the 'call' phase (when the test actually runs)
    if report.when == 'call' and report.failed:
        try:
            # 1. Retrieve the driver from the test fixture
            # 'item.funcargs' is the most reliable way to get fixtures
            driver = item.funcargs.get("driver")

            if driver:
                # 2. Attach the screenshot directly to the Allure report
                allure.attach(
                    driver.get_screenshot_as_png(),
                    name="screenshot_on_failure",
                    attachment_type=allure.attachment_type.PNG
                )
        except Exception as e:
            print(f"Failed to capture screenshot: {e}")


@pytest.fixture(scope="session")
def get_yamldata():
    YAML_FILE = "common_data.yaml"

    root = os.path.dirname(__file__)
    data_path = os.path.join(root, "..", 'testdata', f"{YAML_FILE}")

    print(data_path)

    with open(data_path) as f:
        data = yaml.safe_load(f)
    test_data =  data["user"]
    return test_data
