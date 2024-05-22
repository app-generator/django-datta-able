# SupermodelIoLogisticsExpressAddressValidateResponse

Comment describing your JSON Schema

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**warnings** | **List[str]** |  | [optional] 
**address** | [**List[SupermodelIoLogisticsExpressAddressValidateResponseAddressInner]**](SupermodelIoLogisticsExpressAddressValidateResponseAddressInner.md) |  | [optional] 

## Example

```python
from openapi_client.models.supermodel_io_logistics_express_address_validate_response import SupermodelIoLogisticsExpressAddressValidateResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SupermodelIoLogisticsExpressAddressValidateResponse from a JSON string
supermodel_io_logistics_express_address_validate_response_instance = SupermodelIoLogisticsExpressAddressValidateResponse.from_json(json)
# print the JSON string representation of the object
print(SupermodelIoLogisticsExpressAddressValidateResponse.to_json())

# convert the object into a dict
supermodel_io_logistics_express_address_validate_response_dict = supermodel_io_logistics_express_address_validate_response_instance.to_dict()
# create an instance of SupermodelIoLogisticsExpressAddressValidateResponse from a dict
supermodel_io_logistics_express_address_validate_response_from_dict = SupermodelIoLogisticsExpressAddressValidateResponse.from_dict(supermodel_io_logistics_express_address_validate_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


