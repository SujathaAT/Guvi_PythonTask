


def test_saucelabs():

    import time
    from selenium import webdriver
    from selenium.webdriver.common.by import By

    driver = webdriver.Chrome()

    driver.get("https://www.saucedemo.com/")
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()
    time.sleep(10)

    title = driver.title
    curr_url = driver.current_url
    contents = driver.find_element(By.TAG_NAME, "html").text

    filename = "Webpage_Task10.txt"
    with open(filename, "w") as f:
        f.write("Title : " + title + "/n")
        f.write("URL :" + curr_url + "/n")
        f.write(" \n ")
        f.write(contents)

    print(f"File '{filename}' written successfully")
