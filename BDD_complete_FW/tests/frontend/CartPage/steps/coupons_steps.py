from behave import step
from utilities.common_configs.locatorsConfig import CART_PAGE_LOCATORS
from utilities.common_functions import web_common

@step("I get a valid '{pct}'% off coupon")
def I_get_a_valid_XX_pct_coupon(context, pct):

    if int(pct) == 50:
        context.coupon_code = "test50"
    else:
        raise Exception("Invalid coupon")






