# OpeningTime

Multiple opening hours entities can exist for the same week day.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**day_of_week** | **str** | Weekday for which this opening hours entity is valid. Possible values are: MONDAY, TUESDAY, WEDNESDAY, THURSDAY, FRIDAY, SATURDAY, SUNDAY, HOLIDAY | [optional] 
**opening_time** | **str** | The opening time of this entity | [optional] 
**closing_time** | **str** | The closing time of this entity | [optional] 

## Example

```python
from openapi_client.models.opening_time import OpeningTime

# TODO update the JSON string below
json = "{}"
# create an instance of OpeningTime from a JSON string
opening_time_instance = OpeningTime.from_json(json)
# print the JSON string representation of the object
print(OpeningTime.to_json())

# convert the object into a dict
opening_time_dict = opening_time_instance.to_dict()
# create an instance of OpeningTime from a dict
opening_time_from_dict = OpeningTime.from_dict(opening_time_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


