# SupermodelIoLogisticsExpressLandedCostRequest

Landed cost request model description

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**customer_details** | [**SupermodelIoLogisticsExpressLandedCostRequestCustomerDetails**](SupermodelIoLogisticsExpressLandedCostRequestCustomerDetails.md) |  | 
**accounts** | [**List[SupermodelIoLogisticsExpressAccount]**](SupermodelIoLogisticsExpressAccount.md) | Please enter all the DHL Express accounts and types to be used for this shipment | 
**product_code** | **str** | Please enter DHL Express Global Product code | [optional] 
**local_product_code** | **str** | Please enter DHL Express Local Product code | [optional] 
**unit_of_measurement** | **str** | Please enter Unit of measurement - metric,imperial | 
**currency_code** | **str** | Currency code for the item price (the product being sold) and freight charge. The Landed Cost calculation result will be returned in this defined currency | 
**is_customs_declarable** | **bool** | Set this to true is shipment contains declarable content | 
**is_dtp_requested** | **bool** | Set this to true if you want DHL EXpress product Duties and Taxes Paid outside shipment destination | [optional] 
**is_insurance_requested** | **bool** | Set this true if you ask for DHL Express insurance service | [optional] 
**get_cost_breakdown** | **bool** | Allowed values &#39;true&#39; - item cost breakdown will be returned, &#39;false&#39; - item cost breakdown will not be returned | 
**charges** | [**List[SupermodelIoLogisticsExpressLandedCostRequestChargesInner]**](SupermodelIoLogisticsExpressLandedCostRequestChargesInner.md) | Please provide any additional charges you would like to include in total cost calculation | [optional] 
**shipment_purpose** | **str** | Possible values:&lt;BR&gt;      commercial: B2B&lt;BR&gt;      personal: B2C&lt;BR&gt;      commercia&#39;: B2B&lt;BR&gt;      personal: B2C | [optional] 
**transportation_mode** | **str** |  | [optional] 
**merchant_selected_carrier_name** | **str** | Carrier being used to ship with. Allowed values are:&lt;BR&gt;      &#39;DHL&#39;,&#39;UPS&#39;,&#39;FEDEX&#39;,&#39;TNT&#39;,&#39;POST&#39;,&lt;BR&gt;      &#39;OTHERS&#39; | [optional] 
**packages** | [**List[SupermodelIoLogisticsExpressPackageRR]**](SupermodelIoLogisticsExpressPackageRR.md) | Here you can define properties per package | 
**items** | [**List[SupermodelIoLogisticsExpressLandedCostRequestItemsInner]**](SupermodelIoLogisticsExpressLandedCostRequestItemsInner.md) |  | 
**get_tariff_formula** | **bool** | Allowed values &#39;true&#39; - tariff formula on item and shipment level will be returned, &#39;false&#39; - tariff formula on item and shipment level will not be returned | [optional] 
**get_quotation_id** | **bool** | Allowed values &#39;true&#39; - quotation ID on shipment level will be returned, &#39;false&#39; - quotation ID on shipment level will not be returned | [optional] 

## Example

```python
from openapi_client.models.supermodel_io_logistics_express_landed_cost_request import SupermodelIoLogisticsExpressLandedCostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SupermodelIoLogisticsExpressLandedCostRequest from a JSON string
supermodel_io_logistics_express_landed_cost_request_instance = SupermodelIoLogisticsExpressLandedCostRequest.from_json(json)
# print the JSON string representation of the object
print(SupermodelIoLogisticsExpressLandedCostRequest.to_json())

# convert the object into a dict
supermodel_io_logistics_express_landed_cost_request_dict = supermodel_io_logistics_express_landed_cost_request_instance.to_dict()
# create an instance of SupermodelIoLogisticsExpressLandedCostRequest from a dict
supermodel_io_logistics_express_landed_cost_request_from_dict = SupermodelIoLogisticsExpressLandedCostRequest.from_dict(supermodel_io_logistics_express_landed_cost_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


