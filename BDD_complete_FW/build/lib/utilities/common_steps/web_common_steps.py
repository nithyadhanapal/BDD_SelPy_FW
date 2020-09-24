
from behave import given, when, then, step
from utilities.common_configs import urlconfig
from utilities.common_functions import web_common
import pdb
# start of step definitions

@step("I go to 'my account' page")
@given('I go to the site "{site}"')
def go_to_url(context, site):
    """
    Step definition to go to the specified url.
    :param context:
    :param url:
    """
    url = urlconfig.URLCONFIG.get(site)
    print("Navigating to the site: {}".format(url))


    context.driver = web_common.go_to(url)

#========================================================================================#

@then('the page title should be "{expected_title}"')
def verify_homepage_title(context, expected_title):
    """
    Verifies the home page title is as expected.
    :param context:
    :param expected_title:
    :return:
    """

    web_common.assert_page_title(context, expected_title)

#========================================================================================#
@then('current url should be "{expected_url}"')
def verify_current_url(context, expected_url):
    """
    Verifies the current uls is as expected_url
    :param context:
    :param expected_url:
    """

    web_common.assert_current_url(context, expected_url)