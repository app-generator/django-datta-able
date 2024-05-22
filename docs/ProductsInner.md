# ProductsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**product_name** | **str** | Name of the DHL Express product | [optional] 
**product_code** | **str** | This is the global DHL Express product code for which the delivery is feasible respecting the input data from the request. | [optional] 
**local_product_code** | **str** | This is the local DHL Express product code for which the delivery is feasible respecting the input data from the request. | [optional] 
**local_product_country_code** | **str** | The country code for the local service used | [optional] 
**network_type_code** | **str** | The NetworkTypeCode element indicates the product belongs to the Day Definite (DD) or Time Definite (TD) network.&lt;BR&gt;            Possible Values;&lt;BR&gt;            DD: Day Definite product&lt;BR&gt;            TD: Time Definite product | [optional] 
**is_customer_agreement** | **bool** | Indicator that the product only can be offered to customers with prior agreement. | [optional] 
**weight** | [**Weight**](Weight.md) |  | [optional] 
**breakdown** | [**List[ProductsInnerBreakdownInner]**](ProductsInnerBreakdownInner.md) |  | [optional] 
**service_code_mutually_exclusive_groups** | [**List[ProductsInnerServiceCodeMutuallyExclusiveGroupsInner]**](ProductsInnerServiceCodeMutuallyExclusiveGroupsInner.md) | Group of serviceCodes that are mutually exclusive.  Only one serviceCode among the list must be applied for a shipment | [optional] 
**service_code_dependency_rule_groups** | [**List[ProductsInnerServiceCodeDependencyRuleGroupsInner]**](ProductsInnerServiceCodeDependencyRuleGroupsInner.md) | Dependency rule groups for a particular serviceCode. | [optional] 
**pickup_capabilities** | [**ProductsInnerPickupCapabilities**](ProductsInnerPickupCapabilities.md) |  | [optional] 
**delivery_capabilities** | [**ProductsInnerDeliveryCapabilities**](ProductsInnerDeliveryCapabilities.md) |  | [optional] 

## Example

```python
from openapi_client.models.products_inner import ProductsInner

# TODO update the JSON string below
json = "{}"
# create an instance of ProductsInner from a JSON string
products_inner_instance = ProductsInner.from_json(json)
# print the JSON string representation of the object
print(ProductsInner.to_json())

# convert the object into a dict
products_inner_dict = products_inner_instance.to_dict()
# create an instance of ProductsInner from a dict
products_inner_from_dict = ProductsInner.from_dict(products_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


