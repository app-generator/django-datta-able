# SupermodelIoLogisticsExpressDocumentImagesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type_code** | **str** | Please provide correct document type you wish to upload&lt;BR&gt;        &lt;BR&gt;        Possible values;&lt;BR&gt;        INV, Invoice&lt;BR&gt;        PNV, Proforma&lt;BR&gt;        COO, Certificate of Origin&lt;BR&gt;        NAF, Nafta Certificate of Origin&lt;BR&gt;        CIN, Commercial Invoice&lt;BR&gt;        DCL, Custom Declaration&lt;BR&gt;        AWB, Air Waybill and Waybill Document | [optional] [default to 'INV']
**image_format** | **str** | Please provide the image file format for the document you want to upload | [optional] [default to 'PDF']
**content** | **str** | Please provide the base64 encoded document | 

## Example

```python
from openapi_client.models.supermodel_io_logistics_express_document_images_inner import SupermodelIoLogisticsExpressDocumentImagesInner

# TODO update the JSON string below
json = "{}"
# create an instance of SupermodelIoLogisticsExpressDocumentImagesInner from a JSON string
supermodel_io_logistics_express_document_images_inner_instance = SupermodelIoLogisticsExpressDocumentImagesInner.from_json(json)
# print the JSON string representation of the object
print(SupermodelIoLogisticsExpressDocumentImagesInner.to_json())

# convert the object into a dict
supermodel_io_logistics_express_document_images_inner_dict = supermodel_io_logistics_express_document_images_inner_instance.to_dict()
# create an instance of SupermodelIoLogisticsExpressDocumentImagesInner from a dict
supermodel_io_logistics_express_document_images_inner_from_dict = SupermodelIoLogisticsExpressDocumentImagesInner.from_dict(supermodel_io_logistics_express_document_images_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


