# SupermodelIoLogisticsExpressCreateShipmentRequestContentExportDeclarationInvoiceIndicativeCustomsValues

indicativeCustomsValues contains child nodes importCustomsDutyValue and importTaxesValue.<BR>                  <BR>                  These 2 child elements are only applicable for Commercial Invoice printing purpose in Customs Invoice template*: COMMERCIAL_INVOICE_P_10 and COMMERCIAL_INVOICE_L_10.<BR>                  If any of this child nodes are present, it will only be able to display up to three OtherCharges. <BR>                  <BR>                  Nonetheless, the ShipmentRequest can still contain up to five additionalCharges.<BR>                  If there are more than three additionalCharges, the third additionalCharges onwards will be combined and displayed under one single caption of 'Other Charges'.<BR>                  <BR>                  Note: If either first or second additionalCharges has typeCode of 'other', and there are more than three additionalCharges provided in the request, the additionalCharges with typeCode of 'other' will be consolidated under the combined 'Other Charges' caption as well.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**import_customs_duty_value** | **float** | Please provide the pre-calculated import customs duties value for the shipment | [optional] 
**import_taxes_value** | **float** | Please provide the pre-calculated import taxes (VAT/GST) value for the shipment | [optional] 
**total_with_import_duties_and_taxes** | **float** | Please provide pre-calculated total of all line items plus additional charges plus indicativeCustomsValues | [optional] 

## Example

```python
from openapi_client.models.supermodel_io_logistics_express_create_shipment_request_content_export_declaration_invoice_indicative_customs_values import SupermodelIoLogisticsExpressCreateShipmentRequestContentExportDeclarationInvoiceIndicativeCustomsValues

# TODO update the JSON string below
json = "{}"
# create an instance of SupermodelIoLogisticsExpressCreateShipmentRequestContentExportDeclarationInvoiceIndicativeCustomsValues from a JSON string
supermodel_io_logistics_express_create_shipment_request_content_export_declaration_invoice_indicative_customs_values_instance = SupermodelIoLogisticsExpressCreateShipmentRequestContentExportDeclarationInvoiceIndicativeCustomsValues.from_json(json)
# print the JSON string representation of the object
print(SupermodelIoLogisticsExpressCreateShipmentRequestContentExportDeclarationInvoiceIndicativeCustomsValues.to_json())

# convert the object into a dict
supermodel_io_logistics_express_create_shipment_request_content_export_declaration_invoice_indicative_customs_values_dict = supermodel_io_logistics_express_create_shipment_request_content_export_declaration_invoice_indicative_customs_values_instance.to_dict()
# create an instance of SupermodelIoLogisticsExpressCreateShipmentRequestContentExportDeclarationInvoiceIndicativeCustomsValues from a dict
supermodel_io_logistics_express_create_shipment_request_content_export_declaration_invoice_indicative_customs_values_from_dict = SupermodelIoLogisticsExpressCreateShipmentRequestContentExportDeclarationInvoiceIndicativeCustomsValues.from_dict(supermodel_io_logistics_express_create_shipment_request_content_export_declaration_invoice_indicative_customs_values_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


