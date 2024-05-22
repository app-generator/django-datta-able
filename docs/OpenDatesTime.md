# OpenDatesTime

Array of objects: {date, from, to}, where date is date and from and to is time

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_date** | **str** | Date – when is open during holidays | [optional] 
**var_from** | **str** | Time – beginning of open hours | [optional] 
**to** | **str** | Time – end of open hours | [optional] 

## Example

```python
from openapi_client.models.open_dates_time import OpenDatesTime

# TODO update the JSON string below
json = "{}"
# create an instance of OpenDatesTime from a JSON string
open_dates_time_instance = OpenDatesTime.from_json(json)
# print the JSON string representation of the object
print(OpenDatesTime.to_json())

# convert the object into a dict
open_dates_time_dict = open_dates_time_instance.to_dict()
# create an instance of OpenDatesTime from a dict
open_dates_time_from_dict = OpenDatesTime.from_dict(open_dates_time_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


