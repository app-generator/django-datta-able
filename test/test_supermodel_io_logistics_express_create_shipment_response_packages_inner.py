# coding: utf-8

"""
    DHL Express APIs (MyDHL API)

    Welcome to the official DHL Express APIs (MyDHL API) below are the published API Documentation to fulfill your shipping needs with DHL Express.       Please follow the process described [here](https://developer.dhl.com/api-reference/dhl-express-mydhl-api#get-started-section/user-guide--get-access) to request access to the DHL Express - MyDHL API services   In case you already have DHL Express - MyDHL API Service credentials please ensure to use the endpoints/environments listed  [here](https://developer.dhl.com/api-reference/dhl-express-mydhl-api#get-started-section/user-guide--environments) 

    The version of the OpenAPI document: 2.11.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.supermodel_io_logistics_express_create_shipment_response_packages_inner import SupermodelIoLogisticsExpressCreateShipmentResponsePackagesInner

class TestSupermodelIoLogisticsExpressCreateShipmentResponsePackagesInner(unittest.TestCase):
    """SupermodelIoLogisticsExpressCreateShipmentResponsePackagesInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> SupermodelIoLogisticsExpressCreateShipmentResponsePackagesInner:
        """Test SupermodelIoLogisticsExpressCreateShipmentResponsePackagesInner
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `SupermodelIoLogisticsExpressCreateShipmentResponsePackagesInner`
        """
        model = SupermodelIoLogisticsExpressCreateShipmentResponsePackagesInner()
        if include_optional:
            return SupermodelIoLogisticsExpressCreateShipmentResponsePackagesInner(
                reference_number = 1,
                tracking_number = 'JD914600003889482921',
                tracking_url = 'https://express.api.dhl.com/mydhlapi/shipments/1234567890/tracking?PieceID=JD014600003889482921',
                volumetric_weight = 2.5,
                documents = [
                    openapi_client.models.supermodel_io_logistics_express_create_shipment_response_packages_inner_documents_inner.supermodelIoLogisticsExpressCreateShipmentResponse_packages_inner_documents_inner(
                        image_format = 'PNG', 
                        content = 'base64 encoded document', 
                        type_code = 'qr-code', )
                    ]
            )
        else:
            return SupermodelIoLogisticsExpressCreateShipmentResponsePackagesInner(
                tracking_number = 'JD914600003889482921',
        )
        """

    def testSupermodelIoLogisticsExpressCreateShipmentResponsePackagesInner(self):
        """Test SupermodelIoLogisticsExpressCreateShipmentResponsePackagesInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()