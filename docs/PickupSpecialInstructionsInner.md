# PickupSpecialInstructionsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | **str** | Any special instructions user wish to send to the courier for the order pick-up. | 
**type_code** | **str** | for future use | [optional] 

## Example

```python
from openapi_client.models.pickup_special_instructions_inner import PickupSpecialInstructionsInner

# TODO update the JSON string below
json = "{}"
# create an instance of PickupSpecialInstructionsInner from a JSON string
pickup_special_instructions_inner_instance = PickupSpecialInstructionsInner.from_json(json)
# print the JSON string representation of the object
print(PickupSpecialInstructionsInner.to_json())

# convert the object into a dict
pickup_special_instructions_inner_dict = pickup_special_instructions_inner_instance.to_dict()
# create an instance of PickupSpecialInstructionsInner from a dict
pickup_special_instructions_inner_from_dict = PickupSpecialInstructionsInner.from_dict(pickup_special_instructions_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


