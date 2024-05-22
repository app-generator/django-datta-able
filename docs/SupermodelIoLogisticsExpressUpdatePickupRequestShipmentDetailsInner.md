# SupermodelIoLogisticsExpressUpdatePickupRequestShipmentDetailsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**product_code** | **str** | Please provide DHL Express Global product code of the shipment | 
**local_product_code** | **str** | Please provide DHL Express Local product code of the shipment | [optional] 
**accounts** | [**List[SupermodelIoLogisticsExpressAccount]**](SupermodelIoLogisticsExpressAccount.md) |  | [optional] 
**value_added_services** | [**List[SupermodelIoLogisticsExpressValueAddedServicesRates]**](SupermodelIoLogisticsExpressValueAddedServicesRates.md) |  | [optional] 
**is_customs_declarable** | **bool** | For customs purposes please advise if your shipment is dutiable (true) or non dutiable (false) | 
**declared_value** | **float** | For customs purposes please advise on declared value of the shipment | [optional] 
**declared_value_currency** | **str** | For customs purposes please advise on declared value currency code of the shipment | [optional] 
**unit_of_measurement** | **str** | Please enter Unit of measurement - metric,imperial | 
**shipment_tracking_number** | **str** | Please provide Shipment Identification number (AWB number) | [optional] 
**packages** | [**List[SupermodelIoLogisticsExpressPackageRR]**](SupermodelIoLogisticsExpressPackageRR.md) |  | 

## Example

```python
from openapi_client.models.supermodel_io_logistics_express_update_pickup_request_shipment_details_inner import SupermodelIoLogisticsExpressUpdatePickupRequestShipmentDetailsInner

# TODO update the JSON string below
json = "{}"
# create an instance of SupermodelIoLogisticsExpressUpdatePickupRequestShipmentDetailsInner from a JSON string
supermodel_io_logistics_express_update_pickup_request_shipment_details_inner_instance = SupermodelIoLogisticsExpressUpdatePickupRequestShipmentDetailsInner.from_json(json)
# print the JSON string representation of the object
print(SupermodelIoLogisticsExpressUpdatePickupRequestShipmentDetailsInner.to_json())

# convert the object into a dict
supermodel_io_logistics_express_update_pickup_request_shipment_details_inner_dict = supermodel_io_logistics_express_update_pickup_request_shipment_details_inner_instance.to_dict()
# create an instance of SupermodelIoLogisticsExpressUpdatePickupRequestShipmentDetailsInner from a dict
supermodel_io_logistics_express_update_pickup_request_shipment_details_inner_from_dict = SupermodelIoLogisticsExpressUpdatePickupRequestShipmentDetailsInner.from_dict(supermodel_io_logistics_express_update_pickup_request_shipment_details_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


