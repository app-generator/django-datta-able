# ProductsInnerServiceCodeDependencyRuleGroupsInnerDependencyRuleGroupInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dependency_rule_name** | **str** | Dependency rule group name | [optional] 
**dependency_description** | **str** | Dependency rule group description | [optional] 
**dependency_condition** | **str** | Dependency rule group condition statement | [optional] 
**required_service_codes** | [**List[ProductsInnerServiceCodeDependencyRuleGroupsInnerDependencyRuleGroupInnerRequiredServiceCodesInner]**](ProductsInnerServiceCodeDependencyRuleGroupsInnerDependencyRuleGroupInnerRequiredServiceCodesInner.md) |  | [optional] 

## Example

```python
from openapi_client.models.products_inner_service_code_dependency_rule_groups_inner_dependency_rule_group_inner import ProductsInnerServiceCodeDependencyRuleGroupsInnerDependencyRuleGroupInner

# TODO update the JSON string below
json = "{}"
# create an instance of ProductsInnerServiceCodeDependencyRuleGroupsInnerDependencyRuleGroupInner from a JSON string
products_inner_service_code_dependency_rule_groups_inner_dependency_rule_group_inner_instance = ProductsInnerServiceCodeDependencyRuleGroupsInnerDependencyRuleGroupInner.from_json(json)
# print the JSON string representation of the object
print(ProductsInnerServiceCodeDependencyRuleGroupsInnerDependencyRuleGroupInner.to_json())

# convert the object into a dict
products_inner_service_code_dependency_rule_groups_inner_dependency_rule_group_inner_dict = products_inner_service_code_dependency_rule_groups_inner_dependency_rule_group_inner_instance.to_dict()
# create an instance of ProductsInnerServiceCodeDependencyRuleGroupsInnerDependencyRuleGroupInner from a dict
products_inner_service_code_dependency_rule_groups_inner_dependency_rule_group_inner_from_dict = ProductsInnerServiceCodeDependencyRuleGroupsInnerDependencyRuleGroupInner.from_dict(products_inner_service_code_dependency_rule_groups_inner_dependency_rule_group_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


