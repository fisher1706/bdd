Feature: Facebook login functionality

  @logincase
  @sanity
  Scenario: Test login with correct login credentials
     Given credentials are given
      When we input correct credentials
      Then login will be successful
       And correct profile open

  @smoke
  Scenario: Test login with incorrect login credentials
      When user input wrong credentials
      Then error message demo will come
       And correct profile open
