# ProductsInner1TotalPriceBreakdownInnerPriceBreakdownInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type_code** | **str** | Expected values in Breakdown/Type are below:&lt;BR&gt;                        STTXA:  Total tax for the shipment&lt;BR&gt;                        STDIS: Total discount for the shipment&lt;BR&gt;                        SPRQT: Net shipment / weight charge | 
**price** | **float** | The amount price of DHL product and services | 

## Example

```python
from openapi_client.models.products_inner1_total_price_breakdown_inner_price_breakdown_inner import ProductsInner1TotalPriceBreakdownInnerPriceBreakdownInner

# TODO update the JSON string below
json = "{}"
# create an instance of ProductsInner1TotalPriceBreakdownInnerPriceBreakdownInner from a JSON string
products_inner1_total_price_breakdown_inner_price_breakdown_inner_instance = ProductsInner1TotalPriceBreakdownInnerPriceBreakdownInner.from_json(json)
# print the JSON string representation of the object
print(ProductsInner1TotalPriceBreakdownInnerPriceBreakdownInner.to_json())

# convert the object into a dict
products_inner1_total_price_breakdown_inner_price_breakdown_inner_dict = products_inner1_total_price_breakdown_inner_price_breakdown_inner_instance.to_dict()
# create an instance of ProductsInner1TotalPriceBreakdownInnerPriceBreakdownInner from a dict
products_inner1_total_price_breakdown_inner_price_breakdown_inner_from_dict = ProductsInner1TotalPriceBreakdownInnerPriceBreakdownInner.from_dict(products_inner1_total_price_breakdown_inner_price_breakdown_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


