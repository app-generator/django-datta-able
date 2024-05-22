# SupermodelIoLogisticsExpressTrackingResponse

tracking response schema

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**shipments** | [**List[SupermodelIoLogisticsExpressTrackingResponseShipmentsInner]**](SupermodelIoLogisticsExpressTrackingResponseShipmentsInner.md) |  | [optional] 

## Example

```python
from openapi_client.models.supermodel_io_logistics_express_tracking_response import SupermodelIoLogisticsExpressTrackingResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SupermodelIoLogisticsExpressTrackingResponse from a JSON string
supermodel_io_logistics_express_tracking_response_instance = SupermodelIoLogisticsExpressTrackingResponse.from_json(json)
# print the JSON string representation of the object
print(SupermodelIoLogisticsExpressTrackingResponse.to_json())

# convert the object into a dict
supermodel_io_logistics_express_tracking_response_dict = supermodel_io_logistics_express_tracking_response_instance.to_dict()
# create an instance of SupermodelIoLogisticsExpressTrackingResponse from a dict
supermodel_io_logistics_express_tracking_response_from_dict = SupermodelIoLogisticsExpressTrackingResponse.from_dict(supermodel_io_logistics_express_tracking_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


