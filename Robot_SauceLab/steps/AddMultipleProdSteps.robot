
*** Settings ***
Resource    ../pages/login_page.robot
Resource    ../pages/inventory_page.robot
Library    ../libraries/Selenium_Wrapper.py


*** Keywords ***
Add Multiple Products And Verify Checkout
    Add Multiple Products
    Fill Checkout Info
    Verify Items
    Check Quantity
