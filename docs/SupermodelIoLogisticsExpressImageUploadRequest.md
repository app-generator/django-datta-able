# SupermodelIoLogisticsExpressImageUploadRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**original_planned_shipping_date** | **str** |  | 
**accounts** | [**List[SupermodelIoLogisticsExpressAccount]**](SupermodelIoLogisticsExpressAccount.md) | Please enter all the DHL Express accounts and types to be used for this shipment | 
**product_code** | **str** | Please enter DHL Express Global Product code | 
**document_images** | [**List[SupermodelIoLogisticsExpressDocumentImagesInner]**](SupermodelIoLogisticsExpressDocumentImagesInner.md) | This section is to support multiple base64 encoded string with the image of export documentation for Paperless Trade images. When an invalid base64 encoded string is provided, an error message will be returned | 

## Example

```python
from openapi_client.models.supermodel_io_logistics_express_image_upload_request import SupermodelIoLogisticsExpressImageUploadRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SupermodelIoLogisticsExpressImageUploadRequest from a JSON string
supermodel_io_logistics_express_image_upload_request_instance = SupermodelIoLogisticsExpressImageUploadRequest.from_json(json)
# print the JSON string representation of the object
print(SupermodelIoLogisticsExpressImageUploadRequest.to_json())

# convert the object into a dict
supermodel_io_logistics_express_image_upload_request_dict = supermodel_io_logistics_express_image_upload_request_instance.to_dict()
# create an instance of SupermodelIoLogisticsExpressImageUploadRequest from a dict
supermodel_io_logistics_express_image_upload_request_from_dict = SupermodelIoLogisticsExpressImageUploadRequest.from_dict(supermodel_io_logistics_express_image_upload_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


