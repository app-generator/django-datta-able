# ContactDetails

Information about how the Service Point can be contacted

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**phone_number** | **str** | Phone number of the Service Point | [optional] 
**email** | **str** | E-Mail address of the Service Point | [optional] 
**link_uri** | **str** | Link to website of the Service Point | [optional] 
**service_point_id** | **str** | Service Point ID | [optional] 
**html** | **str** | Obsolete. This is planned to be removed in future releases. | [optional] 

## Example

```python
from openapi_client.models.contact_details import ContactDetails

# TODO update the JSON string below
json = "{}"
# create an instance of ContactDetails from a JSON string
contact_details_instance = ContactDetails.from_json(json)
# print the JSON string representation of the object
print(ContactDetails.to_json())

# convert the object into a dict
contact_details_dict = contact_details_instance.to_dict()
# create an instance of ContactDetails from a dict
contact_details_from_dict = ContactDetails.from_dict(contact_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


