Feature: Calculator API
  Scenario: Add two numbers
    Given I have a calculator API
    When I add 2 and 3
    Then the result should be 5

