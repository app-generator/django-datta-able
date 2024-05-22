# SupermodelIoLogisticsExpressCreateShipmentRequestCustomerDetails

Here you need to define all the parties needed to ship the package

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**shipper_details** | [**SupermodelIoLogisticsExpressCreateShipmentRequestCustomerDetailsShipperDetails**](SupermodelIoLogisticsExpressCreateShipmentRequestCustomerDetailsShipperDetails.md) |  | 
**receiver_details** | [**SupermodelIoLogisticsExpressCreateShipmentRequestCustomerDetailsReceiverDetails**](SupermodelIoLogisticsExpressCreateShipmentRequestCustomerDetailsReceiverDetails.md) |  | 
**buyer_details** | [**SupermodelIoLogisticsExpressCreateShipmentRequestCustomerDetailsBuyerDetails**](SupermodelIoLogisticsExpressCreateShipmentRequestCustomerDetailsBuyerDetails.md) |  | [optional] 
**importer_details** | [**SupermodelIoLogisticsExpressCreateShipmentRequestCustomerDetailsImporterDetails**](SupermodelIoLogisticsExpressCreateShipmentRequestCustomerDetailsImporterDetails.md) |  | [optional] 
**exporter_details** | [**SupermodelIoLogisticsExpressCreateShipmentRequestCustomerDetailsExporterDetails**](SupermodelIoLogisticsExpressCreateShipmentRequestCustomerDetailsExporterDetails.md) |  | [optional] 
**seller_details** | [**SupermodelIoLogisticsExpressCreateShipmentRequestCustomerDetailsSellerDetails**](SupermodelIoLogisticsExpressCreateShipmentRequestCustomerDetailsSellerDetails.md) |  | [optional] 
**payer_details** | [**SupermodelIoLogisticsExpressCreateShipmentRequestCustomerDetailsPayerDetails**](SupermodelIoLogisticsExpressCreateShipmentRequestCustomerDetailsPayerDetails.md) |  | [optional] 
**ultimate_consignee_details** | [**SupermodelIoLogisticsExpressCreateShipmentRequestCustomerDetailsUltimateConsigneeDetails**](SupermodelIoLogisticsExpressCreateShipmentRequestCustomerDetailsUltimateConsigneeDetails.md) |  | [optional] 
**broker_details** | [**SupermodelIoLogisticsExpressCreateShipmentRequestCustomerDetailsBrokerDetails**](SupermodelIoLogisticsExpressCreateShipmentRequestCustomerDetailsBrokerDetails.md) |  | [optional] 

## Example

```python
from openapi_client.models.supermodel_io_logistics_express_create_shipment_request_customer_details import SupermodelIoLogisticsExpressCreateShipmentRequestCustomerDetails

# TODO update the JSON string below
json = "{}"
# create an instance of SupermodelIoLogisticsExpressCreateShipmentRequestCustomerDetails from a JSON string
supermodel_io_logistics_express_create_shipment_request_customer_details_instance = SupermodelIoLogisticsExpressCreateShipmentRequestCustomerDetails.from_json(json)
# print the JSON string representation of the object
print(SupermodelIoLogisticsExpressCreateShipmentRequestCustomerDetails.to_json())

# convert the object into a dict
supermodel_io_logistics_express_create_shipment_request_customer_details_dict = supermodel_io_logistics_express_create_shipment_request_customer_details_instance.to_dict()
# create an instance of SupermodelIoLogisticsExpressCreateShipmentRequestCustomerDetails from a dict
supermodel_io_logistics_express_create_shipment_request_customer_details_from_dict = SupermodelIoLogisticsExpressCreateShipmentRequestCustomerDetails.from_dict(supermodel_io_logistics_express_create_shipment_request_customer_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


