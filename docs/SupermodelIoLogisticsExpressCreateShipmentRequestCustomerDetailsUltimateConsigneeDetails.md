# SupermodelIoLogisticsExpressCreateShipmentRequestCustomerDetailsUltimateConsigneeDetails

Please enter address and contact details related to ultimate consignee

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**postal_address** | [**SupermodelIoLogisticsExpressAddressCreateShipmentRequest**](SupermodelIoLogisticsExpressAddressCreateShipmentRequest.md) |  | 
**contact_information** | [**SupermodelIoLogisticsExpressContact**](SupermodelIoLogisticsExpressContact.md) |  | 
**registration_numbers** | [**List[SupermodelIoLogisticsExpressRegistrationNumbers]**](SupermodelIoLogisticsExpressRegistrationNumbers.md) |  | [optional] 
**bank_details** | [**SupermodelIoLogisticsExpressRegistrationNumbers**](SupermodelIoLogisticsExpressRegistrationNumbers.md) |  | [optional] 
**type_code** | **str** | Please enter the business party role type of the ultimate consignee | [optional] 

## Example

```python
from openapi_client.models.supermodel_io_logistics_express_create_shipment_request_customer_details_ultimate_consignee_details import SupermodelIoLogisticsExpressCreateShipmentRequestCustomerDetailsUltimateConsigneeDetails

# TODO update the JSON string below
json = "{}"
# create an instance of SupermodelIoLogisticsExpressCreateShipmentRequestCustomerDetailsUltimateConsigneeDetails from a JSON string
supermodel_io_logistics_express_create_shipment_request_customer_details_ultimate_consignee_details_instance = SupermodelIoLogisticsExpressCreateShipmentRequestCustomerDetailsUltimateConsigneeDetails.from_json(json)
# print the JSON string representation of the object
print(SupermodelIoLogisticsExpressCreateShipmentRequestCustomerDetailsUltimateConsigneeDetails.to_json())

# convert the object into a dict
supermodel_io_logistics_express_create_shipment_request_customer_details_ultimate_consignee_details_dict = supermodel_io_logistics_express_create_shipment_request_customer_details_ultimate_consignee_details_instance.to_dict()
# create an instance of SupermodelIoLogisticsExpressCreateShipmentRequestCustomerDetailsUltimateConsigneeDetails from a dict
supermodel_io_logistics_express_create_shipment_request_customer_details_ultimate_consignee_details_from_dict = SupermodelIoLogisticsExpressCreateShipmentRequestCustomerDetailsUltimateConsigneeDetails.from_dict(supermodel_io_logistics_express_create_shipment_request_customer_details_ultimate_consignee_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


