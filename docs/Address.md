# Address

Sub-entity holding the facility address

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address_line1** | **str** | First line of the facility address | [optional] 
**address_line2** | **str** | Second line of the facility address (only present if field is filled in GREF database) | [optional] 
**address_line3** | **str** | Third line of the facility address (only present if field is filled in GREF database) | [optional] 
**street** | **str** | Street details in facility address | [optional] 
**house_number** | **str** | House number in facility address | [optional] 
**additional_info** | **str** | Additional details in facility address | [optional] 
**city** | **str** | Facility city | [optional] 
**zip_code** | **str** | Zip code of the facility | [optional] 
**state** | **str** | State | [optional] 
**country** | **str** | Country | [optional] 
**dhl_country** | **str** | DHL country | [optional] 
**country_division_code** | **str** | Country Division Code | [optional] 
**country_division_code_type** | **str** | Enumeration (State, Province) | [optional] 
**html** | **str** | Obsolete. This is planned to be removed in future releases. | [optional] 

## Example

```python
from openapi_client.models.address import Address

# TODO update the JSON string below
json = "{}"
# create an instance of Address from a JSON string
address_instance = Address.from_json(json)
# print the JSON string representation of the object
print(Address.to_json())

# convert the object into a dict
address_dict = address_instance.to_dict()
# create an instance of Address from a dict
address_from_dict = Address.from_dict(address_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


