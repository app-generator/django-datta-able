# SupermodelIoLogisticsExpressTrackingResponseShipmentsInnerShipperDetails


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Note: This field may be intentionally left empty in accordance with the General Data Protection Regulation (GDPR) requirements.                   | [optional] 
**postal_address** | [**SupermodelIoLogisticsExpressTrackingResponseShipmentsInnerShipperDetailsPostalAddress**](SupermodelIoLogisticsExpressTrackingResponseShipmentsInnerShipperDetailsPostalAddress.md) |  | [optional] 
**service_area** | [**List[SupermodelIoLogisticsExpressTrackingResponseShipmentsInnerShipperDetailsServiceAreaInner]**](SupermodelIoLogisticsExpressTrackingResponseShipmentsInnerShipperDetailsServiceAreaInner.md) |  | [optional] 

## Example

```python
from openapi_client.models.supermodel_io_logistics_express_tracking_response_shipments_inner_shipper_details import SupermodelIoLogisticsExpressTrackingResponseShipmentsInnerShipperDetails

# TODO update the JSON string below
json = "{}"
# create an instance of SupermodelIoLogisticsExpressTrackingResponseShipmentsInnerShipperDetails from a JSON string
supermodel_io_logistics_express_tracking_response_shipments_inner_shipper_details_instance = SupermodelIoLogisticsExpressTrackingResponseShipmentsInnerShipperDetails.from_json(json)
# print the JSON string representation of the object
print(SupermodelIoLogisticsExpressTrackingResponseShipmentsInnerShipperDetails.to_json())

# convert the object into a dict
supermodel_io_logistics_express_tracking_response_shipments_inner_shipper_details_dict = supermodel_io_logistics_express_tracking_response_shipments_inner_shipper_details_instance.to_dict()
# create an instance of SupermodelIoLogisticsExpressTrackingResponseShipmentsInnerShipperDetails from a dict
supermodel_io_logistics_express_tracking_response_shipments_inner_shipper_details_from_dict = SupermodelIoLogisticsExpressTrackingResponseShipmentsInnerShipperDetails.from_dict(supermodel_io_logistics_express_tracking_response_shipments_inner_shipper_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


