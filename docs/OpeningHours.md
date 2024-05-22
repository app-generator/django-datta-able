# OpeningHours

Array of openingHours entities, each consisting of week day, opening time and closing time.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**opening_hours** | [**List[OpeningTime]**](OpeningTime.md) | Multiple opening hours entities can exist for the same week day. | 
**holiday_dates** | **List[date]** | Holiday details with date | [optional] 
**holidays_dates** | **Dict[str, List[date]]** | Holiday details with date | [optional] 
**html** | **str** | Obsolete. This is planned to be removed in future releases. | [optional] 
**holiday_opening_hours_html** | **str** | Obsolete. This is planned to be removed in future releases. | [optional] 
**holidays** | [**Holidays**](Holidays.md) |  | [optional] 

## Example

```python
from openapi_client.models.opening_hours import OpeningHours

# TODO update the JSON string below
json = "{}"
# create an instance of OpeningHours from a JSON string
opening_hours_instance = OpeningHours.from_json(json)
# print the JSON string representation of the object
print(OpeningHours.to_json())

# convert the object into a dict
opening_hours_dict = opening_hours_instance.to_dict()
# create an instance of OpeningHours from a dict
opening_hours_from_dict = OpeningHours.from_dict(opening_hours_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


