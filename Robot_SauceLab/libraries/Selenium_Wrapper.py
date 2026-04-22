import os.path
import time

import selenium
from robot.api import logger
from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.common.by import By

# class SeleniumWrapper:
#     def __init__(self):
#         driver =None

def start_browser(browser, url):
    global driver

    if browser == "Chrome":
        chrome_options = ChromeOptions()
        chrome_options.add_argument("--disable-notifications")
        driver = webdriver.Chrome(chrome_options)
    elif browser =="Firefox":
        firefox_options = FirefoxOptions()
        firefox_options.set_preference("dom.webnotifications.enabled", False)
        firefox_options.set_preference("dom.push.enabled", False)  # Disables the underlying push service
        driver = webdriver.Firefox(firefox_options)

    driver.get(url)
    driver.maximize_window()

def close_browser():
    driver.quit()

def find_element(locator_type, locator_value):
    try:
        if locator_type =="id":
            return driver.find_element(By.ID, locator_value)
        elif locator_type =="xpath":
            return driver.find_element(By.XPATH, locator_value)
    except NoSuchElementException:
       logger.debug("Failed to Find The Element")

def click( locator_type, locator_value, element_name):
    try:
        find_element(locator_type, locator_value).click()
        logger.info(element_name + " Is Clicked")
    except:
        logger.debug("Failed to Click On"+ element_name)

def enter_text(locator_type, locator_value, text, element_name):
    try:
        find_element(locator_type, locator_value).send_keys(text)
        logger.info("Entered Value in "+element_name+ "Value:"+text)
    except Exception as e:
        logger.info(e)
        logger.info("Failed to Enter value in" + element_name)

def get_text(locator_type, locator_value, element_name):
    try:
        text = find_element(locator_type, locator_value).text
        logger.info("Got The Text From" + element_name + "Text Is:" + text)
    except:
        logger.info("Failed to get Text From" + element_name)
        text =""

    return text

def switch_to_new_window():
    windows = driver.window_handles
    driver.switch_to.window(windows[1])

def verify_url(expected_url):
    actual_url = driver.current_url
    assert actual_url == expected_url, f"Landed on {expected_url} page and actually {actual_url}"

def take_screenshot(step_name="step"):
    screenshot_dir = os.path.join(os.getcwd(), "screenshots")
    os.makedirs(screenshot_dir, exist_ok=True)

    file_path = os.path.join(screenshot_dir, f"{step_name}_{int(time.time())}.png")
    driver.save_screenshot(file_path)

    logger.info(f'<img src="{file_path}" width="384px" >', html=True)

