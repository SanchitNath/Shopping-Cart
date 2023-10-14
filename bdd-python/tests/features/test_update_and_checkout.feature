Feature: Update and Checkout to complete order
    As a test engineer,
    I want to update the added items in cart,
    checkout the cart to complete the order

Background: Launch the browser and open the website
    Given Launch the browser
    Then get all products list

@Scenario5
@smoke @sanity @web
Scenario: Verify user can delete items in cart
    Then the user opens the cart
    And the user empties the cart
    Then the user add free-shipping item in cart
    And close the cart
    And the user add free-shipping item in cart
    And close the cart
    And the user add non-free-shipping item in cart
    Then verify the items added in cart are in order
    And verify total price
    And the user empties the cart
    Then the user verifies price reduced to zero
    And the user verifies count reduced to zero

@Scenario6
@smoke @sanity @web
Scenario: Verify user is able to place order
    Then the user opens the cart
    And the user empties the cart
    Then the user add free-shipping item in cart
    And close the cart
    Then the user add free-shipping item in cart
    And close the cart
    Then the user add non-free-shipping item in cart
    And verify total price
    Then the user places the order
    And verify the price shown in alert
    Then refresh the page
    And the user opens the cart
    Then the user verifies price reduced to zero
    And the user verifies count reduced to zero

