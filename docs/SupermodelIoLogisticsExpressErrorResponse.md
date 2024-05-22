# SupermodelIoLogisticsExpressErrorResponse

error message

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**instance** | **str** |  | [optional] 
**detail** | **str** |  | [optional] 
**title** | **str** |  | [optional] 
**message** | **str** |  | [optional] 
**additional_details** | **List[str]** |  | [optional] 
**status** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.supermodel_io_logistics_express_error_response import SupermodelIoLogisticsExpressErrorResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SupermodelIoLogisticsExpressErrorResponse from a JSON string
supermodel_io_logistics_express_error_response_instance = SupermodelIoLogisticsExpressErrorResponse.from_json(json)
# print the JSON string representation of the object
print(SupermodelIoLogisticsExpressErrorResponse.to_json())

# convert the object into a dict
supermodel_io_logistics_express_error_response_dict = supermodel_io_logistics_express_error_response_instance.to_dict()
# create an instance of SupermodelIoLogisticsExpressErrorResponse from a dict
supermodel_io_logistics_express_error_response_from_dict = SupermodelIoLogisticsExpressErrorResponse.from_dict(supermodel_io_logistics_express_error_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


