Feature: Search functionality

  @search
  Scenario: Search a  valid product
    Given I am on search page
    When I enter valid product on search bar
    And i click on search button
    Then Product details should displayed

  @search
  Scenario: Search an invalid product
    Given I am on search page
    When I enter invalid product on search bar
    And i click on search button
    Then i should get a proper warning message of no valid product
