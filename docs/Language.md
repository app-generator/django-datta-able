# Language

Information about language used for search

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**language_code** | **str** | Language Code | [optional] 
**language_script_code** | **str** | Language Script Code | [optional] 
**language_country_code** | **str** | Language Country Code | [optional] 
**language_ok** | **bool** | Language Valid | [optional] 

## Example

```python
from openapi_client.models.language import Language

# TODO update the JSON string below
json = "{}"
# create an instance of Language from a JSON string
language_instance = Language.from_json(json)
# print the JSON string representation of the object
print(Language.to_json())

# convert the object into a dict
language_dict = language_instance.to_dict()
# create an instance of Language from a dict
language_from_dict = Language.from_dict(language_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

