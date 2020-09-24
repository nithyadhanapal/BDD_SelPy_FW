from woocommerce import API
from utilities.common_helpers.credentialsHelper import CredentialsHelper

class wooRequestHelpers(object):

    def __init__(self):

        creds_helper = CredentialsHelper()
        wc_creds = creds_helper.get_wc_api_keys()

        self.wcapi = API(
            url="http://nprstore.local",
            consumer_key = wc_creds['wc_key'],
            consumer_secret = wc_creds['wc_secret'],
            version="wc/v3"
        )

    def assert_status_code(self):
        assert self.rs.status_code == self.expected_status_code, "Bad status code. Endpoint: {}, params: {}, " \
                                                                 "Actual status code: {}, Expected status code: {}, " \
                                                                 "Response body: {}" \
                                                                 "".format(self.wc_endpoint, self.params,
                                                                           self.rs.status_code,
                                                                           self.expected_status_code,
                                                                           self.rs.json())

    def get(self, wc_endpoint, params=None, expected_status_code=200):
        """

        :param wc_endpoint:
        :param params:
        :param expected_status_code:
        :return:
        """
        self.rs = self.wcapi.get(wc_endpoint, params=params)
        self.wc_endpoint = wc_endpoint
        self.expected_status_code = expected_status_code
        self.params = params
        self.assert_status_code()

        return self.rs.json()

    def post(self, wc_endpoint, params=None, expected_status_code=200):
        """

        :param wc_endpoint:
        :param params:
        :param expected_status_code:
        :return:
        """
        self.rs = self.wcapi.post(wc_endpoint, data=params)
        self.wc_endpoint = wc_endpoint
        self.expected_status_code = expected_status_code
        self.params = params
        self.assert_status_code()

        return self.rs.json()

    def put(self):
        pass

    def delete(self):
        pass


if __name__ == '__main__':
    myObj = wooRequestHelpers()
    # myObj.get("products")

    payload = {
                "email": "dummyemail1@supersqa.com",
                "password": "123abc"
              }
    response = myObj.post("customers", params=payload, expected_status_code= 201)

    import pprint; pprint.pprint(response)
