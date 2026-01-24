import logging

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

@pytest.fixture(scope='session')
def driver():
    options = Options()
    options.add_argument("--start-maximized")
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-notifications")
    options.add_experimental_option("detach", True)
    options.add_argument("--log-level=3")
    driver = webdriver.Chrome(options=options)

    logging.getLogger("requests").setLevel(logging.WARNING)

    driver.get("https://www.theworldcounts.com/challenges/planet-earth/state-of-the-planet/world-population-clock-live")

    return driver

