# SupermodelIoLogisticsExpressUploadInvoiceDataRequestContent

Here you can define all the properties related to the content of the prospected shipment

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**export_declaration** | [**List[SupermodelIoLogisticsExpressExportDeclaration]**](SupermodelIoLogisticsExpressExportDeclaration.md) | Here you can find all details related to export declaration | 
**currency** | **str** | For customs purposes please advise on currency code of the indicated amount in invoice. | 
**unit_of_measurement** | **str** | Please enter Unit of measurement - metric,imperial | 

## Example

```python
from openapi_client.models.supermodel_io_logistics_express_upload_invoice_data_request_content import SupermodelIoLogisticsExpressUploadInvoiceDataRequestContent

# TODO update the JSON string below
json = "{}"
# create an instance of SupermodelIoLogisticsExpressUploadInvoiceDataRequestContent from a JSON string
supermodel_io_logistics_express_upload_invoice_data_request_content_instance = SupermodelIoLogisticsExpressUploadInvoiceDataRequestContent.from_json(json)
# print the JSON string representation of the object
print(SupermodelIoLogisticsExpressUploadInvoiceDataRequestContent.to_json())

# convert the object into a dict
supermodel_io_logistics_express_upload_invoice_data_request_content_dict = supermodel_io_logistics_express_upload_invoice_data_request_content_instance.to_dict()
# create an instance of SupermodelIoLogisticsExpressUploadInvoiceDataRequestContent from a dict
supermodel_io_logistics_express_upload_invoice_data_request_content_from_dict = SupermodelIoLogisticsExpressUploadInvoiceDataRequestContent.from_dict(supermodel_io_logistics_express_upload_invoice_data_request_content_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


