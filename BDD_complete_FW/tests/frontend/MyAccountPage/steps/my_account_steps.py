from behave import step
from utilities.common_functions import web_common
from utilities.common_configs.locatorsConfig import MY_ACCOUNT_LOCATORS
import pdb
@step("I type '{email}' into the username of login form")
def type_email_into_username_of_login_form(context, email):
    """

    :param context:
    :param email:
    :return:
    """

    email_locator_type = MY_ACCOUNT_LOCATORS['login_user_name']['type']
    email_locator_string = MY_ACCOUNT_LOCATORS['login_user_name']['locator']
    web_common.type_into_element(context, email, email_locator_type, email_locator_string)

@step("I type the '{password}' into the password of login form")
def type_password_into_password_of_login_form(context, password):
    """

    :param context:
    :param password:
    :return:
    """
    password_locator_type = MY_ACCOUNT_LOCATORS['login_password']['type']
    password_locator_string = MY_ACCOUNT_LOCATORS['login_password']['locator']
    web_common.type_into_element(context, password, password_locator_type, password_locator_string)


@step("I click on '{btn_name}' button")
def i_click_on_login_button(context, btn_name):
    """

    :param context:
    :param btn_name:
    :return:
    """
    if btn_name.lower() in ('login', 'log in'):
        login_btn_locator_type = MY_ACCOUNT_LOCATORS['login_btn']['type']
        login_btn_locator_string = MY_ACCOUNT_LOCATORS['login_btn']['locator']
    else:
        raise Exception("Not implemented")

    web_common.click(context, login_btn_locator_type, login_btn_locator_string)

@step('user should be logged in')
def user_should_be_logged_in(context):
    """

    :param context:
    :return:
    """
    nav_bar_type = MY_ACCOUNT_LOCATORS['left_nav']['type']
    nav_bar_text = MY_ACCOUNT_LOCATORS['left_nav']['locator']

    logout_btn_type = MY_ACCOUNT_LOCATORS['left_nav_logout_btn']['type']
    logout_btn_text = MY_ACCOUNT_LOCATORS['left_nav_logout_btn']['locator']

    web_common.assert_element_visible(context, nav_bar_type, nav_bar_text)
    web_common.assert_element_visible(context, logout_btn_type, logout_btn_text)

@step("error message with email '{email}' should be displayed")
def error_message_with_email_should_be_displayed(context, email):
    """

    :param context:
    :param email:
    :return:
    """

    expected_message = "ERROR: The password you entered for the email address {} is incorrect. Lost your password?".format(email)

    error_box_type = MY_ACCOUNT_LOCATORS['error_box']['type']
    error_text= MY_ACCOUNT_LOCATORS['error_box']['locator']
    is_displayed = web_common.element_contains_text(context, expected_message, error_box_type, error_text)

    if is_displayed:
        print("Pass")
    else:
        raise Exception("Correct error message is not displayed at failed login: {}".format(email))

@step("error message for 'unknown email' should be displayed")
def error_message_with_non_existing_email_should_be_displayed(context):
    """

    :param context:
    :param email:
    :return:
    """

    expected_message = "ERROR: Invalid email address. Lost your password?"

    error_box_type = MY_ACCOUNT_LOCATORS['error_box']['type']
    error_text= MY_ACCOUNT_LOCATORS['error_box']['locator']
    is_displayed = web_common.element_contains_text(context, expected_message, error_box_type, error_text)
    if is_displayed:
        print("Pass")
    else:
        raise Exception("Correct error message is not displayed at failed login. Non-existing email.")
