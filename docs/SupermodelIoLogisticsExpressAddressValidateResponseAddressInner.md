# SupermodelIoLogisticsExpressAddressValidateResponseAddressInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**country_code** | **str** |  | 
**postal_code** | **str** |  | 
**city_name** | **str** |  | [optional] 
**county_name** | **str** | Please enter your suburb or county name | [optional] 
**service_area** | [**SupermodelIoLogisticsExpressAddressValidateResponseAddressInnerServiceArea**](SupermodelIoLogisticsExpressAddressValidateResponseAddressInnerServiceArea.md) |  | [optional] 

## Example

```python
from openapi_client.models.supermodel_io_logistics_express_address_validate_response_address_inner import SupermodelIoLogisticsExpressAddressValidateResponseAddressInner

# TODO update the JSON string below
json = "{}"
# create an instance of SupermodelIoLogisticsExpressAddressValidateResponseAddressInner from a JSON string
supermodel_io_logistics_express_address_validate_response_address_inner_instance = SupermodelIoLogisticsExpressAddressValidateResponseAddressInner.from_json(json)
# print the JSON string representation of the object
print(SupermodelIoLogisticsExpressAddressValidateResponseAddressInner.to_json())

# convert the object into a dict
supermodel_io_logistics_express_address_validate_response_address_inner_dict = supermodel_io_logistics_express_address_validate_response_address_inner_instance.to_dict()
# create an instance of SupermodelIoLogisticsExpressAddressValidateResponseAddressInner from a dict
supermodel_io_logistics_express_address_validate_response_address_inner_from_dict = SupermodelIoLogisticsExpressAddressValidateResponseAddressInner.from_dict(supermodel_io_logistics_express_address_validate_response_address_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


