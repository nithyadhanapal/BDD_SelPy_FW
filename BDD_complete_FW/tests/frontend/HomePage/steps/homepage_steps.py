from behave import step
from utilities.common_configs.locatorsConfig import HOME_PAGE_LOCATORS
from utilities.common_functions import web_common
import random
import time
import logging as logger

@step("I add '{qty}' random item to the cart from Home page")
def I_add_random_item_to_the_cart_from_Home_page(context, qty):

    logger.info("111")
    logger.info("111")
    logger.info(f"Adding {qty} items to the cart.")
    cart_btns = HOME_PAGE_LOCATORS['all_add_cart_btn']
    cart_btns_type = cart_btns['type']
    cart_btns_locator = cart_btns['locator']

    cart_btns = web_common.find_elements(context, cart_btns_type, cart_btns_locator)
    random_btns = random.sample(cart_btns, int(qty))

    for item in random_btns:
        web_common.click(item)
    time.sleep(1)


@step("I click on cart in the top nav bar and verify if the cart page opens")
def I_click_on_cart_in_the_top_nav_bar_and_verify_cart_page_opens(context):

    cart_info = HOME_PAGE_LOCATORS['cart_info_box']
    cart_info_type = cart_info['type']
    cart_info_locator = cart_info['locator']

    web_common.click(context, cart_info_type , cart_info_locator)
    web_common.assert_url_contains(context, '/cart/')


