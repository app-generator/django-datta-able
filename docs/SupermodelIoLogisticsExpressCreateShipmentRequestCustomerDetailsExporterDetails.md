# SupermodelIoLogisticsExpressCreateShipmentRequestCustomerDetailsExporterDetails

Please enter address and contact details related to exporter

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**postal_address** | [**SupermodelIoLogisticsExpressAddressCreateShipmentRequest**](SupermodelIoLogisticsExpressAddressCreateShipmentRequest.md) |  | 
**contact_information** | [**SupermodelIoLogisticsExpressContact**](SupermodelIoLogisticsExpressContact.md) |  | 
**registration_numbers** | [**List[SupermodelIoLogisticsExpressRegistrationNumbers]**](SupermodelIoLogisticsExpressRegistrationNumbers.md) |  | [optional] 
**bank_details** | [**List[SupermodelIoLogisticsExpressBankDetailsInner]**](SupermodelIoLogisticsExpressBankDetailsInner.md) |  | [optional] 
**type_code** | **str** | Please enter the business party type of the exporter | [optional] 

## Example

```python
from openapi_client.models.supermodel_io_logistics_express_create_shipment_request_customer_details_exporter_details import SupermodelIoLogisticsExpressCreateShipmentRequestCustomerDetailsExporterDetails

# TODO update the JSON string below
json = "{}"
# create an instance of SupermodelIoLogisticsExpressCreateShipmentRequestCustomerDetailsExporterDetails from a JSON string
supermodel_io_logistics_express_create_shipment_request_customer_details_exporter_details_instance = SupermodelIoLogisticsExpressCreateShipmentRequestCustomerDetailsExporterDetails.from_json(json)
# print the JSON string representation of the object
print(SupermodelIoLogisticsExpressCreateShipmentRequestCustomerDetailsExporterDetails.to_json())

# convert the object into a dict
supermodel_io_logistics_express_create_shipment_request_customer_details_exporter_details_dict = supermodel_io_logistics_express_create_shipment_request_customer_details_exporter_details_instance.to_dict()
# create an instance of SupermodelIoLogisticsExpressCreateShipmentRequestCustomerDetailsExporterDetails from a dict
supermodel_io_logistics_express_create_shipment_request_customer_details_exporter_details_from_dict = SupermodelIoLogisticsExpressCreateShipmentRequestCustomerDetailsExporterDetails.from_dict(supermodel_io_logistics_express_create_shipment_request_customer_details_exporter_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


