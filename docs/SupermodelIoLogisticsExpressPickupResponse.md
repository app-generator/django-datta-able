# SupermodelIoLogisticsExpressPickupResponse

Comment describing your JSON Schema

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dispatch_confirmation_numbers** | **List[str]** | List of Dispatch Confirmation Numbers which identifies the scheduled pickup | [optional] 
**ready_by_time** | **str** |  | [optional] 
**next_pickup_date** | **str** |  | [optional] 
**warnings** | **List[str]** |  | [optional] 

## Example

```python
from openapi_client.models.supermodel_io_logistics_express_pickup_response import SupermodelIoLogisticsExpressPickupResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SupermodelIoLogisticsExpressPickupResponse from a JSON string
supermodel_io_logistics_express_pickup_response_instance = SupermodelIoLogisticsExpressPickupResponse.from_json(json)
# print the JSON string representation of the object
print(SupermodelIoLogisticsExpressPickupResponse.to_json())

# convert the object into a dict
supermodel_io_logistics_express_pickup_response_dict = supermodel_io_logistics_express_pickup_response_instance.to_dict()
# create an instance of SupermodelIoLogisticsExpressPickupResponse from a dict
supermodel_io_logistics_express_pickup_response_from_dict = SupermodelIoLogisticsExpressPickupResponse.from_dict(supermodel_io_logistics_express_pickup_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


