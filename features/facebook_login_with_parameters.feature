Feature: Facebook login functionality with parameters

  Scenario Outline: Test login with incorrect login credentials with parameters
    When user input wrong "<login_id>" and password "<password>"
      """
         Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do
         eiusmod tempor incididunt ut labore et dolore magna aliqua.
      """
    Then error message will come with parameters

  Examples: Credentials
   |    login_id    |   password   |
   |    zapel       |   zapel      |
   |    fisher      |   toxic      |
