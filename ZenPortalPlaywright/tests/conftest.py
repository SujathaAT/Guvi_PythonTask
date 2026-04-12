import os

import pytest
import yaml
from playwright.sync_api import sync_playwright


@pytest.fixture()
def zen_page():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()
        # page.goto("https://www.zenclass.in/login")
        page.goto("https://www.zenclass.in")

        yield page

        context.close()
        browser.close()




@pytest.fixture(scope="session")
def get_yamldata():
    YAML_FILE = "zenportal.yaml"

    root = os.path.dirname(__file__)
    data_path = os.path.join(root,"..", "testdata", f"{YAML_FILE}")

    print(data_path)
    # print(data_path)
    with open(data_path) as f:
        data = yaml.safe_load(f)
    test_data =  data["user"]
    return test_data
