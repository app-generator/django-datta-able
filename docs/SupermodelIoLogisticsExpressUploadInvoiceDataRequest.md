# SupermodelIoLogisticsExpressUploadInvoiceDataRequest

MyDHL API REST UploadInvoiceData request JSON Schema

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**planned_ship_date** | **str** | The planned shipment date for the provided shipmentTrackingNumber.  The date must be in the format: YYYY-MM-DD | [optional] 
**accounts** | [**List[SupermodelIoLogisticsExpressAccount]**](SupermodelIoLogisticsExpressAccount.md) | Please enter all the DHL Express accounts and types to be used for this shipment.   Note: accounts/0/number with typeCode &#39;shipper&#39; is mandatory if using POST method and no shipmentTrackingNumber is provided in request. | [optional] 
**content** | [**SupermodelIoLogisticsExpressUploadInvoiceDataRequestContent**](SupermodelIoLogisticsExpressUploadInvoiceDataRequestContent.md) |  | 
**output_image_properties** | [**SupermodelIoLogisticsExpressUploadInvoiceDataRequestOutputImageProperties**](SupermodelIoLogisticsExpressUploadInvoiceDataRequestOutputImageProperties.md) |  | [optional] 
**customer_details** | [**SupermodelIoLogisticsExpressUploadInvoiceDataRequestCustomerDetails**](SupermodelIoLogisticsExpressUploadInvoiceDataRequestCustomerDetails.md) |  | [optional] 

## Example

```python
from openapi_client.models.supermodel_io_logistics_express_upload_invoice_data_request import SupermodelIoLogisticsExpressUploadInvoiceDataRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SupermodelIoLogisticsExpressUploadInvoiceDataRequest from a JSON string
supermodel_io_logistics_express_upload_invoice_data_request_instance = SupermodelIoLogisticsExpressUploadInvoiceDataRequest.from_json(json)
# print the JSON string representation of the object
print(SupermodelIoLogisticsExpressUploadInvoiceDataRequest.to_json())

# convert the object into a dict
supermodel_io_logistics_express_upload_invoice_data_request_dict = supermodel_io_logistics_express_upload_invoice_data_request_instance.to_dict()
# create an instance of SupermodelIoLogisticsExpressUploadInvoiceDataRequest from a dict
supermodel_io_logistics_express_upload_invoice_data_request_from_dict = SupermodelIoLogisticsExpressUploadInvoiceDataRequest.from_dict(supermodel_io_logistics_express_upload_invoice_data_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


