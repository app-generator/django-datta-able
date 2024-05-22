# SupermodelIoLogisticsExpressCreateShipmentRequestContentExportDeclarationInvoice

Please provide invoice related information

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**number** | **str** | Please enter commercial invoice number | 
**var_date** | **date** | Please enter commercial invoice date | 
**signature_name** | **str** | Please enter who has signed the invoce | [optional] 
**signature_title** | **str** | Please provide title of person who has signed the invoice | [optional] 
**signature_image** | **str** | Please provide the signature image | [optional] 
**instructions** | **List[str]** | Shipment instructions for customs invoice printing purposes. Printed only when using Customs Invoice template COMMERCIAL_INVOICE_04. If using Customs Invoice template    COMMERCIAL_INVOICE_04, recommended max length is 120 characters. | [optional] 
**customer_data_text_entries** | **List[str]** | Customer data text to be printed in&lt;BR&gt;                  customs invoice.&lt;BR&gt;                  Printed only when using Customs&lt;BR&gt;                  Invoice template&lt;BR&gt;                  COMMERCIAL_INVOICE_04. | [optional] 
**total_net_weight** | **float** | Please provide the total net weight | [optional] 
**total_gross_weight** | **float** | Please provide the total gross weight | [optional] 
**customer_references** | [**List[SupermodelIoLogisticsExpressCreateShipmentRequestContentExportDeclarationInvoiceCustomerReferencesInner]**](SupermodelIoLogisticsExpressCreateShipmentRequestContentExportDeclarationInvoiceCustomerReferencesInner.md) | Please provide the customer references at invoice level. It is recommended to provide less than 20 customer references of &#39;MRN&#39; type code. | [optional] 
**terms_of_payment** | **str** | Please provide the terms of payment | [optional] 
**indicative_customs_values** | [**SupermodelIoLogisticsExpressCreateShipmentRequestContentExportDeclarationInvoiceIndicativeCustomsValues**](SupermodelIoLogisticsExpressCreateShipmentRequestContentExportDeclarationInvoiceIndicativeCustomsValues.md) |  | [optional] 
**pre_calculated_total_values** | [**SupermodelIoLogisticsExpressCreateShipmentRequestContentExportDeclarationInvoicePreCalculatedTotalValues**](SupermodelIoLogisticsExpressCreateShipmentRequestContentExportDeclarationInvoicePreCalculatedTotalValues.md) |  | [optional] 

## Example

```python
from openapi_client.models.supermodel_io_logistics_express_create_shipment_request_content_export_declaration_invoice import SupermodelIoLogisticsExpressCreateShipmentRequestContentExportDeclarationInvoice

# TODO update the JSON string below
json = "{}"
# create an instance of SupermodelIoLogisticsExpressCreateShipmentRequestContentExportDeclarationInvoice from a JSON string
supermodel_io_logistics_express_create_shipment_request_content_export_declaration_invoice_instance = SupermodelIoLogisticsExpressCreateShipmentRequestContentExportDeclarationInvoice.from_json(json)
# print the JSON string representation of the object
print(SupermodelIoLogisticsExpressCreateShipmentRequestContentExportDeclarationInvoice.to_json())

# convert the object into a dict
supermodel_io_logistics_express_create_shipment_request_content_export_declaration_invoice_dict = supermodel_io_logistics_express_create_shipment_request_content_export_declaration_invoice_instance.to_dict()
# create an instance of SupermodelIoLogisticsExpressCreateShipmentRequestContentExportDeclarationInvoice from a dict
supermodel_io_logistics_express_create_shipment_request_content_export_declaration_invoice_from_dict = SupermodelIoLogisticsExpressCreateShipmentRequestContentExportDeclarationInvoice.from_dict(supermodel_io_logistics_express_create_shipment_request_content_export_declaration_invoice_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


