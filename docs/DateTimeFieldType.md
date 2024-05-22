# DateTimeFieldType


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**duration_type** | [**DurationFieldType**](DurationFieldType.md) |  | [optional] 
**range_duration_type** | [**DurationFieldType**](DurationFieldType.md) |  | [optional] 

## Example

```python
from openapi_client.models.date_time_field_type import DateTimeFieldType

# TODO update the JSON string below
json = "{}"
# create an instance of DateTimeFieldType from a JSON string
date_time_field_type_instance = DateTimeFieldType.from_json(json)
# print the JSON string representation of the object
print(DateTimeFieldType.to_json())

# convert the object into a dict
date_time_field_type_dict = date_time_field_type_instance.to_dict()
# create an instance of DateTimeFieldType from a dict
date_time_field_type_from_dict = DateTimeFieldType.from_dict(date_time_field_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


