Feature: Adding Items To Cart
    As a test engineer,
    I want to verify the items added in cart are in order,
    verify that i'm able to add same items multiple times as desired

Background: Launch the browser and open the website
    Given Launch the browser
    Then get all products list

@Scenario1
@smoke @sanity @web
Scenario: Verify items listed in cart are in same order as added with price
    Then the user add free-shipping item in cart
    And close the cart
    And the user add free-shipping item in cart
    And close the cart
    And the user add free-shipping item in cart
    And close the cart
    And the user add free-shipping item in cart
    And close the cart
    And the user add non-free-shipping item in cart
    Then verify the items added in cart are in order
    And verify total price
    Then close the cart

@Scenario2
@smoke @sanity @web
Scenario: Verify user is able to add same items as desired
    And the user opens the cart
    Then the user empties the cart
    And the user add "Cropped Stay Groovy off white" item in cart
    Then verify price change as per "Cropped Stay Groovy off white"
    And the user add "Cropped Stay Groovy off white" item in cart
    Then verify price change as per "Cropped Stay Groovy off white"
    And the user add "Cropped Stay Groovy off white" item in cart
    Then verify price change as per "Cropped Stay Groovy off white"
    And verify total price
    And close the cart

    Then the user opens the cart
    And the user empties the cart
    And the user add "Cropped Stay Groovy off white" item in cart
    And verify price change as per "Cropped Stay Groovy off white"
    Then increase the quantity of "Cropped Stay Groovy off white" item in cart
    And verify price change as per "Cropped Stay Groovy off white"
    Then increase the quantity of "Cropped Stay Groovy off white" item in cart
    And verify price change as per "Cropped Stay Groovy off white"
    Then increase the quantity of "Cropped Stay Groovy off white" item in cart
    And verify price change as per "Cropped Stay Groovy off white"
    And the user empties the cart

@Scenario3
@smoke @sanity @web
Scenario: Verify user is able to remove the highest priced item
    And the user opens the cart
    Then the user empties the cart
    And the user add "Skater Black Sweatshirt" item in cart
    And the user add "Skater Black Sweatshirt" item in cart
    And the user add "Skater Black Sweatshirt" item in cart
    And the user add "Cropped Stay Groovy off white" item in cart
    And the user add "Cropped Stay Groovy off white" item in cart
    And the user add "Basic Cactus White T-shirt" item in cart
    And the user verifies the total count shown
    And user remove the highest priced item from cart
    And user remove the highest priced item from cart