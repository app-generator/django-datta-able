# SupermodelIoLogisticsExpressExportDeclarationInvoiceIndicativeCustomsValues

Please provide Perfect Invoice related information

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**import_customs_duty_value** | **float** | Please provide the pre-calculated import customs duties value for the shipment | [optional] 
**import_taxes_value** | **float** | Please provide the pre-calculated import taxes (VAT/GST) value for the shipment | [optional] 
**total_with_import_duties_and_taxes** | **float** | Please provide pre-calculated total of all line items plus additional charges plus indicativeCustomsValues | [optional] 

## Example

```python
from openapi_client.models.supermodel_io_logistics_express_export_declaration_invoice_indicative_customs_values import SupermodelIoLogisticsExpressExportDeclarationInvoiceIndicativeCustomsValues

# TODO update the JSON string below
json = "{}"
# create an instance of SupermodelIoLogisticsExpressExportDeclarationInvoiceIndicativeCustomsValues from a JSON string
supermodel_io_logistics_express_export_declaration_invoice_indicative_customs_values_instance = SupermodelIoLogisticsExpressExportDeclarationInvoiceIndicativeCustomsValues.from_json(json)
# print the JSON string representation of the object
print(SupermodelIoLogisticsExpressExportDeclarationInvoiceIndicativeCustomsValues.to_json())

# convert the object into a dict
supermodel_io_logistics_express_export_declaration_invoice_indicative_customs_values_dict = supermodel_io_logistics_express_export_declaration_invoice_indicative_customs_values_instance.to_dict()
# create an instance of SupermodelIoLogisticsExpressExportDeclarationInvoiceIndicativeCustomsValues from a dict
supermodel_io_logistics_express_export_declaration_invoice_indicative_customs_values_from_dict = SupermodelIoLogisticsExpressExportDeclarationInvoiceIndicativeCustomsValues.from_dict(supermodel_io_logistics_express_export_declaration_invoice_indicative_customs_values_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


