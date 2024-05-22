# SupermodelIoLogisticsExpressCreateShipmentRequestCustomerDetailsBuyerDetails

Please enter address and contact details related to buyer

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**postal_address** | [**SupermodelIoLogisticsExpressAddressCreateShipmentRequest**](SupermodelIoLogisticsExpressAddressCreateShipmentRequest.md) |  | 
**contact_information** | [**SupermodelIoLogisticsExpressContactBuyer**](SupermodelIoLogisticsExpressContactBuyer.md) |  | 
**registration_numbers** | [**List[SupermodelIoLogisticsExpressRegistrationNumbers]**](SupermodelIoLogisticsExpressRegistrationNumbers.md) |  | [optional] 
**bank_details** | [**List[SupermodelIoLogisticsExpressBankDetailsInner]**](SupermodelIoLogisticsExpressBankDetailsInner.md) |  | [optional] 
**type_code** | **str** | Please enter the business party type of the buyer | [optional] 

## Example

```python
from openapi_client.models.supermodel_io_logistics_express_create_shipment_request_customer_details_buyer_details import SupermodelIoLogisticsExpressCreateShipmentRequestCustomerDetailsBuyerDetails

# TODO update the JSON string below
json = "{}"
# create an instance of SupermodelIoLogisticsExpressCreateShipmentRequestCustomerDetailsBuyerDetails from a JSON string
supermodel_io_logistics_express_create_shipment_request_customer_details_buyer_details_instance = SupermodelIoLogisticsExpressCreateShipmentRequestCustomerDetailsBuyerDetails.from_json(json)
# print the JSON string representation of the object
print(SupermodelIoLogisticsExpressCreateShipmentRequestCustomerDetailsBuyerDetails.to_json())

# convert the object into a dict
supermodel_io_logistics_express_create_shipment_request_customer_details_buyer_details_dict = supermodel_io_logistics_express_create_shipment_request_customer_details_buyer_details_instance.to_dict()
# create an instance of SupermodelIoLogisticsExpressCreateShipmentRequestCustomerDetailsBuyerDetails from a dict
supermodel_io_logistics_express_create_shipment_request_customer_details_buyer_details_from_dict = SupermodelIoLogisticsExpressCreateShipmentRequestCustomerDetailsBuyerDetails.from_dict(supermodel_io_logistics_express_create_shipment_request_customer_details_buyer_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


