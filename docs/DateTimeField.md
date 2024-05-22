# DateTimeField


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**type** | [**DateTimeFieldType**](DateTimeFieldType.md) |  | [optional] 
**supported** | **bool** |  | [optional] 
**lenient** | **bool** |  | [optional] 
**minimum_value** | **int** |  | [optional] 
**maximum_value** | **int** |  | [optional] 
**duration_field** | [**DurationField**](DurationField.md) |  | [optional] 
**range_duration_field** | [**DurationField**](DurationField.md) |  | [optional] 
**leap_duration_field** | [**DurationField**](DurationField.md) |  | [optional] 

## Example

```python
from openapi_client.models.date_time_field import DateTimeField

# TODO update the JSON string below
json = "{}"
# create an instance of DateTimeField from a JSON string
date_time_field_instance = DateTimeField.from_json(json)
# print the JSON string representation of the object
print(DateTimeField.to_json())

# convert the object into a dict
date_time_field_dict = date_time_field_instance.to_dict()
# create an instance of DateTimeField from a dict
date_time_field_from_dict = DateTimeField.from_dict(date_time_field_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


