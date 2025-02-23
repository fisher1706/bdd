Feature: Facebook login functionality

  @logincase
  Scenario: Test login with incorrect login credentials
    When input wrong credentials
    Then error message will come
