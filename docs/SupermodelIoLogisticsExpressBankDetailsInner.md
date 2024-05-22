# SupermodelIoLogisticsExpressBankDetailsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | To be mapped in commercial Invoice - Russia Bank Name field | [optional] 
**settlement_local_currency** | **str** | To be mapped in commercial Invoice - Russia Bank Settlement Account Number in RUR field | [optional] 
**settlement_foreign_currency** | **str** | To be mapped in commercial Invoice - Russia Bank Settlement Account Number in RUR field | [optional] 

## Example

```python
from openapi_client.models.supermodel_io_logistics_express_bank_details_inner import SupermodelIoLogisticsExpressBankDetailsInner

# TODO update the JSON string below
json = "{}"
# create an instance of SupermodelIoLogisticsExpressBankDetailsInner from a JSON string
supermodel_io_logistics_express_bank_details_inner_instance = SupermodelIoLogisticsExpressBankDetailsInner.from_json(json)
# print the JSON string representation of the object
print(SupermodelIoLogisticsExpressBankDetailsInner.to_json())

# convert the object into a dict
supermodel_io_logistics_express_bank_details_inner_dict = supermodel_io_logistics_express_bank_details_inner_instance.to_dict()
# create an instance of SupermodelIoLogisticsExpressBankDetailsInner from a dict
supermodel_io_logistics_express_bank_details_inner_from_dict = SupermodelIoLogisticsExpressBankDetailsInner.from_dict(supermodel_io_logistics_express_bank_details_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


