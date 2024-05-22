# coding: utf-8

"""
    DHL Express APIs (MyDHL API)

    Welcome to the official DHL Express APIs (MyDHL API) below are the published API Documentation to fulfill your shipping needs with DHL Express.       Please follow the process described [here](https://developer.dhl.com/api-reference/dhl-express-mydhl-api#get-started-section/user-guide--get-access) to request access to the DHL Express - MyDHL API services   In case you already have DHL Express - MyDHL API Service credentials please ensure to use the endpoints/environments listed  [here](https://developer.dhl.com/api-reference/dhl-express-mydhl-api#get-started-section/user-guide--environments) 

    The version of the OpenAPI document: 2.11.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.partner import Partner

class TestPartner(unittest.TestCase):
    """Partner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Partner:
        """Test Partner
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Partner`
        """
        model = Partner()
        if include_optional:
            return Partner(
                partner_id = '',
                partner_name = '',
                partner_type_code = '',
                promotion = openapi_client.models.promotion.Promotion(
                    id = 56, 
                    country_code = '', 
                    partner_type_code = '', 
                    service_point_id = '', 
                    client_id = '', 
                    capability = '', 
                    start_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    end_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    day_of_week = '', 
                    text = '', 
                    button_text = '', 
                    language_code1 = '', 
                    text1 = '', 
                    button_text1 = '', 
                    language_code2 = '', 
                    text2 = '', 
                    button_text2 = '', 
                    language_code3 = '', 
                    text3 = '', 
                    button_text3 = '', 
                    hyperlink = '', 
                    created = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), )
            )
        else:
            return Partner(
        )
        """

    def testPartner(self):
        """Test Partner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
