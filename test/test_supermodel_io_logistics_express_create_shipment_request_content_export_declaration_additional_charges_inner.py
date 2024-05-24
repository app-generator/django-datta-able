# coding: utf-8

"""
    DHL Express APIs (MyDHL API)

    Welcome to the official DHL Express APIs (MyDHL API) below are the published API Documentation to fulfill your shipping needs with DHL Express.       Please follow the process described [here](https://developer.dhl.com/api-reference/dhl-express-mydhl-api#get-started-section/user-guide--get-access) to request access to the DHL Express - MyDHL API services   In case you already have DHL Express - MyDHL API Service credentials please ensure to use the endpoints/environments listed  [here](https://developer.dhl.com/api-reference/dhl-express-mydhl-api#get-started-section/user-guide--environments) 

    The version of the OpenAPI document: 2.11.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.supermodel_io_logistics_express_create_shipment_request_content_export_declaration_additional_charges_inner import SupermodelIoLogisticsExpressCreateShipmentRequestContentExportDeclarationAdditionalChargesInner

class TestSupermodelIoLogisticsExpressCreateShipmentRequestContentExportDeclarationAdditionalChargesInner(unittest.TestCase):
    """SupermodelIoLogisticsExpressCreateShipmentRequestContentExportDeclarationAdditionalChargesInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> SupermodelIoLogisticsExpressCreateShipmentRequestContentExportDeclarationAdditionalChargesInner:
        """Test SupermodelIoLogisticsExpressCreateShipmentRequestContentExportDeclarationAdditionalChargesInner
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `SupermodelIoLogisticsExpressCreateShipmentRequestContentExportDeclarationAdditionalChargesInner`
        """
        model = SupermodelIoLogisticsExpressCreateShipmentRequestContentExportDeclarationAdditionalChargesInner()
        if include_optional:
            return SupermodelIoLogisticsExpressCreateShipmentRequestContentExportDeclarationAdditionalChargesInner(
                value = 10,
                caption = 'fee',
                type_code = 'freight'
            )
        else:
            return SupermodelIoLogisticsExpressCreateShipmentRequestContentExportDeclarationAdditionalChargesInner(
                value = 10,
                type_code = 'freight',
        )
        """

    def testSupermodelIoLogisticsExpressCreateShipmentRequestContentExportDeclarationAdditionalChargesInner(self):
        """Test SupermodelIoLogisticsExpressCreateShipmentRequestContentExportDeclarationAdditionalChargesInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()