# SupermodelIoLogisticsExpressUploadInvoiceDataRequestOutputImagePropertiesImageOptionsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type_code** | **str** | Please enter the document type you want to wish set properties for | 
**template_name** | **str** | Please enter DHL Express document template name. | [optional] 
**is_requested** | **bool** | If set to true then the document is rendered otherwise not | [optional] 

## Example

```python
from openapi_client.models.supermodel_io_logistics_express_upload_invoice_data_request_output_image_properties_image_options_inner import SupermodelIoLogisticsExpressUploadInvoiceDataRequestOutputImagePropertiesImageOptionsInner

# TODO update the JSON string below
json = "{}"
# create an instance of SupermodelIoLogisticsExpressUploadInvoiceDataRequestOutputImagePropertiesImageOptionsInner from a JSON string
supermodel_io_logistics_express_upload_invoice_data_request_output_image_properties_image_options_inner_instance = SupermodelIoLogisticsExpressUploadInvoiceDataRequestOutputImagePropertiesImageOptionsInner.from_json(json)
# print the JSON string representation of the object
print(SupermodelIoLogisticsExpressUploadInvoiceDataRequestOutputImagePropertiesImageOptionsInner.to_json())

# convert the object into a dict
supermodel_io_logistics_express_upload_invoice_data_request_output_image_properties_image_options_inner_dict = supermodel_io_logistics_express_upload_invoice_data_request_output_image_properties_image_options_inner_instance.to_dict()
# create an instance of SupermodelIoLogisticsExpressUploadInvoiceDataRequestOutputImagePropertiesImageOptionsInner from a dict
supermodel_io_logistics_express_upload_invoice_data_request_output_image_properties_image_options_inner_from_dict = SupermodelIoLogisticsExpressUploadInvoiceDataRequestOutputImagePropertiesImageOptionsInner.from_dict(supermodel_io_logistics_express_upload_invoice_data_request_output_image_properties_image_options_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


