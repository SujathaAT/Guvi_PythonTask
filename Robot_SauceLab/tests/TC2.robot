*** Settings ***
Resource    ../utilities/common.robot
Resource    ../steps/LoginSteps.robot

Test Setup    Open Application
Test Teardown    Close Application

*** Test Cases ***

Validate User Login

    Set Global Variable    ${flag}    NEGATIVE
    Login With Valid Credentials
    find_element    xpath    //button[@class = 'error-button']
    take_screenshot    Invalid_Login