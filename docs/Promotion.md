# Promotion

Promotion on a SVP level

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Unique identifier for promotion | 
**country_code** | **str** | Country Code | [optional] 
**partner_type_code** | **str** | Partner Type code | [optional] 
**service_point_id** | **str** | Service Point ID | [optional] 
**client_id** | **str** | Client ID | 
**capability** | **str** | Capability(PPC) | 
**start_date** | **datetime** | Promotion Start date | 
**end_date** | **datetime** | Promotion End date | 
**day_of_week** | **str** | Promotion on specific day of the week | [optional] 
**text** | **str** | Promotion message | 
**button_text** | **str** | Promotion button text | [optional] 
**language_code1** | **str** | Promotion Language Code | [optional] 
**text1** | **str** | Promotion message | [optional] 
**button_text1** | **str** | Promotion button text | [optional] 
**language_code2** | **str** | Promotion Language Code | [optional] 
**text2** | **str** | Promotion message | [optional] 
**button_text2** | **str** | Promotion button text | [optional] 
**language_code3** | **str** | Promotion Language Code | [optional] 
**text3** | **str** | Promotion message | [optional] 
**button_text3** | **str** | Promotion button text | [optional] 
**hyperlink** | **str** | Promotion Web link | [optional] 
**created** | **datetime** | Promotion created date | [optional] 

## Example

```python
from openapi_client.models.promotion import Promotion

# TODO update the JSON string below
json = "{}"
# create an instance of Promotion from a JSON string
promotion_instance = Promotion.from_json(json)
# print the JSON string representation of the object
print(Promotion.to_json())

# convert the object into a dict
promotion_dict = promotion_instance.to_dict()
# create an instance of Promotion from a dict
promotion_from_dict = Promotion.from_dict(promotion_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


