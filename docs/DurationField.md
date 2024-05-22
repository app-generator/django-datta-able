# DurationField


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**type** | [**DurationFieldType**](DurationFieldType.md) |  | [optional] 
**supported** | **bool** |  | [optional] 
**unit_millis** | **int** |  | [optional] 
**precise** | **bool** |  | [optional] 

## Example

```python
from openapi_client.models.duration_field import DurationField

# TODO update the JSON string below
json = "{}"
# create an instance of DurationField from a JSON string
duration_field_instance = DurationField.from_json(json)
# print the JSON string representation of the object
print(DurationField.to_json())

# convert the object into a dict
duration_field_dict = duration_field_instance.to_dict()
# create an instance of DurationField from a dict
duration_field_from_dict = DurationField.from_dict(duration_field_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


