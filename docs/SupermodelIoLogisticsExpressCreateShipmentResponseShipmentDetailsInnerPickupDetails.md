# SupermodelIoLogisticsExpressCreateShipmentResponseShipmentDetailsInnerPickupDetails

Here you can find pickup details

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**local_cutoff_date_and_time** | **str** | Pickup booking cutoff time | [optional] 
**gmt_cutoff_time** | **str** | Pickup cutoff time in GMT | [optional] 
**cutoff_time_offset** | **str** | Pickup booking cutoff time in GMT offset | [optional] 
**pickup_earliest** | **str** | The DHL earliest time possible for pickup | [optional] 
**pickup_latest** | **str** | The DHL latest time possible for pickup | [optional] 
**total_transit_days** | **str** | The number of transit days | [optional] 
**pickup_additional_days** | **str** | This is additional transit delays (in days) for shipment picked up from the mentioned city or postal area to arrival at the service area | [optional] 
**delivery_additional_days** | **str** | This is additional transit delays (in days) for shipment delivered to the mentioned city or postal area following arrival at the service area | [optional] 
**pickup_day_of_week** | **str** | Pickup day of the week number | [optional] 
**delivery_day_of_week** | **str** | Destination day of the week number | [optional] 

## Example

```python
from openapi_client.models.supermodel_io_logistics_express_create_shipment_response_shipment_details_inner_pickup_details import SupermodelIoLogisticsExpressCreateShipmentResponseShipmentDetailsInnerPickupDetails

# TODO update the JSON string below
json = "{}"
# create an instance of SupermodelIoLogisticsExpressCreateShipmentResponseShipmentDetailsInnerPickupDetails from a JSON string
supermodel_io_logistics_express_create_shipment_response_shipment_details_inner_pickup_details_instance = SupermodelIoLogisticsExpressCreateShipmentResponseShipmentDetailsInnerPickupDetails.from_json(json)
# print the JSON string representation of the object
print(SupermodelIoLogisticsExpressCreateShipmentResponseShipmentDetailsInnerPickupDetails.to_json())

# convert the object into a dict
supermodel_io_logistics_express_create_shipment_response_shipment_details_inner_pickup_details_dict = supermodel_io_logistics_express_create_shipment_response_shipment_details_inner_pickup_details_instance.to_dict()
# create an instance of SupermodelIoLogisticsExpressCreateShipmentResponseShipmentDetailsInnerPickupDetails from a dict
supermodel_io_logistics_express_create_shipment_response_shipment_details_inner_pickup_details_from_dict = SupermodelIoLogisticsExpressCreateShipmentResponseShipmentDetailsInnerPickupDetails.from_dict(supermodel_io_logistics_express_create_shipment_response_shipment_details_inner_pickup_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


