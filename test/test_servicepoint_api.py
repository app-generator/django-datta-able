# coding: utf-8

"""
    DHL Express APIs (MyDHL API)

    Welcome to the official DHL Express APIs (MyDHL API) below are the published API Documentation to fulfill your shipping needs with DHL Express.       Please follow the process described [here](https://developer.dhl.com/api-reference/dhl-express-mydhl-api#get-started-section/user-guide--get-access) to request access to the DHL Express - MyDHL API services   In case you already have DHL Express - MyDHL API Service credentials please ensure to use the endpoints/environments listed  [here](https://developer.dhl.com/api-reference/dhl-express-mydhl-api#get-started-section/user-guide--environments) 

    The version of the OpenAPI document: 2.11.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.api.servicepoint_api import ServicepointApi


class TestServicepointApi(unittest.TestCase):
    """ServicepointApi unit test stubs"""

    def setUp(self) -> None:
        self.api = ServicepointApi()

    def tearDown(self) -> None:
        pass

    def test_exp_api_servicepoints(self) -> None:
        """Test case for exp_api_servicepoints

        Returns list of service points based on the given postal location address, service point ID or geocode details for DHL Express Service points to pick-up and drop-off shipments
        """
        pass


if __name__ == '__main__':
    unittest.main()
