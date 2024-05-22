# MonetaryAmountInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type_code** | **str** | Please provide the monetary amount type | 
**value** | **float** | Please provide the monetary value | 
**currency** | **str** | Pleaseprovide monetary amount currency code | 

## Example

```python
from openapi_client.models.monetary_amount_inner import MonetaryAmountInner

# TODO update the JSON string below
json = "{}"
# create an instance of MonetaryAmountInner from a JSON string
monetary_amount_inner_instance = MonetaryAmountInner.from_json(json)
# print the JSON string representation of the object
print(MonetaryAmountInner.to_json())

# convert the object into a dict
monetary_amount_inner_dict = monetary_amount_inner_instance.to_dict()
# create an instance of MonetaryAmountInner from a dict
monetary_amount_inner_from_dict = MonetaryAmountInner.from_dict(monetary_amount_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


