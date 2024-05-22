# ProductsInnerServiceCodeDependencyRuleGroupsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dependent_service_code** | **str** | Dependent special service charge code where the rule groups are applied | [optional] 
**dependency_rule_group** | [**List[ProductsInnerServiceCodeDependencyRuleGroupsInnerDependencyRuleGroupInner]**](ProductsInnerServiceCodeDependencyRuleGroupsInnerDependencyRuleGroupInner.md) |  | [optional] 

## Example

```python
from openapi_client.models.products_inner_service_code_dependency_rule_groups_inner import ProductsInnerServiceCodeDependencyRuleGroupsInner

# TODO update the JSON string below
json = "{}"
# create an instance of ProductsInnerServiceCodeDependencyRuleGroupsInner from a JSON string
products_inner_service_code_dependency_rule_groups_inner_instance = ProductsInnerServiceCodeDependencyRuleGroupsInner.from_json(json)
# print the JSON string representation of the object
print(ProductsInnerServiceCodeDependencyRuleGroupsInner.to_json())

# convert the object into a dict
products_inner_service_code_dependency_rule_groups_inner_dict = products_inner_service_code_dependency_rule_groups_inner_instance.to_dict()
# create an instance of ProductsInnerServiceCodeDependencyRuleGroupsInner from a dict
products_inner_service_code_dependency_rule_groups_inner_from_dict = ProductsInnerServiceCodeDependencyRuleGroupsInner.from_dict(products_inner_service_code_dependency_rule_groups_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


