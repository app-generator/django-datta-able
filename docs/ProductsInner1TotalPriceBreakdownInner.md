# ProductsInner1TotalPriceBreakdownInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**currency_type** | **str** | Possible Values :&lt;BR&gt;                  &#39;BILLC&#39;, billing currency&lt;BR&gt;                  &#39;PULCL&#39;, country public rates currency&lt;BR&gt;                  &#39;BASEC&#39;, base currency | [optional] 
**price_currency** | **str** | This the currency of the rated shipment for the prices listed. | [optional] 
**price_breakdown** | [**List[ProductsInner1TotalPriceBreakdownInnerPriceBreakdownInner]**](ProductsInner1TotalPriceBreakdownInnerPriceBreakdownInner.md) |  | [optional] 

## Example

```python
from openapi_client.models.products_inner1_total_price_breakdown_inner import ProductsInner1TotalPriceBreakdownInner

# TODO update the JSON string below
json = "{}"
# create an instance of ProductsInner1TotalPriceBreakdownInner from a JSON string
products_inner1_total_price_breakdown_inner_instance = ProductsInner1TotalPriceBreakdownInner.from_json(json)
# print the JSON string representation of the object
print(ProductsInner1TotalPriceBreakdownInner.to_json())

# convert the object into a dict
products_inner1_total_price_breakdown_inner_dict = products_inner1_total_price_breakdown_inner_instance.to_dict()
# create an instance of ProductsInner1TotalPriceBreakdownInner from a dict
products_inner1_total_price_breakdown_inner_from_dict = ProductsInner1TotalPriceBreakdownInner.from_dict(products_inner1_total_price_breakdown_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


