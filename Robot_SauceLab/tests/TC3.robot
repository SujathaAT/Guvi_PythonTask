*** Settings ***
Resource    ../utilities/common.robot
Resource    ../steps/LoginSteps.robot
Resource    ../steps/AddProductSteps.robot
Library    ../libraries/Selenium_Wrapper.py

Test Setup    Open Application
Test Teardown    Close Application

*** Test Cases ***

Add Product to Cart

    Login With Valid Credentials
    Add Product and Verify Cart
    take_screenshot    Add Product