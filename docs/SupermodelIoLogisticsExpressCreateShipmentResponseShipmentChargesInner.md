# SupermodelIoLogisticsExpressCreateShipmentResponseShipmentChargesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**currency_type** | **str** | Possible Values :&lt;BR&gt;            - &#39;BILLC&#39;, billing currency&lt;BR&gt;            - &#39;PULCL&#39;, country public rates currency&lt;BR&gt;            - &#39;BASEC&#39;, base currency | 
**price_currency** | **str** | This the currency of the rated shipment for the prices listed. | 
**price** | **float** | The amount price of DHL product and services | 
**service_breakdown** | [**List[SupermodelIoLogisticsExpressCreateShipmentResponseShipmentChargesInnerServiceBreakdownInner]**](SupermodelIoLogisticsExpressCreateShipmentResponseShipmentChargesInnerServiceBreakdownInner.md) |  | [optional] 

## Example

```python
from openapi_client.models.supermodel_io_logistics_express_create_shipment_response_shipment_charges_inner import SupermodelIoLogisticsExpressCreateShipmentResponseShipmentChargesInner

# TODO update the JSON string below
json = "{}"
# create an instance of SupermodelIoLogisticsExpressCreateShipmentResponseShipmentChargesInner from a JSON string
supermodel_io_logistics_express_create_shipment_response_shipment_charges_inner_instance = SupermodelIoLogisticsExpressCreateShipmentResponseShipmentChargesInner.from_json(json)
# print the JSON string representation of the object
print(SupermodelIoLogisticsExpressCreateShipmentResponseShipmentChargesInner.to_json())

# convert the object into a dict
supermodel_io_logistics_express_create_shipment_response_shipment_charges_inner_dict = supermodel_io_logistics_express_create_shipment_response_shipment_charges_inner_instance.to_dict()
# create an instance of SupermodelIoLogisticsExpressCreateShipmentResponseShipmentChargesInner from a dict
supermodel_io_logistics_express_create_shipment_response_shipment_charges_inner_from_dict = SupermodelIoLogisticsExpressCreateShipmentResponseShipmentChargesInner.from_dict(supermodel_io_logistics_express_create_shipment_response_shipment_charges_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


