# SupermodelIoLogisticsExpressCreateShipmentRequestCustomerDetailsBrokerDetails

Please enter address and contact details related to broker

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**postal_address** | [**SupermodelIoLogisticsExpressAddressCreateShipmentRequest**](SupermodelIoLogisticsExpressAddressCreateShipmentRequest.md) |  | 
**contact_information** | [**SupermodelIoLogisticsExpressContact**](SupermodelIoLogisticsExpressContact.md) |  | 
**registration_numbers** | [**List[SupermodelIoLogisticsExpressRegistrationNumbers]**](SupermodelIoLogisticsExpressRegistrationNumbers.md) |  | [optional] 
**bank_details** | [**SupermodelIoLogisticsExpressRegistrationNumbers**](SupermodelIoLogisticsExpressRegistrationNumbers.md) |  | [optional] 
**type_code** | **str** | Please enter the business party role type of the broker | [optional] 

## Example

```python
from openapi_client.models.supermodel_io_logistics_express_create_shipment_request_customer_details_broker_details import SupermodelIoLogisticsExpressCreateShipmentRequestCustomerDetailsBrokerDetails

# TODO update the JSON string below
json = "{}"
# create an instance of SupermodelIoLogisticsExpressCreateShipmentRequestCustomerDetailsBrokerDetails from a JSON string
supermodel_io_logistics_express_create_shipment_request_customer_details_broker_details_instance = SupermodelIoLogisticsExpressCreateShipmentRequestCustomerDetailsBrokerDetails.from_json(json)
# print the JSON string representation of the object
print(SupermodelIoLogisticsExpressCreateShipmentRequestCustomerDetailsBrokerDetails.to_json())

# convert the object into a dict
supermodel_io_logistics_express_create_shipment_request_customer_details_broker_details_dict = supermodel_io_logistics_express_create_shipment_request_customer_details_broker_details_instance.to_dict()
# create an instance of SupermodelIoLogisticsExpressCreateShipmentRequestCustomerDetailsBrokerDetails from a dict
supermodel_io_logistics_express_create_shipment_request_customer_details_broker_details_from_dict = SupermodelIoLogisticsExpressCreateShipmentRequestCustomerDetailsBrokerDetails.from_dict(supermodel_io_logistics_express_create_shipment_request_customer_details_broker_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


