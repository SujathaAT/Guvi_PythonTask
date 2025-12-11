import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By



def test_draganddrop():
    driver = webdriver.Chrome()
    driver.get("https://jqueryui.com/droppable/")
    driver.switch_to.frame(0)
    drag_ele = driver.find_element(By.XPATH, "//div[@id = 'draggable']")
    drop_ele = driver.find_element(By.XPATH, "//div[@id = 'droppable']")

    actions = ActionChains(driver)
    actions.drag_and_drop(drag_ele, drop_ele).perform()
    time.sleep(5)
    assert drop_ele.text == "Dropped!", "Drag and Dropped actions performed"

    driver.switch_to.default_content()
    driver.close()
    driver.quit()


def test_draganddrop_neg():
    driver = webdriver.Chrome()
    driver.get("https://jqueryui.com/droppable/")
    driver.switch_to.frame(0)
    drag_ele = driver.find_element(By.XPATH, "//div[@id = 'draggable']")
    drop_ele = driver.find_element(By.XPATH, "//div[@id = 'droppable']")

    actions = ActionChains(driver)
    actions.drag_and_drop_by_offset(drag_ele, 50, 50).perform()
    time.sleep(5)
    assert drop_ele.text == "Drop here", "Drag and Dropped actions performed"

    driver.switch_to.default_content()
    driver.close()
    driver.quit()

