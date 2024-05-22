# PriceDetailInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**price_type** | **str** | If a breakdown is provided, details can either be; &#39;TAX&#39;,&lt;BR&gt;                              &#39;DISCOUNT&#39; | [optional] 
**type_code** | **str** | Discount or tax type codes as provided by DHL Express. Example values:&lt;BR&gt;                              For discount;&lt;BR&gt;                              P: promotional&lt;BR&gt;                              S: special | [optional] 
**price** | **float** | The actual amount of the discount/tax | [optional] 
**rate** | **float** | Percentage of the discount/tax | [optional] 
**base_price** | **float** | The base amount of the service charge | [optional] 

## Example

```python
from openapi_client.models.price_detail_inner import PriceDetailInner

# TODO update the JSON string below
json = "{}"
# create an instance of PriceDetailInner from a JSON string
price_detail_inner_instance = PriceDetailInner.from_json(json)
# print the JSON string representation of the object
print(PriceDetailInner.to_json())

# convert the object into a dict
price_detail_inner_dict = price_detail_inner_instance.to_dict()
# create an instance of PriceDetailInner from a dict
price_detail_inner_from_dict = PriceDetailInner.from_dict(price_detail_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


