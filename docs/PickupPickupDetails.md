# PickupPickupDetails

Please enter address and contact details related to your pickup

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**postal_address** | [**SupermodelIoLogisticsExpressAddressCreateShipmentRequest**](SupermodelIoLogisticsExpressAddressCreateShipmentRequest.md) |  | 
**contact_information** | [**SupermodelIoLogisticsExpressContact**](SupermodelIoLogisticsExpressContact.md) |  | 
**registration_numbers** | [**List[SupermodelIoLogisticsExpressRegistrationNumbers]**](SupermodelIoLogisticsExpressRegistrationNumbers.md) |  | [optional] 
**bank_details** | [**List[SupermodelIoLogisticsExpressBankDetailsInner]**](SupermodelIoLogisticsExpressBankDetailsInner.md) |  | [optional] 
**type_code** | **str** | Please enter the business party type related to the pickup. | [optional] 

## Example

```python
from openapi_client.models.pickup_pickup_details import PickupPickupDetails

# TODO update the JSON string below
json = "{}"
# create an instance of PickupPickupDetails from a JSON string
pickup_pickup_details_instance = PickupPickupDetails.from_json(json)
# print the JSON string representation of the object
print(PickupPickupDetails.to_json())

# convert the object into a dict
pickup_pickup_details_dict = pickup_pickup_details_instance.to_dict()
# create an instance of PickupPickupDetails from a dict
pickup_pickup_details_from_dict = PickupPickupDetails.from_dict(pickup_pickup_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


