# Holidays

Holiday details

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**open** | [**List[OpenDatesTime]**](OpenDatesTime.md) | Array of objects: {date, from, to}, where date is date and from and to is time | [optional] 
**closed** | [**List[ClosedDates]**](ClosedDates.md) | Array of dates:{from, to} when is closed. | [optional] 

## Example

```python
from openapi_client.models.holidays import Holidays

# TODO update the JSON string below
json = "{}"
# create an instance of Holidays from a JSON string
holidays_instance = Holidays.from_json(json)
# print the JSON string representation of the object
print(Holidays.to_json())

# convert the object into a dict
holidays_dict = holidays_instance.to_dict()
# create an instance of Holidays from a dict
holidays_from_dict = Holidays.from_dict(holidays_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


