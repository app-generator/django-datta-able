# SupermodelIoLogisticsExpressExportDeclarationCustomsDocumentsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type_code** | **str** | Please provide the Customs Document type code at invoice level. Please refer to the YAML Reference Data Guide PDF file for valid enumeration values. | 
**value** | **str** | Please provide the Customs Document ID at invoice level | 

## Example

```python
from openapi_client.models.supermodel_io_logistics_express_export_declaration_customs_documents_inner import SupermodelIoLogisticsExpressExportDeclarationCustomsDocumentsInner

# TODO update the JSON string below
json = "{}"
# create an instance of SupermodelIoLogisticsExpressExportDeclarationCustomsDocumentsInner from a JSON string
supermodel_io_logistics_express_export_declaration_customs_documents_inner_instance = SupermodelIoLogisticsExpressExportDeclarationCustomsDocumentsInner.from_json(json)
# print the JSON string representation of the object
print(SupermodelIoLogisticsExpressExportDeclarationCustomsDocumentsInner.to_json())

# convert the object into a dict
supermodel_io_logistics_express_export_declaration_customs_documents_inner_dict = supermodel_io_logistics_express_export_declaration_customs_documents_inner_instance.to_dict()
# create an instance of SupermodelIoLogisticsExpressExportDeclarationCustomsDocumentsInner from a dict
supermodel_io_logistics_express_export_declaration_customs_documents_inner_from_dict = SupermodelIoLogisticsExpressExportDeclarationCustomsDocumentsInner.from_dict(supermodel_io_logistics_express_export_declaration_customs_documents_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


