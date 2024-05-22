# SupermodelIoLogisticsExpressUploadInvoiceDataRequestCustomerDetails

Here you need to define all the parties needed to ship the package

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**seller_details** | [**SupermodelIoLogisticsExpressUploadInvoiceDataRequestCustomerDetailsSellerDetails**](SupermodelIoLogisticsExpressUploadInvoiceDataRequestCustomerDetailsSellerDetails.md) |  | [optional] 
**buyer_details** | [**SupermodelIoLogisticsExpressUploadInvoiceDataRequestCustomerDetailsBuyerDetails**](SupermodelIoLogisticsExpressUploadInvoiceDataRequestCustomerDetailsBuyerDetails.md) |  | [optional] 
**importer_details** | [**SupermodelIoLogisticsExpressUploadInvoiceDataRequestCustomerDetailsImporterDetails**](SupermodelIoLogisticsExpressUploadInvoiceDataRequestCustomerDetailsImporterDetails.md) |  | [optional] 
**exporter_details** | [**SupermodelIoLogisticsExpressUploadInvoiceDataRequestCustomerDetailsExporterDetails**](SupermodelIoLogisticsExpressUploadInvoiceDataRequestCustomerDetailsExporterDetails.md) |  | [optional] 
**ultimate_consignee_details** | [**SupermodelIoLogisticsExpressUploadInvoiceDataRequestCustomerDetailsUltimateConsigneeDetails**](SupermodelIoLogisticsExpressUploadInvoiceDataRequestCustomerDetailsUltimateConsigneeDetails.md) |  | [optional] 
**broker_details** | [**SupermodelIoLogisticsExpressUploadInvoiceDataRequestCustomerDetailsBrokerDetails**](SupermodelIoLogisticsExpressUploadInvoiceDataRequestCustomerDetailsBrokerDetails.md) |  | [optional] 

## Example

```python
from openapi_client.models.supermodel_io_logistics_express_upload_invoice_data_request_customer_details import SupermodelIoLogisticsExpressUploadInvoiceDataRequestCustomerDetails

# TODO update the JSON string below
json = "{}"
# create an instance of SupermodelIoLogisticsExpressUploadInvoiceDataRequestCustomerDetails from a JSON string
supermodel_io_logistics_express_upload_invoice_data_request_customer_details_instance = SupermodelIoLogisticsExpressUploadInvoiceDataRequestCustomerDetails.from_json(json)
# print the JSON string representation of the object
print(SupermodelIoLogisticsExpressUploadInvoiceDataRequestCustomerDetails.to_json())

# convert the object into a dict
supermodel_io_logistics_express_upload_invoice_data_request_customer_details_dict = supermodel_io_logistics_express_upload_invoice_data_request_customer_details_instance.to_dict()
# create an instance of SupermodelIoLogisticsExpressUploadInvoiceDataRequestCustomerDetails from a dict
supermodel_io_logistics_express_upload_invoice_data_request_customer_details_from_dict = SupermodelIoLogisticsExpressUploadInvoiceDataRequestCustomerDetails.from_dict(supermodel_io_logistics_express_upload_invoice_data_request_customer_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


