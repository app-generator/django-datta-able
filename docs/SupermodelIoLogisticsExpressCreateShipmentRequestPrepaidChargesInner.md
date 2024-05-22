# SupermodelIoLogisticsExpressCreateShipmentRequestPrepaidChargesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type_code** | **str** | Please enter type of prepaid charge. At this moment only freight is supported | 
**currency** | **str** | Please enter currency for the value you have entered into value field | 
**value** | **float** | Please enter nominal value related to the charge | 
**method** | **str** | Please enter method you have used to pay the charges. At this moment only cash is supported | 

## Example

```python
from openapi_client.models.supermodel_io_logistics_express_create_shipment_request_prepaid_charges_inner import SupermodelIoLogisticsExpressCreateShipmentRequestPrepaidChargesInner

# TODO update the JSON string below
json = "{}"
# create an instance of SupermodelIoLogisticsExpressCreateShipmentRequestPrepaidChargesInner from a JSON string
supermodel_io_logistics_express_create_shipment_request_prepaid_charges_inner_instance = SupermodelIoLogisticsExpressCreateShipmentRequestPrepaidChargesInner.from_json(json)
# print the JSON string representation of the object
print(SupermodelIoLogisticsExpressCreateShipmentRequestPrepaidChargesInner.to_json())

# convert the object into a dict
supermodel_io_logistics_express_create_shipment_request_prepaid_charges_inner_dict = supermodel_io_logistics_express_create_shipment_request_prepaid_charges_inner_instance.to_dict()
# create an instance of SupermodelIoLogisticsExpressCreateShipmentRequestPrepaidChargesInner from a dict
supermodel_io_logistics_express_create_shipment_request_prepaid_charges_inner_from_dict = SupermodelIoLogisticsExpressCreateShipmentRequestPrepaidChargesInner.from_dict(supermodel_io_logistics_express_create_shipment_request_prepaid_charges_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


