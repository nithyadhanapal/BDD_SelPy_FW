
  @regression @coupon @cart @coupon_fe
  Feature: Add valid coupons to the cart

    @TCID-44
    Scenario: Adding 50% off, cart should discount the whole cart by 50%
      Given I go to 'home' page
      When I add '3' random item to the cart from Home page
      And I click on cart in the top nav bar and verify if the cart page opens
      And I get the total amount of the cart
      And I get a valid '50'% off coupon
      Then I apply the coupon to the cart
      Then The total should be reduced by '50'%