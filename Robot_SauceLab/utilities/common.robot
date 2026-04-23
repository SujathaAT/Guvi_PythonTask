*** Settings ***
Library    ../libraries/Selenium_Wrapper.py
Library    SeleniumLibrary

*** Variables ***
${url}    https://www.saucedemo.com/

*** Keywords ***

Open Application
    Start Browser    Chrome    ${url}

Close Application
    Selenium_Wrapper.Close Browser