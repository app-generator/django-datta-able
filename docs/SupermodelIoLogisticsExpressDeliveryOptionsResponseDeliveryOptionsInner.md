# SupermodelIoLogisticsExpressDeliveryOptionsResponseDeliveryOptionsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | The name of delivery option\&quot; | 
**parameters** | [**List[SupermodelIoLogisticsExpressDeliveryOptionsResponseDeliveryOptionsInnerParametersInner]**](SupermodelIoLogisticsExpressDeliveryOptionsResponseDeliveryOptionsInnerParametersInner.md) |  | 
**service_point_url** | **str** | Returned only for type&#x3D;servicePoint | [optional] 
**delivery_windows** | [**List[SupermodelIoLogisticsExpressDeliveryOptionsResponseDeliveryOptionsInnerDeliveryWindowsInner]**](SupermodelIoLogisticsExpressDeliveryOptionsResponseDeliveryOptionsInnerDeliveryWindowsInner.md) | Returned only for type&#x3D;scheduleDelivery and vacationHold. Important: the start and end datetime field values must be among the options provided in GET delivery-option response.  | [optional] 

## Example

```python
from openapi_client.models.supermodel_io_logistics_express_delivery_options_response_delivery_options_inner import SupermodelIoLogisticsExpressDeliveryOptionsResponseDeliveryOptionsInner

# TODO update the JSON string below
json = "{}"
# create an instance of SupermodelIoLogisticsExpressDeliveryOptionsResponseDeliveryOptionsInner from a JSON string
supermodel_io_logistics_express_delivery_options_response_delivery_options_inner_instance = SupermodelIoLogisticsExpressDeliveryOptionsResponseDeliveryOptionsInner.from_json(json)
# print the JSON string representation of the object
print(SupermodelIoLogisticsExpressDeliveryOptionsResponseDeliveryOptionsInner.to_json())

# convert the object into a dict
supermodel_io_logistics_express_delivery_options_response_delivery_options_inner_dict = supermodel_io_logistics_express_delivery_options_response_delivery_options_inner_instance.to_dict()
# create an instance of SupermodelIoLogisticsExpressDeliveryOptionsResponseDeliveryOptionsInner from a dict
supermodel_io_logistics_express_delivery_options_response_delivery_options_inner_from_dict = SupermodelIoLogisticsExpressDeliveryOptionsResponseDeliveryOptionsInner.from_dict(supermodel_io_logistics_express_delivery_options_response_delivery_options_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


