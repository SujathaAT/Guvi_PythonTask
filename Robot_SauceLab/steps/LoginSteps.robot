*** Settings ***
Resource    ../pages/login_page.robot
Library    ../libraries/Selenium_Wrapper.py


*** Keywords ***
Login With Valid Credentials
    Enter User Credentials
    Click On Login Button
