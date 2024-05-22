# ProductsInner1TotalPriceInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**currency_type** | **str** | Possible Values :&lt;BR&gt;                  &#39;BILLC&#39;, billing currency&lt;BR&gt;                  &#39;PULCL&#39;, country public rates currency&lt;BR&gt;                  &#39;BASEC&#39;, base currency | [optional] 
**price_currency** | **str** | This the currency of the rated shipment for the prices listed. | [optional] 
**price** | **float** | This is the total price of the rated shipment for the product listed. | 

## Example

```python
from openapi_client.models.products_inner1_total_price_inner import ProductsInner1TotalPriceInner

# TODO update the JSON string below
json = "{}"
# create an instance of ProductsInner1TotalPriceInner from a JSON string
products_inner1_total_price_inner_instance = ProductsInner1TotalPriceInner.from_json(json)
# print the JSON string representation of the object
print(ProductsInner1TotalPriceInner.to_json())

# convert the object into a dict
products_inner1_total_price_inner_dict = products_inner1_total_price_inner_instance.to_dict()
# create an instance of ProductsInner1TotalPriceInner from a dict
products_inner1_total_price_inner_from_dict = ProductsInner1TotalPriceInner.from_dict(products_inner1_total_price_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


