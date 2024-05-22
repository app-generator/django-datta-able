# LocalTime

Array of openingHours entities, each consisting of week day, opening time and closing time.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**chronology** | [**Chronology**](Chronology.md) |  | [optional] 
**hour_of_day** | **int** |  | [optional] 
**minute_of_hour** | **int** |  | [optional] 
**second_of_minute** | **int** |  | [optional] 
**millis_of_second** | **int** |  | [optional] 
**millis_of_day** | **int** |  | [optional] 
**fields** | [**List[DateTimeField]**](DateTimeField.md) |  | [optional] 
**values** | **List[int]** |  | [optional] 
**field_types** | [**List[DateTimeFieldType]**](DateTimeFieldType.md) |  | [optional] 

## Example

```python
from openapi_client.models.local_time import LocalTime

# TODO update the JSON string below
json = "{}"
# create an instance of LocalTime from a JSON string
local_time_instance = LocalTime.from_json(json)
# print the JSON string representation of the object
print(LocalTime.to_json())

# convert the object into a dict
local_time_dict = local_time_instance.to_dict()
# create an instance of LocalTime from a dict
local_time_from_dict = LocalTime.from_dict(local_time_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


