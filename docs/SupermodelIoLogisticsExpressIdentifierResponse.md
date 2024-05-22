# SupermodelIoLogisticsExpressIdentifierResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**warnings** | **List[str]** |  | [optional] 
**identifiers** | [**List[SupermodelIoLogisticsExpressIdentifierResponseIdentifiersInner]**](SupermodelIoLogisticsExpressIdentifierResponseIdentifiersInner.md) |  | [optional] 

## Example

```python
from openapi_client.models.supermodel_io_logistics_express_identifier_response import SupermodelIoLogisticsExpressIdentifierResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SupermodelIoLogisticsExpressIdentifierResponse from a JSON string
supermodel_io_logistics_express_identifier_response_instance = SupermodelIoLogisticsExpressIdentifierResponse.from_json(json)
# print the JSON string representation of the object
print(SupermodelIoLogisticsExpressIdentifierResponse.to_json())

# convert the object into a dict
supermodel_io_logistics_express_identifier_response_dict = supermodel_io_logistics_express_identifier_response_instance.to_dict()
# create an instance of SupermodelIoLogisticsExpressIdentifierResponse from a dict
supermodel_io_logistics_express_identifier_response_from_dict = SupermodelIoLogisticsExpressIdentifierResponse.from_dict(supermodel_io_logistics_express_identifier_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


