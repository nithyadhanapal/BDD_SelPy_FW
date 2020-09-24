
  Feature: Order Placement

    @TCID-33
    Scenario: New user places order with 1 item without creating an account

      Given I go to 'home' page
      When I add '1' random item to the cart from Home page
      And I click on cart in the top nav bar and verify if the cart page opens
#      And I click on 'Free shipping' option
      And I click on 'Proceed to checkout' button in the cart page
      And I verify 'Checkout' page is loaded
      And I fill in the details form
      And I click on 'Place order' button in the checkout page
      Then order confirmation page should load with correct data