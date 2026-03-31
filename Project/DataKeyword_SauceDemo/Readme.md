SauceDemo Automation Framework

A Hybrid Framework built with Python, Selenium, and Pytest utilizing POM, Data-Driven, and Keyword-Driven architectures.

Architecture
The project follows a multi-layered design for maximum reusability:
Page Object Model (POM): Decouples UI locators from test logic in pages/.
Keyword-Driven: Common workflows (Login, Checkout) are abstracted in workflow/keywords.py.
Data-Driven: All test inputs (Users, Sorting criteria) managed via testdata/common_data.yaml.
BasePage Wrapper: Centralized Selenium interactions with explicit waits for stability.

Features
* Cross-Browser Testing: Supports Chrome and Firefox.
* Data Centralization: Easy management of credentials and test data via YAML.
* Resilient Reporting: Automatic screenshot capture on failure via Pytest hooks.
* Interactive Analytics: Integration with Allure Reports for execution history.

Usage
1. Execution
Run the entire suite or specific tests using the following commands:

(a) Run all tests 
    pytest tests/test_saucedemo.py

(b) Run on Firefox
    pytest tests/test_saucedemo.py --browser firefox

2. Allure Reporting
    pytest tests/test_saucedemo.py --alluredir=allure-results