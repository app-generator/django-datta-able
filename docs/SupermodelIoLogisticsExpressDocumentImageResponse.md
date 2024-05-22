# SupermodelIoLogisticsExpressDocumentImageResponse

MyDHL API REST document image response schema

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**documents** | [**List[SupermodelIoLogisticsExpressDocumentImageResponseDocumentsInner]**](SupermodelIoLogisticsExpressDocumentImageResponseDocumentsInner.md) | Here you can find all document images from search query | [optional] 

## Example

```python
from openapi_client.models.supermodel_io_logistics_express_document_image_response import SupermodelIoLogisticsExpressDocumentImageResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SupermodelIoLogisticsExpressDocumentImageResponse from a JSON string
supermodel_io_logistics_express_document_image_response_instance = SupermodelIoLogisticsExpressDocumentImageResponse.from_json(json)
# print the JSON string representation of the object
print(SupermodelIoLogisticsExpressDocumentImageResponse.to_json())

# convert the object into a dict
supermodel_io_logistics_express_document_image_response_dict = supermodel_io_logistics_express_document_image_response_instance.to_dict()
# create an instance of SupermodelIoLogisticsExpressDocumentImageResponse from a dict
supermodel_io_logistics_express_document_image_response_from_dict = SupermodelIoLogisticsExpressDocumentImageResponse.from_dict(supermodel_io_logistics_express_document_image_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


