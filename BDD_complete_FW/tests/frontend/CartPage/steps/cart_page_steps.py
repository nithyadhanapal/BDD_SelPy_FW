import time

from behave import step
from utilities.common_configs.locatorsConfig import CART_PAGE_LOCATORS
from utilities.common_functions import web_common


@step("I click on 'Free shipping' option")
def I_click_on_Free_shipping_option(context):
    free_ship = CART_PAGE_LOCATORS['free_shipping_radio']
    web_common.click(context, free_ship['type'], free_ship['locator'])

    web_common.assert_radio_is_selected(context, free_ship['type'], free_ship['locator'])


@step("I click on 'Proceed to checkout' button in the cart page")
def I_click_on_Proceed_to_checkout_button_in_the_cart_page(context, ):
    """

    :param context:
    :return:
    """

    proceed_btn = CART_PAGE_LOCATORS['proceed_to_checkout_btn']
    proceed_btn_type = proceed_btn['type']
    proceed_btn_locator = proceed_btn['locator']

    max_try = 3
    try_count = 0
    while try_count < max_try:
        try:
            web_common.click(context, proceed_btn_type, proceed_btn_locator)
            break
        except Exception:
            try_count += 1
            print("Failed to click on Proceed to checkout button. Retry number {}".format(try_count))

    else:
        raise Exception("Failed to click on Proceed to checkout button after retrying {} times".format(max_try))


@step("I get the total amount of the cart")
def I_get_the_total_amount_of_the_cart(context):
    time.sleep(2)
    total_locator = CART_PAGE_LOCATORS['total_cart_value']
    total_raw = web_common.get_element_text(context, total_locator['type'], total_locator['locator'])
    context.cart_total = total_raw.replace('$', '')

@step("I apply the coupon to the cart")
def I_apply_the_coupon_to_the_cart(context):

    coupon_code_locator = CART_PAGE_LOCATORS['coupon_code_value']
    web_common.type_into_element(context, context.coupon_code, coupon_code_locator['type'], coupon_code_locator['locator'])

    apply_coupon_locator = CART_PAGE_LOCATORS['apply_coupon_code']
    web_common.click(context, apply_coupon_locator['type'], apply_coupon_locator['locator'])

@step("The total should be reduced by '{pct}'%")
def The_total_should_be_reduced_by_XX_pct(context, pct):
    original_total = context.cart_total
    expected_new_total = float(original_total) * float(pct) / 100

    context.execute_steps("then I get the total amount of the cart")
    new_total = context.cart_total
    assert float(new_total) == expected_new_total, \
        f"Cart total after applying {pct}% coupon is not expected." \
        f"Original: {original_total}, Expected: {expected_new_total}, Actual: {new_total} "
