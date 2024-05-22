# ValueUnit

Max. weight per piece

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | **float** | Value in BigDecimal | [optional] 
**uom** | **str** | UOM | [optional] 

## Example

```python
from openapi_client.models.value_unit import ValueUnit

# TODO update the JSON string below
json = "{}"
# create an instance of ValueUnit from a JSON string
value_unit_instance = ValueUnit.from_json(json)
# print the JSON string representation of the object
print(ValueUnit.to_json())

# convert the object into a dict
value_unit_dict = value_unit_instance.to_dict()
# create an instance of ValueUnit from a dict
value_unit_from_dict = ValueUnit.from_dict(value_unit_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


