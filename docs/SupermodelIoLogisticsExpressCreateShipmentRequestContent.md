# SupermodelIoLogisticsExpressCreateShipmentRequestContent

Here you can define all the properties related to the content of the prospected shipment

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**packages** | [**List[SupermodelIoLogisticsExpressPackage]**](SupermodelIoLogisticsExpressPackage.md) | Here you can define properties per package | 
**is_customs_declarable** | **bool** | For customs purposes please advise if your shipment is dutiable (true) or non dutiable (false).Note:If the shipment is dutiable, exportDeclaration element must be provided. | 
**declared_value** | **float** | For customs purposes please advise on declared value of the shipment | [optional] 
**declared_value_currency** | **str** | For customs purposes please advise on declared value currency code of the shipment | [optional] 
**export_declaration** | [**SupermodelIoLogisticsExpressCreateShipmentRequestContentExportDeclaration**](SupermodelIoLogisticsExpressCreateShipmentRequestContentExportDeclaration.md) |  | [optional] 
**description** | **str** | Please enter description of your shipment | 
**us_filing_type_value** | **str** | This is used for the US AES4, FTR and ITN numbers to be printed on the Transport Label | [optional] 
**incoterm** | **str** | The Incoterms rules are a globally-recognized set of standards, used worldwide in international and domestic contracts for the delivery of goods, illustrating responsibilities between buyer and seller for costs and risk, as well as cargo insurance.&lt;BR&gt;          EXW ExWorks&lt;BR&gt;          FCA Free Carrier&lt;BR&gt;          CPT Carriage Paid To&lt;BR&gt;          CIP Carriage and Insurance Paid To&lt;BR&gt;          DPU Delivered at Place Unloaded&lt;BR&gt;          DAP Delivered at Place&lt;BR&gt;          DDP Delivered Duty Paid&lt;BR&gt;          FAS Free Alongside Ship&lt;BR&gt;          FOB Free on Board&lt;BR&gt;          CFR Cost and Freight&lt;BR&gt;          CIF Cost, Insurance and Freight&lt;BR&gt;          DAF Delivered at Frontier&lt;BR&gt;          DAT Delivered at Terminal&lt;BR&gt;          DDU Delivered Duty Unpaid&lt;BR&gt;          DEQ Delivery ex Quay&lt;BR&gt;          DES Delivered ex Ship | 
**unit_of_measurement** | **str** | Please enter Unit of measurement - metric,imperial | 

## Example

```python
from openapi_client.models.supermodel_io_logistics_express_create_shipment_request_content import SupermodelIoLogisticsExpressCreateShipmentRequestContent

# TODO update the JSON string below
json = "{}"
# create an instance of SupermodelIoLogisticsExpressCreateShipmentRequestContent from a JSON string
supermodel_io_logistics_express_create_shipment_request_content_instance = SupermodelIoLogisticsExpressCreateShipmentRequestContent.from_json(json)
# print the JSON string representation of the object
print(SupermodelIoLogisticsExpressCreateShipmentRequestContent.to_json())

# convert the object into a dict
supermodel_io_logistics_express_create_shipment_request_content_dict = supermodel_io_logistics_express_create_shipment_request_content_instance.to_dict()
# create an instance of SupermodelIoLogisticsExpressCreateShipmentRequestContent from a dict
supermodel_io_logistics_express_create_shipment_request_content_from_dict = SupermodelIoLogisticsExpressCreateShipmentRequestContent.from_dict(supermodel_io_logistics_express_create_shipment_request_content_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


