*** Settings ***
Resource    ../utilities/common.robot
Resource    ../steps/LoginSteps.robot
Resource    ../steps/AddMultipleProdSteps.robot
Library     SeleniumLibrary
Library    ../libraries/Selenium_Wrapper.py

Test Setup    Open Application
Test Teardown    Close Application

*** Variables ***
@{productnames}    Sauce Labs Backpack    Sauce Labs Bike Light


*** Test Cases ***


Add Multiple Products And Validate Checkout Summary

    Set Global Variable    ${flag}    POSITIVE
    Login With Valid Credentials
    Add Multiple Products
    Fill Checkout Info
    Verify Items
    Check Quantity

    verify_url    https://www.saucedemo.com/inventory.html
    take_screenshot    Add Multiple Products and Checkout