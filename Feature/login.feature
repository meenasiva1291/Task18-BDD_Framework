Feature: Login functionality for ZenPortal

  Scenario: Successful login
    Given I open zenportal login page
    When I login using valid credentials
    And I click on submit button
    Then I should be directed to dashboard page

  Scenario: Unsuccessful login
    Given I open zenportal login page
    When I login using valid username and invalid password
    And I click on submit button
    Then I should receive an error message

  Scenario: Validate username and password input box
    Given I open zenportal login page
    Then username and password input boxes should be visible and enabled

  Scenario: Validate logout functionality
    Given I open zenportal login page
    When I login using valid credentials
    And I click on submit button
    Then I should be directed to dashboard page
    When I click on logout button
    Then I should be redirected to login page
