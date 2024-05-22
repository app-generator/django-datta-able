# ClosedDates

Array of dates:{from, to} when is closed.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_from** | **str** | Date – start when it is closed | [optional] 
**to** | **str** | Date – end when it is closed | [optional] 

## Example

```python
from openapi_client.models.closed_dates import ClosedDates

# TODO update the JSON string below
json = "{}"
# create an instance of ClosedDates from a JSON string
closed_dates_instance = ClosedDates.from_json(json)
# print the JSON string representation of the object
print(ClosedDates.to_json())

# convert the object into a dict
closed_dates_dict = closed_dates_instance.to_dict()
# create an instance of ClosedDates from a dict
closed_dates_from_dict = ClosedDates.from_dict(closed_dates_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


