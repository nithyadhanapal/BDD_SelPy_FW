from behave import step
from utilities.common_configs.locatorsConfig import CHECKOUT_PAGE_LOCATORS
from utilities.common_functions import web_common
from utilities.common_helpers.utilitiesHelper import generate_random_first_and_last_names


@step("I verify 'Checkout' page is loaded")
def I_verify_checkout_page_is_loaded(context):

    # To check if the URL contains 'Checkout' text
    web_common.assert_url_contains(context, '/checkout/')

    # To check if the header is Checkout
    expected_text = 'Checkout'
    check_out_locator = CHECKOUT_PAGE_LOCATORS['checkout_page_header']
    header_type = check_out_locator['type']
    header_locator = check_out_locator['locator']
    contains = web_common.element_contains_text(context, expected_text, header_type, header_locator)
    assert contains, f"Header of checkout page deosnt not contain the text '{expected_text}'."

    # To check checkout form is loaded

    checkout_form_field = CHECKOUT_PAGE_LOCATORS['checkout_form']
    web_common.assert_element_visible(context, checkout_form_field['type'], checkout_form_field['locator'])

@step("I fill in the details form")
def I_fill_in_the_details_form(context):

    rand_name = generate_random_first_and_last_names()
    f_name = rand_name['f_name']
    l_name = rand_name['l_name']
    comp_name = 'CG'
    address_1 = 'Unit 201'
    address_2 = 'Main street'
    city_name = 'Boston'
    zip_code = '02123'
    phone_num = '123455666'
    email_id = 'testform@gmail.com'

    f_name_locator = CHECKOUT_PAGE_LOCATORS['first_name']
    l_name_locator = CHECKOUT_PAGE_LOCATORS['last_name']
    comp_name_locator = CHECKOUT_PAGE_LOCATORS['company_name']
    address1_locator = CHECKOUT_PAGE_LOCATORS['address_1']
    address2_locator = CHECKOUT_PAGE_LOCATORS['address_2']
    city_locator = CHECKOUT_PAGE_LOCATORS['billing_city']
    zipcode_locator = CHECKOUT_PAGE_LOCATORS['billing_zipcode']
    phone_locator = CHECKOUT_PAGE_LOCATORS['phone_number']
    email_locator = CHECKOUT_PAGE_LOCATORS['email_id']

    # Start input values
    web_common.type_into_element(context, f_name, f_name_locator['type'], f_name_locator['locator'])
    web_common.type_into_element(context, l_name, l_name_locator['type'], l_name_locator['locator'])
    web_common.type_into_element(context, comp_name, comp_name_locator['type'], comp_name_locator['locator'])
    web_common.type_into_element(context, address_1, address1_locator['type'], address1_locator['locator'])
    web_common.type_into_element(context, address_2, address2_locator['type'], address2_locator['locator'])
    web_common.type_into_element(context, city_name, city_locator['type'], city_locator['locator'])
    web_common.type_into_element(context, zip_code, zipcode_locator['type'], zipcode_locator['locator'])
    web_common.type_into_element(context, phone_num, phone_locator['type'], phone_locator['locator'])
    web_common.type_into_element(context, email_id, email_locator['type'], email_locator['locator'])

@step("I click on 'Place order' button in the checkout page")
def I_click_on_Place_order_button_in_the_checkout_page(context):

    btn_locator = CHECKOUT_PAGE_LOCATORS['place_order_btn']
    web_common.click(context, btn_locator['type'], btn_locator['locator'])
