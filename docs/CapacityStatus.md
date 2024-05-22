# CapacityStatus

Capacity information – only if additional call to SCMS was triggered

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sev** | **str** | Severity code | [optional] 
**msg_clg** | **str** | SCMS | [optional] 
**msg_c_igd** | **str** | SCMS Status code | [optional] 
**dsc** | **str** | SCMS Description of status code | [optional] 
**dtl_dsc** | **str** | SCMS detailed description | [optional] 

## Example

```python
from openapi_client.models.capacity_status import CapacityStatus

# TODO update the JSON string below
json = "{}"
# create an instance of CapacityStatus from a JSON string
capacity_status_instance = CapacityStatus.from_json(json)
# print the JSON string representation of the object
print(CapacityStatus.to_json())

# convert the object into a dict
capacity_status_dict = capacity_status_instance.to_dict()
# create an instance of CapacityStatus from a dict
capacity_status_from_dict = CapacityStatus.from_dict(capacity_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


