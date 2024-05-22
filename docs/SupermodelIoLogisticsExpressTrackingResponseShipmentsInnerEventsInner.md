# SupermodelIoLogisticsExpressTrackingResponseShipmentsInnerEventsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_date** | **str** |  | [optional] 
**time** | **str** |  | [optional] 
**gmt_offset** | **str** |  | [optional] 
**type_code** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**service_area** | [**List[SupermodelIoLogisticsExpressTrackingResponseShipmentsInnerEventsInnerServiceAreaInner]**](SupermodelIoLogisticsExpressTrackingResponseShipmentsInnerEventsInnerServiceAreaInner.md) |  | [optional] 
**signed_by** | **str** | Note: This field may be intentionally left empty in accordance with the General Data Protection Regulation (GDPR) requirements.     | [optional] 

## Example

```python
from openapi_client.models.supermodel_io_logistics_express_tracking_response_shipments_inner_events_inner import SupermodelIoLogisticsExpressTrackingResponseShipmentsInnerEventsInner

# TODO update the JSON string below
json = "{}"
# create an instance of SupermodelIoLogisticsExpressTrackingResponseShipmentsInnerEventsInner from a JSON string
supermodel_io_logistics_express_tracking_response_shipments_inner_events_inner_instance = SupermodelIoLogisticsExpressTrackingResponseShipmentsInnerEventsInner.from_json(json)
# print the JSON string representation of the object
print(SupermodelIoLogisticsExpressTrackingResponseShipmentsInnerEventsInner.to_json())

# convert the object into a dict
supermodel_io_logistics_express_tracking_response_shipments_inner_events_inner_dict = supermodel_io_logistics_express_tracking_response_shipments_inner_events_inner_instance.to_dict()
# create an instance of SupermodelIoLogisticsExpressTrackingResponseShipmentsInnerEventsInner from a dict
supermodel_io_logistics_express_tracking_response_shipments_inner_events_inner_from_dict = SupermodelIoLogisticsExpressTrackingResponseShipmentsInnerEventsInner.from_dict(supermodel_io_logistics_express_tracking_response_shipments_inner_events_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


