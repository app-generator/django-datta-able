# SupermodelIoLogisticsExpressCreateShipmentResponseDocumentsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**image_format** | **str** | Identifie image format the document is created in, like PDF, JPG etc. | 
**content** | **str** | Contains base64 encoded document image | 
**type_code** | **str** | Identifie type of the document, like invoice, label or receipt | 
**package_reference_number** | **float** | Package reference number | [optional] 

## Example

```python
from openapi_client.models.supermodel_io_logistics_express_create_shipment_response_documents_inner import SupermodelIoLogisticsExpressCreateShipmentResponseDocumentsInner

# TODO update the JSON string below
json = "{}"
# create an instance of SupermodelIoLogisticsExpressCreateShipmentResponseDocumentsInner from a JSON string
supermodel_io_logistics_express_create_shipment_response_documents_inner_instance = SupermodelIoLogisticsExpressCreateShipmentResponseDocumentsInner.from_json(json)
# print the JSON string representation of the object
print(SupermodelIoLogisticsExpressCreateShipmentResponseDocumentsInner.to_json())

# convert the object into a dict
supermodel_io_logistics_express_create_shipment_response_documents_inner_dict = supermodel_io_logistics_express_create_shipment_response_documents_inner_instance.to_dict()
# create an instance of SupermodelIoLogisticsExpressCreateShipmentResponseDocumentsInner from a dict
supermodel_io_logistics_express_create_shipment_response_documents_inner_from_dict = SupermodelIoLogisticsExpressCreateShipmentResponseDocumentsInner.from_dict(supermodel_io_logistics_express_create_shipment_response_documents_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


