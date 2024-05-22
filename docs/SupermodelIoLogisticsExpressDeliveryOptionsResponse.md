# SupermodelIoLogisticsExpressDeliveryOptionsResponse

MyDHL API REST DeliveryOption response JSON Schema

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**delivery_options** | [**List[SupermodelIoLogisticsExpressDeliveryOptionsResponseDeliveryOptionsInner]**](SupermodelIoLogisticsExpressDeliveryOptionsResponseDeliveryOptionsInner.md) | Contains available deliveryOptions for the shipment | 
**warnings** | **List[str]** |  | [optional] 

## Example

```python
from openapi_client.models.supermodel_io_logistics_express_delivery_options_response import SupermodelIoLogisticsExpressDeliveryOptionsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SupermodelIoLogisticsExpressDeliveryOptionsResponse from a JSON string
supermodel_io_logistics_express_delivery_options_response_instance = SupermodelIoLogisticsExpressDeliveryOptionsResponse.from_json(json)
# print the JSON string representation of the object
print(SupermodelIoLogisticsExpressDeliveryOptionsResponse.to_json())

# convert the object into a dict
supermodel_io_logistics_express_delivery_options_response_dict = supermodel_io_logistics_express_delivery_options_response_instance.to_dict()
# create an instance of SupermodelIoLogisticsExpressDeliveryOptionsResponse from a dict
supermodel_io_logistics_express_delivery_options_response_from_dict = SupermodelIoLogisticsExpressDeliveryOptionsResponse.from_dict(supermodel_io_logistics_express_delivery_options_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


