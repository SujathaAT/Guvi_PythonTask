import time
from selenium import webdriver
from selenium.webdriver.common.by import By

from selenium.webdriver.chrome.options import Options

def test_guvi():

    options =  Options()
    options.add_argument("--headless=new")

    driver = webdriver.Chrome(options = options)
    driver.maximize_window()
    driver.implicitly_wait(5)
    driver.get("https://www.guvi.in")
    #driver.refresh()
    #time.sleep(10)
    #chat_wind = driver.find_element(By.XPATH,"//div[@class = 'call-prof-cont']").is_displayed()
    #chatclose = driver.find_element(By.XPATH,"//div/span[contains(@aria-label, 'chat')]").is_displayed()
    #if chat_wind == True:
        #driver.find_element(By.XPATH,"//div/span[contains(@aria-label, 'chat')]").click()
    #time.sleep(5)

    driver.find_element(By.XPATH, "//div/a[@id = 'login-btn']").click()
    checkSignIn = driver.current_url
    assert "https://www.guvi.in/sign-in/" == checkSignIn, "Navigated to Sign-In URL"

    email_id = driver.find_element(By.ID, "email")
    emailEnabledFlag = email_id.is_enabled()
    emailVisibleFlag = email_id.is_displayed()
    assert emailEnabledFlag == True, "Email ID is enabled"
    assert emailVisibleFlag == True, "Email id is visible"

    # Enter email-id/
    if emailEnabledFlag == True and emailVisibleFlag == True:
        email_id.send_keys("suja2105@gmail.com")
    # Enter password
    password = driver.find_element(By.ID, "password")
    if password.is_displayed() == True and password.is_enabled():
        password.send_keys("Sujatha@7777")
    #time.sleep(10)

    #checkLoginbtn = driver.find_element(By.XPATH, "//a[contains(@id, 'login')]").is_displayed()
    #assert  checkLoginbtn == True, "Login button is displayed"
    ##if (checkLoginbtn == True):
    driver.find_element(By.XPATH, "//a[contains(@id, 'login')]").click()
    #time.sleep(2)
    checkloginsuccess = driver.title
    checkstring = "courses"
    if checkstring in checkloginsuccess:
        print("Submit button is working. Navigated to courses page")
    #assert "https://www.guvi.in/courses/?current_tab=myCourses" == checkloginsuccess, "Navigated to Guvi Courses"
    driver.close()
    driver.quit()


def test_VoidCredentials():
    options = Options()
    options.add_argument("--headless=new")

    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    driver.implicitly_wait(5)

    driver.get("https://www.guvi.in")

    if driver.find_element(By.XPATH, "//div/a[@id = 'login-btn']").is_displayed() == False:
        driver.find_element(By.XPATH, "//div/span[contains(@aria-label, 'chat')]").click()

    driver.find_element(By.XPATH, "//div/a[@id = 'login-btn']").click()
    loginbtn = driver.find_element(By.XPATH, "//a[contains(@id, 'login')]")
    #driver.execute_script("arguments[0].focus();", loginbtn)
    driver.execute_script("arguments[0].scrollIntoView();", loginbtn)

    driver.find_element(By.XPATH, "//a[contains(@id, 'login')]").click()

    ErrorMsg = driver.find_element(By.XPATH,"//div[contains(text(), 'forgot your password')]")
    driver.execute_script("arguments[0].scrollIntoView();", ErrorMsg)

    assert ErrorMsg.is_displayed()== True , "Error Message is displayed"

    driver.close()
    driver.quit()
