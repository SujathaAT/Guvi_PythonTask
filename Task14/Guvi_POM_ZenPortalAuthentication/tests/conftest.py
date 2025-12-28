import os
from pathlib import Path

import pytest
import yaml
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

@pytest.fixture(scope='function')
def driver():
    options = Options()
    options.add_argument("--disable-notifications")
    options.add_argument("--start-maximized")
    options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(options=options)
    driver.get("https://www.zenclass.in/")

    return driver


# @pytest.fixture(scope="session")
# def env_config():
#     YAML_FILE = "Zen_data.yaml"
#     #env = request.config.getoption("--env")
#     root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
#     filepath = os.path.join(root, 'testdata', f"{YAML_FILE}")
#     # path = os.path.join("config", f"{env}_env_config.yaml")
#     # abpath = os.path.abspath(path)
#     # print(abpath)
#     with open(filepath) as f:
#         return yaml.safe_load(f)


@pytest.fixture(scope="session")
def get_yamldata():
    YAML_FILE = "Zen_data.yaml"

    root = os.path.dirname(__file__)
    data_path = os.path.join(root, "..", 'testdata', f"{YAML_FILE}")

    print(data_path)
    # print(data_path)
    with open(data_path) as f:
        data = yaml.safe_load(f)
    test_data =  data["user"]
    return test_data
