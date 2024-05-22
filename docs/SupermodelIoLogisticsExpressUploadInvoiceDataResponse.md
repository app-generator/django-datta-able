# SupermodelIoLogisticsExpressUploadInvoiceDataResponse

MyDHL API REST UploadInvoiceData response JSON schema

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**warnings** | **List[str]** |  | [optional] 
**status** | **str** | Status description | [optional] 

## Example

```python
from openapi_client.models.supermodel_io_logistics_express_upload_invoice_data_response import SupermodelIoLogisticsExpressUploadInvoiceDataResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SupermodelIoLogisticsExpressUploadInvoiceDataResponse from a JSON string
supermodel_io_logistics_express_upload_invoice_data_response_instance = SupermodelIoLogisticsExpressUploadInvoiceDataResponse.from_json(json)
# print the JSON string representation of the object
print(SupermodelIoLogisticsExpressUploadInvoiceDataResponse.to_json())

# convert the object into a dict
supermodel_io_logistics_express_upload_invoice_data_response_dict = supermodel_io_logistics_express_upload_invoice_data_response_instance.to_dict()
# create an instance of SupermodelIoLogisticsExpressUploadInvoiceDataResponse from a dict
supermodel_io_logistics_express_upload_invoice_data_response_from_dict = SupermodelIoLogisticsExpressUploadInvoiceDataResponse.from_dict(supermodel_io_logistics_express_upload_invoice_data_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


