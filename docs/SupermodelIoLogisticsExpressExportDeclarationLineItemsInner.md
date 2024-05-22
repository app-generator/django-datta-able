# SupermodelIoLogisticsExpressExportDeclarationLineItemsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**number** | **int** | Please provide line item number | 
**description** | **str** | Please provide description of the line item | 
**price** | **float** | Please provide unit or article price line item value | 
**quantity** | [**SupermodelIoLogisticsExpressExportDeclarationLineItemsInnerQuantity**](SupermodelIoLogisticsExpressExportDeclarationLineItemsInnerQuantity.md) |  | 
**commodity_codes** | [**List[SupermodelIoLogisticsExpressCreateShipmentRequestContentExportDeclarationLineItemsInnerCommodityCodesInner]**](SupermodelIoLogisticsExpressCreateShipmentRequestContentExportDeclarationLineItemsInnerCommodityCodesInner.md) | Please provide Commodity codes for the shipment at item line level | [optional] 
**export_reason_type** | **str** | Please provide the reason for export | [optional] 
**manufacturer_country** | **str** | Please enter two letter ISO manufacturer country code | 
**weight** | [**SupermodelIoLogisticsExpressExportDeclarationLineItemsInnerWeight**](SupermodelIoLogisticsExpressExportDeclarationLineItemsInnerWeight.md) |  | 
**is_taxes_paid** | **bool** | Please provide if the Taxes is paid for the line item | [optional] 
**customer_references** | [**List[SupermodelIoLogisticsExpressExportDeclarationLineItemsInnerCustomerReferencesInner]**](SupermodelIoLogisticsExpressExportDeclarationLineItemsInnerCustomerReferencesInner.md) | Please provide the Customer References for the line item | [optional] 
**customs_documents** | [**List[SupermodelIoLogisticsExpressExportDeclarationLineItemsInnerCustomsDocumentsInner]**](SupermodelIoLogisticsExpressExportDeclarationLineItemsInnerCustomsDocumentsInner.md) | Please provide the customs documents details | [optional] 
**pre_calculated_line_item_total_value** | **float** | Please provide monetary value of the line item x quantity | [optional] 

## Example

```python
from openapi_client.models.supermodel_io_logistics_express_export_declaration_line_items_inner import SupermodelIoLogisticsExpressExportDeclarationLineItemsInner

# TODO update the JSON string below
json = "{}"
# create an instance of SupermodelIoLogisticsExpressExportDeclarationLineItemsInner from a JSON string
supermodel_io_logistics_express_export_declaration_line_items_inner_instance = SupermodelIoLogisticsExpressExportDeclarationLineItemsInner.from_json(json)
# print the JSON string representation of the object
print(SupermodelIoLogisticsExpressExportDeclarationLineItemsInner.to_json())

# convert the object into a dict
supermodel_io_logistics_express_export_declaration_line_items_inner_dict = supermodel_io_logistics_express_export_declaration_line_items_inner_instance.to_dict()
# create an instance of SupermodelIoLogisticsExpressExportDeclarationLineItemsInner from a dict
supermodel_io_logistics_express_export_declaration_line_items_inner_from_dict = SupermodelIoLogisticsExpressExportDeclarationLineItemsInner.from_dict(supermodel_io_logistics_express_export_declaration_line_items_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


