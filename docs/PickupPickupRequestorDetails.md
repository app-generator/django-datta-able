# PickupPickupRequestorDetails

Please enter address and contact details of the individual requesting the pickup

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**postal_address** | [**SupermodelIoLogisticsExpressAddressCreateShipmentRequest**](SupermodelIoLogisticsExpressAddressCreateShipmentRequest.md) |  | 
**contact_information** | [**SupermodelIoLogisticsExpressContact**](SupermodelIoLogisticsExpressContact.md) |  | 
**registration_numbers** | [**List[SupermodelIoLogisticsExpressRegistrationNumbers]**](SupermodelIoLogisticsExpressRegistrationNumbers.md) |  | [optional] 
**bank_details** | [**List[SupermodelIoLogisticsExpressBankDetailsInner]**](SupermodelIoLogisticsExpressBankDetailsInner.md) |  | [optional] 
**type_code** | **str** | Please enter the business party type of the pickup requestor. | [optional] 

## Example

```python
from openapi_client.models.pickup_pickup_requestor_details import PickupPickupRequestorDetails

# TODO update the JSON string below
json = "{}"
# create an instance of PickupPickupRequestorDetails from a JSON string
pickup_pickup_requestor_details_instance = PickupPickupRequestorDetails.from_json(json)
# print the JSON string representation of the object
print(PickupPickupRequestorDetails.to_json())

# convert the object into a dict
pickup_pickup_requestor_details_dict = pickup_pickup_requestor_details_instance.to_dict()
# create an instance of PickupPickupRequestorDetails from a dict
pickup_pickup_requestor_details_from_dict = PickupPickupRequestorDetails.from_dict(pickup_pickup_requestor_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


