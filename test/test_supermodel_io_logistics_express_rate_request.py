# coding: utf-8

"""
    DHL Express APIs (MyDHL API)

    Welcome to the official DHL Express APIs (MyDHL API) below are the published API Documentation to fulfill your shipping needs with DHL Express.       Please follow the process described [here](https://developer.dhl.com/api-reference/dhl-express-mydhl-api#get-started-section/user-guide--get-access) to request access to the DHL Express - MyDHL API services   In case you already have DHL Express - MyDHL API Service credentials please ensure to use the endpoints/environments listed  [here](https://developer.dhl.com/api-reference/dhl-express-mydhl-api#get-started-section/user-guide--environments) 

    The version of the OpenAPI document: 2.11.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.supermodel_io_logistics_express_rate_request import SupermodelIoLogisticsExpressRateRequest

class TestSupermodelIoLogisticsExpressRateRequest(unittest.TestCase):
    """SupermodelIoLogisticsExpressRateRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> SupermodelIoLogisticsExpressRateRequest:
        """Test SupermodelIoLogisticsExpressRateRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `SupermodelIoLogisticsExpressRateRequest`
        """
        model = SupermodelIoLogisticsExpressRateRequest()
        if include_optional:
            return SupermodelIoLogisticsExpressRateRequest(
                customer_details = openapi_client.models.supermodel_io_logistics_express_rate_request_customer_details.supermodelIoLogisticsExpressRateRequest_customerDetails(
                    shipper_details = openapi_client.models.address_definition_for_/rates,_/products,_/landed_cost.Address definition for /rates, /products, /landed-cost(
                        postal_code = '14800', 
                        city_name = 'Prague', 
                        country_code = 'CZ', 
                        province_code = 'CZ', 
                        address_line1 = 'addres1', 
                        address_line2 = 'addres2', 
                        address_line3 = 'addres3', 
                        county_name = 'Central Bohemia', ), 
                    receiver_details = openapi_client.models.address_definition_for_/rates,_/products,_/landed_cost.Address definition for /rates, /products, /landed-cost(
                        postal_code = '14800', 
                        city_name = 'Prague', 
                        country_code = 'CZ', 
                        province_code = 'CZ', 
                        address_line1 = 'addres1', 
                        address_line2 = 'addres2', 
                        address_line3 = 'addres3', 
                        county_name = 'Central Bohemia', ), ),
                accounts = [
                    openapi_client.models.account_definition.Account definition(
                        type_code = 'shipper', 
                        number = '123456789', )
                    ],
                product_code = 'P',
                local_product_code = 'P',
                value_added_services = [
                    openapi_client.models.value_added_services_definition_for_/rates,_/products,_/landed_cost.Value Added Services definition for /rates, /products, /landed-cost(
                        service_code = 'II', 
                        local_service_code = 'II', 
                        value = 100, 
                        currency = 'GBP', 
                        method = 'cash', )
                    ],
                products_and_services = [
                    openapi_client.models.supermodel_io_logistics_express_rate_request_products_and_services_inner.supermodelIoLogisticsExpressRateRequest_productsAndServices_inner(
                        product_code = 'P', 
                        local_product_code = 'P', 
                        value_added_services = [
                            openapi_client.models.value_added_services_definition_for_/rates,_/products,_/landed_cost.Value Added Services definition for /rates, /products, /landed-cost(
                                service_code = 'II', 
                                local_service_code = 'II', 
                                value = 100, 
                                currency = 'GBP', 
                                method = 'cash', )
                            ], )
                    ],
                payer_country_code = 'CZ',
                planned_shipping_date_and_time = '2020-03-24T13:00:00GMT+00:00',
                unit_of_measurement = 'metric',
                is_customs_declarable = False,
                monetary_amount = [
                    openapi_client.models.monetary_amount_inner.monetaryAmount_inner(
                        type_code = 'declaredValue', 
                        value = 100, 
                        currency = 'CZK', )
                    ],
                request_all_value_added_services = False,
                estimated_delivery_date = openapi_client.models.estimated_delivery_date.estimated delivery date(
                    is_requested = False, 
                    type_code = 'QDDF', ),
                get_additional_information = [
                    openapi_client.models.supermodel_io_logistics_express_rate_request_get_additional_information_inner.supermodelIoLogisticsExpressRateRequest_getAdditionalInformation_inner(
                        type_code = 'allValueAddedServices', 
                        is_requested = True, )
                    ],
                return_standard_products_only = False,
                next_business_day = False,
                product_type_code = 'all',
                packages = [
                    openapi_client.models.package_definition_for_/rates,_/products,_/landed_cost.Package definition for /rates, /products, /landed-cost(
                        type_code = '3BX', 
                        weight = 10.5, 
                        dimensions = openapi_client.models.dimensions.dimensions(
                            length = 25, 
                            width = 35, 
                            height = 15, ), )
                    ]
            )
        else:
            return SupermodelIoLogisticsExpressRateRequest(
                customer_details = openapi_client.models.supermodel_io_logistics_express_rate_request_customer_details.supermodelIoLogisticsExpressRateRequest_customerDetails(
                    shipper_details = openapi_client.models.address_definition_for_/rates,_/products,_/landed_cost.Address definition for /rates, /products, /landed-cost(
                        postal_code = '14800', 
                        city_name = 'Prague', 
                        country_code = 'CZ', 
                        province_code = 'CZ', 
                        address_line1 = 'addres1', 
                        address_line2 = 'addres2', 
                        address_line3 = 'addres3', 
                        county_name = 'Central Bohemia', ), 
                    receiver_details = openapi_client.models.address_definition_for_/rates,_/products,_/landed_cost.Address definition for /rates, /products, /landed-cost(
                        postal_code = '14800', 
                        city_name = 'Prague', 
                        country_code = 'CZ', 
                        province_code = 'CZ', 
                        address_line1 = 'addres1', 
                        address_line2 = 'addres2', 
                        address_line3 = 'addres3', 
                        county_name = 'Central Bohemia', ), ),
                planned_shipping_date_and_time = '2020-03-24T13:00:00GMT+00:00',
                unit_of_measurement = 'metric',
                is_customs_declarable = False,
                packages = [
                    openapi_client.models.package_definition_for_/rates,_/products,_/landed_cost.Package definition for /rates, /products, /landed-cost(
                        type_code = '3BX', 
                        weight = 10.5, 
                        dimensions = openapi_client.models.dimensions.dimensions(
                            length = 25, 
                            width = 35, 
                            height = 15, ), )
                    ],
        )
        """

    def testSupermodelIoLogisticsExpressRateRequest(self):
        """Test SupermodelIoLogisticsExpressRateRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()