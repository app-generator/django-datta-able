# SupermodelIoLogisticsExpressExportDeclaration

Here you can find all details related to export declaration

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**line_items** | [**List[SupermodelIoLogisticsExpressExportDeclarationLineItemsInner]**](SupermodelIoLogisticsExpressExportDeclarationLineItemsInner.md) | Please enter details for each export line item | 
**invoice** | [**SupermodelIoLogisticsExpressExportDeclarationInvoice**](SupermodelIoLogisticsExpressExportDeclarationInvoice.md) |  | 
**remarks** | [**List[SupermodelIoLogisticsExpressExportDeclarationRemarksInner]**](SupermodelIoLogisticsExpressExportDeclarationRemarksInner.md) | Please enter up to three remarks | [optional] 
**additional_charges** | [**List[SupermodelIoLogisticsExpressExportDeclarationAdditionalChargesInner]**](SupermodelIoLogisticsExpressExportDeclarationAdditionalChargesInner.md) | Please enter additional charge to appear on the invoice&lt;BR&gt;      admin, Administration Charge&lt;BR&gt;      delivery, Delivery Charge&lt;BR&gt;      documentation, Documentation Charge&lt;BR&gt;      expedite, Expedite Charge&lt;BR&gt;      freight, Freight Charge&lt;BR&gt;      fuel surcharge, Fuel Surcharge&lt;BR&gt;      logistic, Logistic Charge&lt;BR&gt;      other, Other Charge&lt;BR&gt;      packaging, Packaging Charge&lt;BR&gt;      pickup, Pickup Charge&lt;BR&gt;      handling, Handling Charge&lt;BR&gt;      vat, VAT Charge&lt;BR&gt;      insurance, Insurance Cost | [optional] 
**place_of_incoterm** | **str** | Name of port of departure, shipment or destination as required under the applicable delivery term. | [optional] 
**recipient_reference** | **str** | Please enter recipient reference | [optional] 
**exporter** | [**SupermodelIoLogisticsExpressCreateShipmentRequestContentExportDeclarationExporter**](SupermodelIoLogisticsExpressCreateShipmentRequestContentExportDeclarationExporter.md) |  | [optional] 
**export_reason_type** | **str** | Please provide the reason for export | [optional] 
**shipment_type** | **str** | Please provide the shipment was sent for Personal (Gift) or Commercial (Sale) reasons | [optional] 
**customs_documents** | [**List[SupermodelIoLogisticsExpressExportDeclarationCustomsDocumentsInner]**](SupermodelIoLogisticsExpressExportDeclarationCustomsDocumentsInner.md) | Please provide the Customs Documents at invoice level | [optional] 
**incoterm** | **str** | The Incoterms rules are a globally-recognized set of standards, used worldwide in international and domestic contracts for the delivery of goods, illustrating responsibilities between buyer and seller for costs and risk, as well as cargo insurance.&lt;BR&gt;      EXW ExWorks&lt;BR&gt;      FCA Free Carrier&lt;BR&gt;      CPT Carriage Paid To&lt;BR&gt;      CIP Carriage and Insurance Paid To&lt;BR&gt;      DPU Delivered at Place Unloaded&lt;BR&gt;      DAP Delivered at Place&lt;BR&gt;      DDP Delivered Duty Paid&lt;BR&gt;      FAS Free Alongside Ship&lt;BR&gt;      FOB Free on Board&lt;BR&gt;      CFR Cost and Freight&lt;BR&gt;      CIF Cost, Insurance and Freight&lt;BR&gt;      DAF Delivered at Frontier&lt;BR&gt;      DAT Delivered at Terminal&lt;BR&gt;      DDU Delivered Duty Unpaid&lt;BR&gt;      DEQ Delivery ex Quay&lt;BR&gt;      DES Delivered ex Ship | 

## Example

```python
from openapi_client.models.supermodel_io_logistics_express_export_declaration import SupermodelIoLogisticsExpressExportDeclaration

# TODO update the JSON string below
json = "{}"
# create an instance of SupermodelIoLogisticsExpressExportDeclaration from a JSON string
supermodel_io_logistics_express_export_declaration_instance = SupermodelIoLogisticsExpressExportDeclaration.from_json(json)
# print the JSON string representation of the object
print(SupermodelIoLogisticsExpressExportDeclaration.to_json())

# convert the object into a dict
supermodel_io_logistics_express_export_declaration_dict = supermodel_io_logistics_express_export_declaration_instance.to_dict()
# create an instance of SupermodelIoLogisticsExpressExportDeclaration from a dict
supermodel_io_logistics_express_export_declaration_from_dict = SupermodelIoLogisticsExpressExportDeclaration.from_dict(supermodel_io_logistics_express_export_declaration_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


