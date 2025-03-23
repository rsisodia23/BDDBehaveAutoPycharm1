Feature: Login functionality

  @logincheck
  Scenario: login with valid credential
    Given I am on login page
    When I enter valid email address and password
    And i click on login button
    Then I should get logged in

  @loginwithparam
  Scenario: login with valid credential with params
    Given I am on login page
    When I enter valid email address as "RS202503231215@gmail.com" and password as "123456789"
    And i click on login button
    Then I should get logged in

  @loginwithmultiparam
  Scenario Outline: login with Invalid credential with multiparams
    Given I am on login page
    When I enter valid email address as "<email>" and password as "<password>"
    And i click on login button
    Then I should get logged in
    Examples:
      | email                    | password  |
      | rs123                    | wrongpwd1 |
      | rs1234                   | wrongpwd1 |
      | RS202503231215@gmail.com | 123456789 |

  @loginwithdatatable
  Scenario: login with  credential with multiparams from datatable
    Given I am on login page
    When I enter email address  and password from below datatable
      | email                    | password  |
      | RS202503231215@gmail.com | 123456789 |
      | wrongemail               |wrongpwd   |
    And i click on login button
    Then I should get logged in
