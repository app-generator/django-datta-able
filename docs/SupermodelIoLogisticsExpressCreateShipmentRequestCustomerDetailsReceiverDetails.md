# SupermodelIoLogisticsExpressCreateShipmentRequestCustomerDetailsReceiverDetails

Please enter address and contact details related to receiver

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**postal_address** | [**SupermodelIoLogisticsExpressAddressCreateShipmentRequest**](SupermodelIoLogisticsExpressAddressCreateShipmentRequest.md) |  | 
**contact_information** | [**SupermodelIoLogisticsExpressContact**](SupermodelIoLogisticsExpressContact.md) |  | 
**registration_numbers** | [**List[SupermodelIoLogisticsExpressRegistrationNumbers]**](SupermodelIoLogisticsExpressRegistrationNumbers.md) |  | [optional] 
**bank_details** | [**List[SupermodelIoLogisticsExpressBankDetailsInner]**](SupermodelIoLogisticsExpressBankDetailsInner.md) |  | [optional] 
**type_code** | **str** | Please enter the business party type of the receiver | [optional] 

## Example

```python
from openapi_client.models.supermodel_io_logistics_express_create_shipment_request_customer_details_receiver_details import SupermodelIoLogisticsExpressCreateShipmentRequestCustomerDetailsReceiverDetails

# TODO update the JSON string below
json = "{}"
# create an instance of SupermodelIoLogisticsExpressCreateShipmentRequestCustomerDetailsReceiverDetails from a JSON string
supermodel_io_logistics_express_create_shipment_request_customer_details_receiver_details_instance = SupermodelIoLogisticsExpressCreateShipmentRequestCustomerDetailsReceiverDetails.from_json(json)
# print the JSON string representation of the object
print(SupermodelIoLogisticsExpressCreateShipmentRequestCustomerDetailsReceiverDetails.to_json())

# convert the object into a dict
supermodel_io_logistics_express_create_shipment_request_customer_details_receiver_details_dict = supermodel_io_logistics_express_create_shipment_request_customer_details_receiver_details_instance.to_dict()
# create an instance of SupermodelIoLogisticsExpressCreateShipmentRequestCustomerDetailsReceiverDetails from a dict
supermodel_io_logistics_express_create_shipment_request_customer_details_receiver_details_from_dict = SupermodelIoLogisticsExpressCreateShipmentRequestCustomerDetailsReceiverDetails.from_dict(supermodel_io_logistics_express_create_shipment_request_customer_details_receiver_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


