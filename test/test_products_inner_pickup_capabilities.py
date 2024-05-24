# coding: utf-8

"""
    DHL Express APIs (MyDHL API)

    Welcome to the official DHL Express APIs (MyDHL API) below are the published API Documentation to fulfill your shipping needs with DHL Express.       Please follow the process described [here](https://developer.dhl.com/api-reference/dhl-express-mydhl-api#get-started-section/user-guide--get-access) to request access to the DHL Express - MyDHL API services   In case you already have DHL Express - MyDHL API Service credentials please ensure to use the endpoints/environments listed  [here](https://developer.dhl.com/api-reference/dhl-express-mydhl-api#get-started-section/user-guide--environments) 

    The version of the OpenAPI document: 2.11.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.products_inner_pickup_capabilities import ProductsInnerPickupCapabilities

class TestProductsInnerPickupCapabilities(unittest.TestCase):
    """ProductsInnerPickupCapabilities unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ProductsInnerPickupCapabilities:
        """Test ProductsInnerPickupCapabilities
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ProductsInnerPickupCapabilities`
        """
        model = ProductsInnerPickupCapabilities()
        if include_optional:
            return ProductsInnerPickupCapabilities(
                next_business_day = False,
                local_cutoff_date_and_time = '2019-09-18T15:00:00',
                gmt_cutoff_time = '16:00:00',
                pickup_earliest = '09:30:00',
                pickup_latest = '16:00:00',
                origin_service_area_code = 'ELA',
                origin_facility_area_code = 'ELA',
                pickup_additional_days = 0,
                pickup_day_of_week = 3
            )
        else:
            return ProductsInnerPickupCapabilities(
        )
        """

    def testProductsInnerPickupCapabilities(self):
        """Test ProductsInnerPickupCapabilities"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()