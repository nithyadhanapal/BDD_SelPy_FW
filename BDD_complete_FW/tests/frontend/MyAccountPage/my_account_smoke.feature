  @my_acc_smoke @smoke
  Feature: My account smoke test

    @TCID-10
    Scenario: Valid user should be able to login

      Given I go to 'my account' page
      When I type 'first.test.user@supersqa.com' into the username of login form
      And I type the 'testuserpassw' into the password of login form
      And I click on 'login' button
      Then user should be logged in

    @TCID-11
    Scenario: User with wrong password should get correct error message

      Given I go to 'my account' page
      When I type 'first.test.user@supersqa.com' into the username of login form
      And I type the '123456' into the password of login form
      And I click on 'login' button
      Then error message with email 'first.test.user@supersqa.com' should be displayed

    @TCID-12
    Scenario: User with non existing email should get correct error message

      Given I go to 'my account' page
      When I type 'nonexisting123@supersqa.com' into the username of login form
      And I type the '123456' into the password of login form
      And I click on 'login' button
      Then error message for 'unknown email' should be displayed