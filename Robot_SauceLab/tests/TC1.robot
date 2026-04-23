*** Settings ***
Resource    ../utilities/common.robot
Resource    ../steps/LoginSteps.robot
Library    ../libraries/Selenium_Wrapper.py

Test Setup    Open Application
Test Teardown    Close Application

*** Test Cases ***

Validate User Login

    Login With Valid Credentials
    verify_url    https://www.saucedemo.com/inventory.html
    take_screenshot    Login