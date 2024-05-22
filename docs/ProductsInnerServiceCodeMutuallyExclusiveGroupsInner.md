# ProductsInnerServiceCodeMutuallyExclusiveGroupsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**service_code_rule_name** | **str** | Mutually exclusive serviceCode group name | [optional] 
**description** | **str** | Mutually exclusive serviceCode group description | [optional] 
**service_codes** | [**List[ProductsInnerServiceCodeMutuallyExclusiveGroupsInnerServiceCodesInner]**](ProductsInnerServiceCodeMutuallyExclusiveGroupsInnerServiceCodesInner.md) |  | [optional] 

## Example

```python
from openapi_client.models.products_inner_service_code_mutually_exclusive_groups_inner import ProductsInnerServiceCodeMutuallyExclusiveGroupsInner

# TODO update the JSON string below
json = "{}"
# create an instance of ProductsInnerServiceCodeMutuallyExclusiveGroupsInner from a JSON string
products_inner_service_code_mutually_exclusive_groups_inner_instance = ProductsInnerServiceCodeMutuallyExclusiveGroupsInner.from_json(json)
# print the JSON string representation of the object
print(ProductsInnerServiceCodeMutuallyExclusiveGroupsInner.to_json())

# convert the object into a dict
products_inner_service_code_mutually_exclusive_groups_inner_dict = products_inner_service_code_mutually_exclusive_groups_inner_instance.to_dict()
# create an instance of ProductsInnerServiceCodeMutuallyExclusiveGroupsInner from a dict
products_inner_service_code_mutually_exclusive_groups_inner_from_dict = ProductsInnerServiceCodeMutuallyExclusiveGroupsInner.from_dict(products_inner_service_code_mutually_exclusive_groups_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


