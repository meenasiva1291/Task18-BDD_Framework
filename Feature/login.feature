Feature: Login functionality for zenportal

  Scenario: Successful login
    Given I open zenportal login page
    When I enter valid username and password
    When I click on submit button
    Then I should be directed to dashboard page

    #Data from Excel
  Scenario: Verify login functionality with users from Excel
     Given I open zenportal login page
     When I login using credentials from Excel file
     When I click on submit button
     Then I should be directed to dashboard page

    #Data from Json file
  Scenario: Verify login functionality with users from json
    Given I open zenportal login page
    When I login using credentials from json file
    When I click on submit button
    Then I should be directed to dashboard page

  Scenario: Unsuccessful login
    Given I open zenportal login page
    When I enter invalid username and password
    When I click on submit button
    Then I should receive an error message

  Scenario: Validate username and password input box
    Given I open zenportal login page
    When I enter valid username and password
    Then username and password input box is visible and enabled

  Scenario: Validate logout functionality
    Given I open zenportal login page
    When I enter valid username and password
    When I click on submit button
    Then I should be directed to dashboard page
    Then I should be able to click on logout

