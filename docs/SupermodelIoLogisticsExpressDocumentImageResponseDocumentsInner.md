# SupermodelIoLogisticsExpressDocumentImageResponseDocumentsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**shipment_tracking_number** | **str** | Shipment Tracking Number | 
**type_code** | **str** | Identifies type of the document like commercial invoice or waybill, or archived zip documents | 
**function** | **str** | Clearance code or document function whether for import, export or both.  Returned only for customs-entry | [optional] 
**encoding_format** | **str** | Identifies image format the document is created in, like PDF, TIFF, or ZIP | 
**content** | **str** | Contains base64 encoded document image or archived zip | 

## Example

```python
from openapi_client.models.supermodel_io_logistics_express_document_image_response_documents_inner import SupermodelIoLogisticsExpressDocumentImageResponseDocumentsInner

# TODO update the JSON string below
json = "{}"
# create an instance of SupermodelIoLogisticsExpressDocumentImageResponseDocumentsInner from a JSON string
supermodel_io_logistics_express_document_image_response_documents_inner_instance = SupermodelIoLogisticsExpressDocumentImageResponseDocumentsInner.from_json(json)
# print the JSON string representation of the object
print(SupermodelIoLogisticsExpressDocumentImageResponseDocumentsInner.to_json())

# convert the object into a dict
supermodel_io_logistics_express_document_image_response_documents_inner_dict = supermodel_io_logistics_express_document_image_response_documents_inner_instance.to_dict()
# create an instance of SupermodelIoLogisticsExpressDocumentImageResponseDocumentsInner from a dict
supermodel_io_logistics_express_document_image_response_documents_inner_from_dict = SupermodelIoLogisticsExpressDocumentImageResponseDocumentsInner.from_dict(supermodel_io_logistics_express_document_image_response_documents_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


