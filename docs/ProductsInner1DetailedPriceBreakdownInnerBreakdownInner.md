# ProductsInner1DetailedPriceBreakdownInnerBreakdownInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | When landed-cost is requested then following items name (Charge Types) might be returned: &lt;BR&gt;                        Charge Type : Description &lt;BR&gt;                        STDIS : Quoted shipment total discount &lt;BR&gt;                        SCUSV : Shipment Customs value &lt;BR&gt;                        SINSV : Insured value &lt;BR&gt;                        SPRQD : Shipment product quote discount&lt;BR&gt;                        SPRQN : The price quoted to the Customer by DHL at the time of the booking. This quote covers the weight price including discounts and without taxes. &lt;BR&gt;                        STSCH : The total of service charges quoted to customer for DHL Express value added services, the amount is after discounts and doesn&#39;t include tax amounts. &lt;BR&gt;                        MACHG : The total of service charges as provided by Merchant for the purpose of landed cost calculation. &lt;BR&gt;                        MFCHG : The freight charge as provided by Merchant for the purpose of landed cost calculation. | [optional] 
**service_code** | **str** | Special service or extra charge code. This is the code you would have to use in the /shipment service if you wish to add an optional Service such as Saturday delivery | [optional] 
**local_service_code** | **str** | Local service code | [optional] 
**type_code** | **str** | Price breakdown type code | [optional] 
**service_type_code** | **str** | Special service charge code type for service. | [optional] 
**price** | **float** | Price breakdown value | [optional] 
**price_currency** | **str** | This the currency of the rated shipment for the prices listed. | [optional] 
**is_customer_agreement** | **bool** | Customer agreement indicator for product and services, if service is offered with prior customer agreement | [optional] 
**is_marketed_service** | **bool** | Indicator if the special service is marketed service | [optional] 
**is_billing_service_indicator** | **bool** | Indicator if there is any discount allowed | [optional] 
**price_breakdown** | [**List[PriceDetailInner]**](PriceDetailInner.md) |  | [optional] 
**tariff_rate_formula** | **str** | Tariff Rate Formula on Shipment Level | [optional] 

## Example

```python
from openapi_client.models.products_inner1_detailed_price_breakdown_inner_breakdown_inner import ProductsInner1DetailedPriceBreakdownInnerBreakdownInner

# TODO update the JSON string below
json = "{}"
# create an instance of ProductsInner1DetailedPriceBreakdownInnerBreakdownInner from a JSON string
products_inner1_detailed_price_breakdown_inner_breakdown_inner_instance = ProductsInner1DetailedPriceBreakdownInnerBreakdownInner.from_json(json)
# print the JSON string representation of the object
print(ProductsInner1DetailedPriceBreakdownInnerBreakdownInner.to_json())

# convert the object into a dict
products_inner1_detailed_price_breakdown_inner_breakdown_inner_dict = products_inner1_detailed_price_breakdown_inner_breakdown_inner_instance.to_dict()
# create an instance of ProductsInner1DetailedPriceBreakdownInnerBreakdownInner from a dict
products_inner1_detailed_price_breakdown_inner_breakdown_inner_from_dict = ProductsInner1DetailedPriceBreakdownInnerBreakdownInner.from_dict(products_inner1_detailed_price_breakdown_inner_breakdown_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


