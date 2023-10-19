Feature: Filter Validation
    As a test engineer,
    I want to filter products based on sizes and verify the filtered result

Background: Launch the browser and open the website
    Given Launch the browser

@Scenario4
@smoke @sanity @web
Scenario: Search a single size and filter the items
    Then the user apply/remove "XS" filter
    Then items with "XS" size gets filtered
    And the user apply/remove "XS" filter

    Then the user apply/remove "S" filter
    And items with "S" size gets filtered
    Then the user apply/remove "S" filter

    And the user apply/remove "M" filter
    Then items with "M" size gets filtered
    And the user apply/remove "M" filter

    Then the user apply/remove "ML" filter
    And items with "ML" size gets filtered
    Then the user apply/remove "ML" filter

    And the user apply/remove "L" filter
    Then items with "L" size gets filtered
    And the user apply/remove "L" filter

    Then the user apply/remove "XL" filter
    And items with "XL" size gets filtered
    Then the user apply/remove "XL" filter

    And the user apply/remove "XXL" filter
    Then items with "XXL" size gets filtered
    And the user apply/remove "XXL" filter

@Scenario5
@smoke @sanity @web
Scenario: Search multiple size at once (or) one by one and filter the items
    Then the user apply/remove "S" filter
    And the user apply/remove "M" filter
    Then items with double "S" "M" sizes gets filtered
    And the user apply/remove "S" filter
    Then the user apply/remove "M" filter

    And the user apply/remove at once "S" "M" filters
    Then items with double "S" "M" sizes gets filtered
    And the user apply/remove at once "S" "M" filters