# SupermodelIoLogisticsExpressUploadInvoiceDataRequestOutputImageProperties

Here you can set invoice properties

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**image_options** | [**List[SupermodelIoLogisticsExpressUploadInvoiceDataRequestOutputImagePropertiesImageOptionsInner]**](SupermodelIoLogisticsExpressUploadInvoiceDataRequestOutputImagePropertiesImageOptionsInner.md) | Here the image options are defined for label, waybillDoc, invoice, receipt and QRcode | [optional] 

## Example

```python
from openapi_client.models.supermodel_io_logistics_express_upload_invoice_data_request_output_image_properties import SupermodelIoLogisticsExpressUploadInvoiceDataRequestOutputImageProperties

# TODO update the JSON string below
json = "{}"
# create an instance of SupermodelIoLogisticsExpressUploadInvoiceDataRequestOutputImageProperties from a JSON string
supermodel_io_logistics_express_upload_invoice_data_request_output_image_properties_instance = SupermodelIoLogisticsExpressUploadInvoiceDataRequestOutputImageProperties.from_json(json)
# print the JSON string representation of the object
print(SupermodelIoLogisticsExpressUploadInvoiceDataRequestOutputImageProperties.to_json())

# convert the object into a dict
supermodel_io_logistics_express_upload_invoice_data_request_output_image_properties_dict = supermodel_io_logistics_express_upload_invoice_data_request_output_image_properties_instance.to_dict()
# create an instance of SupermodelIoLogisticsExpressUploadInvoiceDataRequestOutputImageProperties from a dict
supermodel_io_logistics_express_upload_invoice_data_request_output_image_properties_from_dict = SupermodelIoLogisticsExpressUploadInvoiceDataRequestOutputImageProperties.from_dict(supermodel_io_logistics_express_upload_invoice_data_request_output_image_properties_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


