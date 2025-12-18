import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

def test_locateelement():
    driver.get("https://www.guvi.in/")
    xpath_list =   ("//div/a[contains(text(), 'Courses')]/parent::*",
                    "//div/a[contains(text(), 'Courses')]/parent::*/child::a",
                    "//div/a[contains(text(), 'Courses')]//following-sibling::div",
                    "//div/a[contains(text(), 'Courses')]//preceding-sibling::div",
                    "//div/a[contains(text(), 'Courses')]//following-sibling::div[2]",
                    "//div/a[@href ='/courses/']",
                    "//div/a[@href ='/courses/']",
                    "//p[contains(text(), 'Class')]/parent::*",
                    "//p[contains(text(), 'Class')]/parent::*/child::*",
                    "//p[contains(text(), 'Class')]/ancestor::div",
                    "//p[contains(text(), 'Practice')]/parent::*",
                    "//p[contains(text(), 'Practice')]/parent::*/child::*",
                    "//p[contains(text(), 'Practice')]//following-sibling::*",
                    "//p[contains(text(), 'Practice')]//following-sibling::*[2]",
                    "//p[contains(text(), 'Practice')]/ancestor::div",
                    "//p[contains(text(), 'Resources')]/parent::*",
                    "//p[contains(text(), 'Resources')]/parent::*/child::*",
                    "//p[contains(text(), 'Resources')]//following-sibling::*",
                    "//p[contains(text(), 'Resources')]/ancestor::div",
                    "//p[contains(text(), 'Products')]",
                    "//p[contains(text(), 'Products')]/parent::*",
                    "//p[contains(text(), 'Products')]/parent::*/child::*",
                    "//p[contains(text(), 'Products')]//following-sibling::*",
                    "//p[contains(text(), 'Products')]//following-sibling::*[2]",
                    "//p[contains(text(), 'Products')]//ancestor::div",
                    "//button[contains(text(), 'Login') or@id=login-btn]"
                    "//button[contains(text(), 'Login') or@id=login-btn]/parent::*",
                    "//button[contains(text(), 'Login') or@id=login-btn]/parent::*/child::*",
                    "//button[contains(text(), 'Login') or@id=login-btn]//following-sibling::*",
                    "//button[contains(text(), 'Login') or@id=login-btn]//ancestor::div",
                    "//button[contains(text(), 'Sign up')]/parent::*",
                    "//button[contains(text(), 'Sign up')]/parent::*/child::*",
                    "//button[contains(text(), 'Sign up')]//ancestor::div"
                    )
    checkelement(driver, xpath_list)
    time.sleep(10)

def checkelement(driver,element):
    for xpath in element:
        try:
            curr_ele = driver.find_element(By.XPATH, xpath)
            print(f"Found element : {curr_ele.tag_name}")
        except:
            print(f"Element not found")