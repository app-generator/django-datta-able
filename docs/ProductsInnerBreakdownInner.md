# ProductsInnerBreakdownInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Breakdown Name | [optional] 
**service_code** | **str** | Special service or extra charge code.  This is the code you would have to use in the /shipment service if you wish to add an optional Service such as Saturday delivery | [optional] 
**local_service_code** | **str** | Local service code | [optional] 
**type_code** | **str** | Breakdown type code | [optional] 
**service_type_code** | **str** | Special service charge code type for service. | [optional] 
**is_customer_agreement** | **bool** | Customer agreement indicator for product and services, if service is offered with prior customer agreement | [optional] 
**is_marketed_service** | **bool** | Indicator if the special service is marketed service | [optional] 
**is_billing_service_indicator** | **bool** | Indicator if there is any discount allowed | [optional] 

## Example

```python
from openapi_client.models.products_inner_breakdown_inner import ProductsInnerBreakdownInner

# TODO update the JSON string below
json = "{}"
# create an instance of ProductsInnerBreakdownInner from a JSON string
products_inner_breakdown_inner_instance = ProductsInnerBreakdownInner.from_json(json)
# print the JSON string representation of the object
print(ProductsInnerBreakdownInner.to_json())

# convert the object into a dict
products_inner_breakdown_inner_dict = products_inner_breakdown_inner_instance.to_dict()
# create an instance of ProductsInnerBreakdownInner from a dict
products_inner_breakdown_inner_from_dict = ProductsInnerBreakdownInner.from_dict(products_inner_breakdown_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


