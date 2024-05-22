# Partner

Partner information (when SVP type is PRT)

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**partner_id** | **str** | ID of a partner | [optional] 
**partner_name** | **str** | Name of a partner | [optional] 
**partner_type_code** | **str** | Code of a partner | [optional] 
**promotion** | [**Promotion**](Promotion.md) |  | [optional] 

## Example

```python
from openapi_client.models.partner import Partner

# TODO update the JSON string below
json = "{}"
# create an instance of Partner from a JSON string
partner_instance = Partner.from_json(json)
# print the JSON string representation of the object
print(Partner.to_json())

# convert the object into a dict
partner_dict = partner_instance.to_dict()
# create an instance of Partner from a dict
partner_from_dict = Partner.from_dict(partner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


