# Suggestion

Suggestion for the search address

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**label** | **str** | Always holds null value | [optional] 
**value** | **str** | Always holds null value | [optional] 
**latitude** | **float** | Latitude of the geocoded search address (used for GREF web service search) | [optional] 
**longitude** | **float** | Longitude of the geocoded search address (used for GREF web service search) | [optional] 
**country_code** | **str** | Country code of the search address | [optional] 
**place_id** | **str** | Place id of the search address | [optional] 
**provider_id** | **str** | Provider id of the search address | [optional] 

## Example

```python
from openapi_client.models.suggestion import Suggestion

# TODO update the JSON string below
json = "{}"
# create an instance of Suggestion from a JSON string
suggestion_instance = Suggestion.from_json(json)
# print the JSON string representation of the object
print(Suggestion.to_json())

# convert the object into a dict
suggestion_dict = suggestion_instance.to_dict()
# create an instance of Suggestion from a dict
suggestion_from_dict = Suggestion.from_dict(suggestion_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


