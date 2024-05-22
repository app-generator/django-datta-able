# SupermodelIoLogisticsExpressExportDeclarationInvoice

Please provide invoice related information

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**number** | **str** | Please enter commercial invoice number | 
**var_date** | **str** | Please enter commercial invoice date | 
**function** | **str** | Please provide the purpose was the document details captured and are planned to be used. Note: export and import is only applicable for approve Sale In Transit customers | 
**customer_references** | [**List[SupermodelIoLogisticsExpressExportDeclarationInvoiceCustomerReferencesInner]**](SupermodelIoLogisticsExpressExportDeclarationInvoiceCustomerReferencesInner.md) | Please provide the customer references at invoice level.   Note: customerReference/0/value with typeCode &#39;CU&#39; is mandatory if using POST method and no shipmentTrackingNumber is provided in request. It is recommended to provide less than 20 customer references of &#39;MRN&#39; type code | [optional] 
**indicative_customs_values** | [**SupermodelIoLogisticsExpressExportDeclarationInvoiceIndicativeCustomsValues**](SupermodelIoLogisticsExpressExportDeclarationInvoiceIndicativeCustomsValues.md) |  | [optional] 
**pre_calculated_total_values** | [**SupermodelIoLogisticsExpressExportDeclarationInvoicePreCalculatedTotalValues**](SupermodelIoLogisticsExpressExportDeclarationInvoicePreCalculatedTotalValues.md) |  | [optional] 

## Example

```python
from openapi_client.models.supermodel_io_logistics_express_export_declaration_invoice import SupermodelIoLogisticsExpressExportDeclarationInvoice

# TODO update the JSON string below
json = "{}"
# create an instance of SupermodelIoLogisticsExpressExportDeclarationInvoice from a JSON string
supermodel_io_logistics_express_export_declaration_invoice_instance = SupermodelIoLogisticsExpressExportDeclarationInvoice.from_json(json)
# print the JSON string representation of the object
print(SupermodelIoLogisticsExpressExportDeclarationInvoice.to_json())

# convert the object into a dict
supermodel_io_logistics_express_export_declaration_invoice_dict = supermodel_io_logistics_express_export_declaration_invoice_instance.to_dict()
# create an instance of SupermodelIoLogisticsExpressExportDeclarationInvoice from a dict
supermodel_io_logistics_express_export_declaration_invoice_from_dict = SupermodelIoLogisticsExpressExportDeclarationInvoice.from_dict(supermodel_io_logistics_express_export_declaration_invoice_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


