*** Settings ***
Library    SeleniumLibrary
Library    ../utilities/hooks.py
Test Setup    Start Browser
Test Teardown    Stop Browser

*** Test Cases ***
Validate login Function
#    Open Browser    https://robotsparebinindustries.com/    chrome
#    Maximize Browser Window
    Title Should Be    RobotSpareBin Industries Inc. - Intranet
    Wait Until Element Is Visible    id=username    15s
    Input Text    id=username    maria
    Input Text    name=password    thoushallnotpass
    Click Element    xpath://button[text()='Log in']
    Wait Until Element Is Visible    id=logout    15s
    Page Should Contain Element    id=logout
    Click Button    id=logout
    Sleep    10s
    Close Browser