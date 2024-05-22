# SupermodelIoLogisticsExpressTrackingResponseShipmentsInnerReceiverDetails


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Note: This field may be intentionally left empty in accordance with the General Data Protection Regulation (GDPR) requirements. | [optional] 
**postal_address** | [**SupermodelIoLogisticsExpressTrackingResponseShipmentsInnerReceiverDetailsPostalAddress**](SupermodelIoLogisticsExpressTrackingResponseShipmentsInnerReceiverDetailsPostalAddress.md) |  | [optional] 
**service_area** | [**List[SupermodelIoLogisticsExpressTrackingResponseShipmentsInnerReceiverDetailsServiceAreaInner]**](SupermodelIoLogisticsExpressTrackingResponseShipmentsInnerReceiverDetailsServiceAreaInner.md) |  | [optional] 

## Example

```python
from openapi_client.models.supermodel_io_logistics_express_tracking_response_shipments_inner_receiver_details import SupermodelIoLogisticsExpressTrackingResponseShipmentsInnerReceiverDetails

# TODO update the JSON string below
json = "{}"
# create an instance of SupermodelIoLogisticsExpressTrackingResponseShipmentsInnerReceiverDetails from a JSON string
supermodel_io_logistics_express_tracking_response_shipments_inner_receiver_details_instance = SupermodelIoLogisticsExpressTrackingResponseShipmentsInnerReceiverDetails.from_json(json)
# print the JSON string representation of the object
print(SupermodelIoLogisticsExpressTrackingResponseShipmentsInnerReceiverDetails.to_json())

# convert the object into a dict
supermodel_io_logistics_express_tracking_response_shipments_inner_receiver_details_dict = supermodel_io_logistics_express_tracking_response_shipments_inner_receiver_details_instance.to_dict()
# create an instance of SupermodelIoLogisticsExpressTrackingResponseShipmentsInnerReceiverDetails from a dict
supermodel_io_logistics_express_tracking_response_shipments_inner_receiver_details_from_dict = SupermodelIoLogisticsExpressTrackingResponseShipmentsInnerReceiverDetails.from_dict(supermodel_io_logistics_express_tracking_response_shipments_inner_receiver_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


