# coding: utf-8

"""
    DHL Express APIs (MyDHL API)

    Welcome to the official DHL Express APIs (MyDHL API) below are the published API Documentation to fulfill your shipping needs with DHL Express.       Please follow the process described [here](https://developer.dhl.com/api-reference/dhl-express-mydhl-api#get-started-section/user-guide--get-access) to request access to the DHL Express - MyDHL API services   In case you already have DHL Express - MyDHL API Service credentials please ensure to use the endpoints/environments listed  [here](https://developer.dhl.com/api-reference/dhl-express-mydhl-api#get-started-section/user-guide--environments) 

    The version of the OpenAPI document: 2.11.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.supermodel_io_logistics_express_tracking_response_shipments_inner_pieces_inner import SupermodelIoLogisticsExpressTrackingResponseShipmentsInnerPiecesInner

class TestSupermodelIoLogisticsExpressTrackingResponseShipmentsInnerPiecesInner(unittest.TestCase):
    """SupermodelIoLogisticsExpressTrackingResponseShipmentsInnerPiecesInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> SupermodelIoLogisticsExpressTrackingResponseShipmentsInnerPiecesInner:
        """Test SupermodelIoLogisticsExpressTrackingResponseShipmentsInnerPiecesInner
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `SupermodelIoLogisticsExpressTrackingResponseShipmentsInnerPiecesInner`
        """
        model = SupermodelIoLogisticsExpressTrackingResponseShipmentsInnerPiecesInner()
        if include_optional:
            return SupermodelIoLogisticsExpressTrackingResponseShipmentsInnerPiecesInner(
                number = 1,
                type_code = '',
                shipment_tracking_number = '',
                tracking_number = '',
                description = '',
                weight = 22.5,
                dimensional_weight = 22.5,
                actual_weight = 22.5,
                dimensions = openapi_client.models.dimensions.dimensions(
                    length = 15, 
                    width = 15, 
                    height = 40, ),
                actual_dimensions = openapi_client.models.dimensions.dimensions(
                    length = 15, 
                    width = 15, 
                    height = 40, ),
                unit_of_measurements = '',
                shipper_references = [
                    openapi_client.models.reference_definition.Reference definition(
                        value = 'Customer reference', 
                        type_code = 'CU', )
                    ],
                events = [
                    openapi_client.models.supermodel_io_logistics_express_tracking_response_shipments_inner_pieces_inner_events_inner.supermodelIoLogisticsExpressTrackingResponse_shipments_inner_pieces_inner_events_inner(
                        date = '', 
                        gmt_offset = '+09:00', 
                        time = '', 
                        type_code = '', 
                        description = '', 
                        service_area = [
                            openapi_client.models.supermodel_io_logistics_express_tracking_response_shipments_inner_pieces_inner_events_inner_service_area_inner.supermodelIoLogisticsExpressTrackingResponse_shipments_inner_pieces_inner_events_inner_serviceArea_inner(
                                code = '', 
                                description = '', )
                            ], 
                        signed_by = '', )
                    ]
            )
        else:
            return SupermodelIoLogisticsExpressTrackingResponseShipmentsInnerPiecesInner(
                events = [
                    openapi_client.models.supermodel_io_logistics_express_tracking_response_shipments_inner_pieces_inner_events_inner.supermodelIoLogisticsExpressTrackingResponse_shipments_inner_pieces_inner_events_inner(
                        date = '', 
                        gmt_offset = '+09:00', 
                        time = '', 
                        type_code = '', 
                        description = '', 
                        service_area = [
                            openapi_client.models.supermodel_io_logistics_express_tracking_response_shipments_inner_pieces_inner_events_inner_service_area_inner.supermodelIoLogisticsExpressTrackingResponse_shipments_inner_pieces_inner_events_inner_serviceArea_inner(
                                code = '', 
                                description = '', )
                            ], 
                        signed_by = '', )
                    ],
        )
        """

    def testSupermodelIoLogisticsExpressTrackingResponseShipmentsInnerPiecesInner(self):
        """Test SupermodelIoLogisticsExpressTrackingResponseShipmentsInnerPiecesInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
