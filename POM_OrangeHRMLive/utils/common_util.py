import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


def verify_fields_presence(driver, element_locator):
    try:
        element = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(element_locator))

        flag1 = element.is_displayed()
        flag2 = element.is_enabled()
        return flag1 and flag2
    except:
        return False

def click_element_by_text(driver, text, tag, timeout=10):
    locator = f"//{tag}[text()='{text}']"
    if tag is None:
        tag = "span"
    try:
        element = WebDriverWait(driver, timeout).until(
            EC.element_to_be_clickable((By.XPATH, locator))
        )
        element.click()
    except Exception as e:
        print(f"Error: Could not click {tag} with text '{text}'. Exception {e}")


def savescreenshot(driver,TC_name):
    timestamp = time.strftime("%Y%m%d-%H%M%S")
    file_name = f"{TC_name}_{timestamp}.png"

    # Save the screenshot
    driver.save_screenshot(file_name)
