# coding: utf-8

"""
    DHL Express APIs (MyDHL API)

    Welcome to the official DHL Express APIs (MyDHL API) below are the published API Documentation to fulfill your shipping needs with DHL Express.       Please follow the process described [here](https://developer.dhl.com/api-reference/dhl-express-mydhl-api#get-started-section/user-guide--get-access) to request access to the DHL Express - MyDHL API services   In case you already have DHL Express - MyDHL API Service credentials please ensure to use the endpoints/environments listed  [here](https://developer.dhl.com/api-reference/dhl-express-mydhl-api#get-started-section/user-guide--environments) 

    The version of the OpenAPI document: 2.11.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.supermodel_io_logistics_express_create_shipment_request_customer_details_importer_details import SupermodelIoLogisticsExpressCreateShipmentRequestCustomerDetailsImporterDetails

class TestSupermodelIoLogisticsExpressCreateShipmentRequestCustomerDetailsImporterDetails(unittest.TestCase):
    """SupermodelIoLogisticsExpressCreateShipmentRequestCustomerDetailsImporterDetails unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> SupermodelIoLogisticsExpressCreateShipmentRequestCustomerDetailsImporterDetails:
        """Test SupermodelIoLogisticsExpressCreateShipmentRequestCustomerDetailsImporterDetails
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `SupermodelIoLogisticsExpressCreateShipmentRequestCustomerDetailsImporterDetails`
        """
        model = SupermodelIoLogisticsExpressCreateShipmentRequestCustomerDetailsImporterDetails()
        if include_optional:
            return SupermodelIoLogisticsExpressCreateShipmentRequestCustomerDetailsImporterDetails(
                postal_address = openapi_client.models.address_definition_for_/shipments_request.Address definition for /shipments request(
                    postal_code = '14800', 
                    city_name = 'Prague', 
                    country_code = 'CZ', 
                    province_code = 'CZ', 
                    address_line1 = 'V Parku 2308/10', 
                    address_line2 = 'addres2', 
                    address_line3 = 'addres3', 
                    county_name = 'Central Bohemia', 
                    province_name = 'Central Bohemia', 
                    country_name = 'Czech Republic', ),
                contact_information = openapi_client.models.contact_definition.Contact definition(
                    email = 'that@before.de', 
                    phone = '+1123456789', 
                    mobile_phone = '+60112345678', 
                    company_name = 'Company Name', 
                    full_name = 'John Brew', ),
                registration_numbers = [
                    openapi_client.models.registration_numbers_definition.RegistrationNumbers definition(
                        type_code = 'VAT', 
                        number = 'CZ123456789', 
                        issuer_country_code = 'CZ', )
                    ],
                bank_details = [
                    openapi_client.models.supermodel_io_logistics_express_bank_details_inner.supermodelIoLogisticsExpressBankDetails_inner(
                        name = 'Russian Bank Name', 
                        settlement_local_currency = 'RUB', 
                        settlement_foreign_currency = 'USD', )
                    ],
                type_code = 'business'
            )
        else:
            return SupermodelIoLogisticsExpressCreateShipmentRequestCustomerDetailsImporterDetails(
                postal_address = openapi_client.models.address_definition_for_/shipments_request.Address definition for /shipments request(
                    postal_code = '14800', 
                    city_name = 'Prague', 
                    country_code = 'CZ', 
                    province_code = 'CZ', 
                    address_line1 = 'V Parku 2308/10', 
                    address_line2 = 'addres2', 
                    address_line3 = 'addres3', 
                    county_name = 'Central Bohemia', 
                    province_name = 'Central Bohemia', 
                    country_name = 'Czech Republic', ),
                contact_information = openapi_client.models.contact_definition.Contact definition(
                    email = 'that@before.de', 
                    phone = '+1123456789', 
                    mobile_phone = '+60112345678', 
                    company_name = 'Company Name', 
                    full_name = 'John Brew', ),
        )
        """

    def testSupermodelIoLogisticsExpressCreateShipmentRequestCustomerDetailsImporterDetails(self):
        """Test SupermodelIoLogisticsExpressCreateShipmentRequestCustomerDetailsImporterDetails"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
