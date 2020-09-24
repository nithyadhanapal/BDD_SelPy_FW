LOCATORS = {
    'main navigation' : {'type': 'id', 'locator':'mainnav'},
    'top navigation' : {'type': 'id', 'locator':'top'},
    'options' : {'type': 'css selector', 'locator':'.options-bar'}
}

MY_ACCOUNT_LOCATORS = {
    'login_user_name' : {'type': 'id', 'locator':'username'},
    'login_password' : {'type': 'id', 'locator':'password'},
    'login_btn' : {'type': 'css selector', 'locator':'button[name="login"]'},
    'left_nav' : {'type': 'class name', 'locator': 'woocommerce-MyAccount-navigation'},
    'left_nav_logout_btn' : {'type': 'css selector', 'locator': 'div.entry-content nav.woocommerce-MyAccount-navigation ul li:nth-of-type(6)'},
    'error_box' : {'type': 'css selector', 'locator': 'ul.woocommerce-error'}

}

HOME_PAGE_LOCATORS = {
    'all_add_cart_btn' : {'type': 'css selector', 'locator': 'li.product a.ajax_add_to_cart'},
    'cart_info_box' : {'type': 'css selector', 'locator': 'ul.site-header-cart'}
}

CART_PAGE_LOCATORS = {
    'free_shipping_radio': {'type': 'css selector', 'locator': 'li input#shipping_method_0_free_shipping3'},
    'proceed_to_checkout_btn': {'type': 'css selector', 'locator': 'div.wc-proceed-to-checkout a.checkout-button'},
    'total_cart_value': {'type': 'css selector', 'locator': 'tr.order-total span.woocommerce-Price-amount.amount'},
    'coupon_code_value': {'type': 'css selector', 'locator': "input[id='coupon_code']"},
    'apply_coupon_code': {'type': 'css selector', 'locator': "button[name='apply_coupon']"},

}

CHECKOUT_PAGE_LOCATORS = {
    'checkout_page_header': {'type': 'xpath', 'locator': "//h1[@class='entry-title']"},
    'checkout_form': {'type': 'css selector', 'locator': "form[name='checkout']"},
    'first_name': {'type': 'css selector', 'locator': "input[name='billing_first_name']"},
    'last_name': {'type': 'css selector', 'locator': "input[name='billing_last_name']"},
    'company_name': {'type': 'css selector', 'locator': "input[name='billing_company']"},
    'address_1': {'type': 'css selector', 'locator': "input[name='billing_address_1']"},
    'address_2': {'type': 'css selector', 'locator': "input[name='billing_address_2']"},
    'billing_city': {'type': 'css selector', 'locator': "input[name='billing_city']"},
    # 'billing_state': {'type': 'css selector', 'locator': ""},
    'billing_zipcode': {'type': 'css selector', 'locator': "input[name='billing_postcode']"},
    'phone_number': {'type': 'css selector', 'locator': "input[name='billing_phone']"},
    'email_id': {'type': 'css selector', 'locator': "input[name='billing_email']"},

    'place_order_btn': {'type': 'css selector', 'locator': "button[id='place_order']"}
}

ORDER_RECEIVED_LOCATORS = {
    'page_header': {'type': 'xpath', 'locator': "//h1[@class='entry-title']"},
    # 'thankyou_notice': {'type': 'css selector', 'locator': "div.woocommerce-order p.woocommerce-thankyou-order-received"},
    'thankyou_notice': {'type': 'css selector', 'locator': "p[class*='woocommerce-thankyou-order-received']"},
    'order_details_order': {'type': 'css selector', 'locator': "ul.order_details li.order"},
    'order_details_date': {'type': 'css selector', 'locator': "ul.order_details li.date"},
    'order_details_total': {'type': 'css selector', 'locator': "ul.order_details li.total"},
    'order_details_method': {'type': 'css selector', 'locator': "ul.order_details li.mothod"},


}