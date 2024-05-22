# SupermodelIoLogisticsExpressTrackingResponseShipmentsInnerPiecesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**number** | **float** |  | [optional] 
**type_code** | **str** |  | [optional] 
**shipment_tracking_number** | **str** |  | [optional] 
**tracking_number** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**weight** | **float** | The weight of the package. | [optional] 
**dimensional_weight** | **float** | The weight of the package. | [optional] 
**actual_weight** | **float** | The weight of the package. | [optional] 
**dimensions** | [**Dimensions2**](Dimensions2.md) |  | [optional] 
**actual_dimensions** | [**Dimensions3**](Dimensions3.md) |  | [optional] 
**unit_of_measurements** | **str** |  | [optional] 
**shipper_references** | [**List[SupermodelIoLogisticsExpressReference]**](SupermodelIoLogisticsExpressReference.md) |  | [optional] 
**events** | [**List[SupermodelIoLogisticsExpressTrackingResponseShipmentsInnerPiecesInnerEventsInner]**](SupermodelIoLogisticsExpressTrackingResponseShipmentsInnerPiecesInnerEventsInner.md) |  | 

## Example

```python
from openapi_client.models.supermodel_io_logistics_express_tracking_response_shipments_inner_pieces_inner import SupermodelIoLogisticsExpressTrackingResponseShipmentsInnerPiecesInner

# TODO update the JSON string below
json = "{}"
# create an instance of SupermodelIoLogisticsExpressTrackingResponseShipmentsInnerPiecesInner from a JSON string
supermodel_io_logistics_express_tracking_response_shipments_inner_pieces_inner_instance = SupermodelIoLogisticsExpressTrackingResponseShipmentsInnerPiecesInner.from_json(json)
# print the JSON string representation of the object
print(SupermodelIoLogisticsExpressTrackingResponseShipmentsInnerPiecesInner.to_json())

# convert the object into a dict
supermodel_io_logistics_express_tracking_response_shipments_inner_pieces_inner_dict = supermodel_io_logistics_express_tracking_response_shipments_inner_pieces_inner_instance.to_dict()
# create an instance of SupermodelIoLogisticsExpressTrackingResponseShipmentsInnerPiecesInner from a dict
supermodel_io_logistics_express_tracking_response_shipments_inner_pieces_inner_from_dict = SupermodelIoLogisticsExpressTrackingResponseShipmentsInnerPiecesInner.from_dict(supermodel_io_logistics_express_tracking_response_shipments_inner_pieces_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


