# SupermodelIoLogisticsExpressTrackingResponseShipmentsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**shipment_tracking_number** | **str** |  | [optional] 
**status** | **str** |  | [optional] 
**shipment_timestamp** | **str** |  | [optional] 
**product_code** | **str** | DHL product code | [optional] 
**description** | **str** |  | [optional] 
**shipper_details** | [**SupermodelIoLogisticsExpressTrackingResponseShipmentsInnerShipperDetails**](SupermodelIoLogisticsExpressTrackingResponseShipmentsInnerShipperDetails.md) |  | [optional] 
**receiver_details** | [**SupermodelIoLogisticsExpressTrackingResponseShipmentsInnerReceiverDetails**](SupermodelIoLogisticsExpressTrackingResponseShipmentsInnerReceiverDetails.md) |  | [optional] 
**total_weight** | **float** |  | [optional] 
**unit_of_measurements** | **str** |  | [optional] 
**shipper_references** | [**List[SupermodelIoLogisticsExpressReference]**](SupermodelIoLogisticsExpressReference.md) |  | [optional] 
**events** | [**List[SupermodelIoLogisticsExpressTrackingResponseShipmentsInnerEventsInner]**](SupermodelIoLogisticsExpressTrackingResponseShipmentsInnerEventsInner.md) |  | 
**number_of_pieces** | **float** |  | [optional] 
**pieces** | [**List[SupermodelIoLogisticsExpressTrackingResponseShipmentsInnerPiecesInner]**](SupermodelIoLogisticsExpressTrackingResponseShipmentsInnerPiecesInner.md) |  | [optional] 
**estimated_delivery_date** | **str** |  | [optional] 
**children_shipment_identification_numbers** | **List[str]** |  | [optional] 
**controlled_access_data_codes** | **List[str]** | controlled access data codes such as &#39;SHPR_CTY&#39; for shipper&#39;s city, &#39;CNSGN_CTY&#39; for consignee&#39;s city, &#39;SVP_URL&#39; for service point URL, &#39;SVP_FAC&#39; for service point facility code and &#39;SIGN_NM&#39; for signatory name. | [optional] 

## Example

```python
from openapi_client.models.supermodel_io_logistics_express_tracking_response_shipments_inner import SupermodelIoLogisticsExpressTrackingResponseShipmentsInner

# TODO update the JSON string below
json = "{}"
# create an instance of SupermodelIoLogisticsExpressTrackingResponseShipmentsInner from a JSON string
supermodel_io_logistics_express_tracking_response_shipments_inner_instance = SupermodelIoLogisticsExpressTrackingResponseShipmentsInner.from_json(json)
# print the JSON string representation of the object
print(SupermodelIoLogisticsExpressTrackingResponseShipmentsInner.to_json())

# convert the object into a dict
supermodel_io_logistics_express_tracking_response_shipments_inner_dict = supermodel_io_logistics_express_tracking_response_shipments_inner_instance.to_dict()
# create an instance of SupermodelIoLogisticsExpressTrackingResponseShipmentsInner from a dict
supermodel_io_logistics_express_tracking_response_shipments_inner_from_dict = SupermodelIoLogisticsExpressTrackingResponseShipmentsInner.from_dict(supermodel_io_logistics_express_tracking_response_shipments_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


