Feature: Register functionality

  @registercheck
  Scenario: register with all details
    Given I am on Register page
    When I enter all mandatory details
    And i click on continue button
    Then I should get registerd successfully