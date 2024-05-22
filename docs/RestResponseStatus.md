# RestResponseStatus

Response status

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status_code** | **int** | Status/error code of the response | [optional] 
**status_message** | **str** | Status/error message text of the response | [optional] 
**ok** | **bool** |  | [optional] 
**warning** | **bool** |  | [optional] 
**error_status** | **bool** |  | [optional] 

## Example

```python
from openapi_client.models.rest_response_status import RestResponseStatus

# TODO update the JSON string below
json = "{}"
# create an instance of RestResponseStatus from a JSON string
rest_response_status_instance = RestResponseStatus.from_json(json)
# print the JSON string representation of the object
print(RestResponseStatus.to_json())

# convert the object into a dict
rest_response_status_dict = rest_response_status_instance.to_dict()
# create an instance of RestResponseStatus from a dict
rest_response_status_from_dict = RestResponseStatus.from_dict(rest_response_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


