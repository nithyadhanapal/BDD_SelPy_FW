import time
from behave import *
from utilities.common_configs.locatorsConfig import ORDER_RECEIVED_LOCATORS
from utilities.common_functions import web_common

@then("order confirmation page should load with correct data")
def order_confirmation_page_should_load_with_correct_data(context):

    context.execute_steps("""
        then Order received heading should be displayed
        then Thank you message should be displayed
    """)

@then("Order received heading should be displayed")
def Order_received_heading_should_be_displayed(context):
    header_locator = ORDER_RECEIVED_LOCATORS['page_header']
    web_common.assert_element_contains_text(context, 'Order Received', header_locator['type'], header_locator['locator'])


@then("Thank you message should be displayed")
def Thank_you_message_should_be_displayed(context):
    thankyou_locator = ORDER_RECEIVED_LOCATORS['thankyou_notice']
    web_common.assert_element_contains_text(context, 'Thank you. Your order has been received.', thankyou_locator['type'],
                                     thankyou_locator['locator'])