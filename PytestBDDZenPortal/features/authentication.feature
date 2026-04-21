Feature: Zen Portal Authentication Functionality
  As a user of the Zen Class portal
  I want to be able to login and logout
  So that I can access my tasks and dashboard securely

  @login
  Scenario: Successful login
    Given user is on zen portal login page
    And user validates user name and password
    And user validates submit button
    When user keys in username "suja2105@gmail.com" and password "Sujatha@7777"
    And clicks on the login button
    Then user should be navigated to zen dashboard

  @login_unsuccessful
  Scenario Outline: Unsuccessful login with invalid credentials
    Given user is on zen portal login page
    When user keys username "<username>" and invalid password "<password>"
    And clicks on the login button
    Then user should be not be navigated to zen dashboard

    Examples:

      | username          | password    |
      | ven2105@gmail.com | invalidpass |
      | suja2105@gmail.in | wrongpassword |

  @logout
  Scenario: Successful logout from dashboard
    Given user is on zen portal login page
    When user keys in username "suja2105@gmail.com" and password "Sujatha@7777"
    And clicks on the login button
    Then user should be navigated to zen dashboard
    And user logsout of zen dashboard
    And user should be redirected to login page