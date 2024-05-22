# Pickup


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_requested** | **bool** | Please advise if a pickup is needed for this shipment | [default to False]
**close_time** | **str** | The latest time the location premises is available to dispatch the DHL Express shipment. (HH:MM)  | [optional] 
**location** | **str** | Provides information on where the package should be picked up by DHL courier. | [optional] 
**special_instructions** | [**List[PickupSpecialInstructionsInner]**](PickupSpecialInstructionsInner.md) | Details special pickup instructions you may wish to send to the DHL Courier. | [optional] 
**pickup_details** | [**PickupPickupDetails**](PickupPickupDetails.md) |  | [optional] 
**pickup_requestor_details** | [**PickupPickupRequestorDetails**](PickupPickupRequestorDetails.md) |  | [optional] 

## Example

```python
from openapi_client.models.pickup import Pickup

# TODO update the JSON string below
json = "{}"
# create an instance of Pickup from a JSON string
pickup_instance = Pickup.from_json(json)
# print the JSON string representation of the object
print(Pickup.to_json())

# convert the object into a dict
pickup_dict = pickup_instance.to_dict()
# create an instance of Pickup from a dict
pickup_from_dict = Pickup.from_dict(pickup_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


