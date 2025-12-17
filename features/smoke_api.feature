Feature: Smoke E2E for Kanban API

  Scenario: Create user (registration smoke)
    Given API server is running
    When I create a user with email "smoke_user@example.com"
    Then response status should be 200
    And response should contain field "id"

  Scenario: Create task for existing user (tasks smoke)
    Given API server is running
    Given I have a user with email "task_owner@example.com"
    When I create a task with title "Smoke task" for that user
    Then response status should be 200
    And response json should match:
      | title   | Smoke task |
    And response should contain field "id"

  Scenario: List tasks contains created task (read smoke)
    Given API server is running
    Given I have a user with email "list_owner@example.com"
    Given I have a task with title "Listed smoke task" for that user
    When I request tasks list
    Then response status should be 200
    And tasks list should contain a task with title "Listed smoke task"
