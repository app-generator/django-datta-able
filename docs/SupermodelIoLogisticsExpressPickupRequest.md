# SupermodelIoLogisticsExpressPickupRequest

RequestPickup schema definition

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**planned_pickup_date_and_time** | **str** | Identifies the date and time the package is ready for pickup Both the date and time portions of the string are expected to be used. The date should not be a past date or a date more than 10 days in the future. The time is the local time of the shipment based on the shipper&#39;s time zone. The date component must be in the format: YYYY-MM-DD; the time component must be in the format: HH:MM:SS using a 24 hour clock. The date and time parts are separated by the letter T (e.g. 2006-06-26T17:00:00 GMT+01:00).&lt;BR&gt;                            | 
**close_time** | **str** | The latest time the location premises is available to dispatch the DHL Express shipment. (HH:MM)  | [optional] 
**location** | **str** | Provides information on where the package should be picked up by DHL courier. &lt;BR&gt;                            | [optional] 
**location_type** | **str** | Provides information on where the package should be picked up by DHL courier. &lt;BR&gt;                            | [optional] 
**accounts** | [**List[SupermodelIoLogisticsExpressAccount]**](SupermodelIoLogisticsExpressAccount.md) |  | 
**special_instructions** | [**List[SupermodelIoLogisticsExpressPickupRequestSpecialInstructionsInner]**](SupermodelIoLogisticsExpressPickupRequestSpecialInstructionsInner.md) | Details special pickup instructions you may wish to send to the DHL Courier. | [optional] 
**remark** | **str** | Please provide additional pickup remark | [optional] 
**customer_details** | [**SupermodelIoLogisticsExpressPickupRequestCustomerDetails**](SupermodelIoLogisticsExpressPickupRequestCustomerDetails.md) |  | 
**shipment_details** | [**List[SupermodelIoLogisticsExpressPickupRequestShipmentDetailsInner]**](SupermodelIoLogisticsExpressPickupRequestShipmentDetailsInner.md) | Please provide details related to shipment you want to do the pickup for | 

## Example

```python
from openapi_client.models.supermodel_io_logistics_express_pickup_request import SupermodelIoLogisticsExpressPickupRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SupermodelIoLogisticsExpressPickupRequest from a JSON string
supermodel_io_logistics_express_pickup_request_instance = SupermodelIoLogisticsExpressPickupRequest.from_json(json)
# print the JSON string representation of the object
print(SupermodelIoLogisticsExpressPickupRequest.to_json())

# convert the object into a dict
supermodel_io_logistics_express_pickup_request_dict = supermodel_io_logistics_express_pickup_request_instance.to_dict()
# create an instance of SupermodelIoLogisticsExpressPickupRequest from a dict
supermodel_io_logistics_express_pickup_request_from_dict = SupermodelIoLogisticsExpressPickupRequest.from_dict(supermodel_io_logistics_express_pickup_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


