# SupermodelIoLogisticsExpressPickupRequestCustomerDetails


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**shipper_details** | [**SupermodelIoLogisticsExpressPickupRequestCustomerDetailsShipperDetails**](SupermodelIoLogisticsExpressPickupRequestCustomerDetailsShipperDetails.md) |  | 
**receiver_details** | [**SupermodelIoLogisticsExpressPickupRequestCustomerDetailsShipperDetails**](SupermodelIoLogisticsExpressPickupRequestCustomerDetailsShipperDetails.md) |  | [optional] 
**booking_requestor_details** | [**SupermodelIoLogisticsExpressPickupRequestCustomerDetailsBookingRequestorDetails**](SupermodelIoLogisticsExpressPickupRequestCustomerDetailsBookingRequestorDetails.md) |  | [optional] 
**pickup_details** | [**SupermodelIoLogisticsExpressPickupRequestCustomerDetailsShipperDetails**](SupermodelIoLogisticsExpressPickupRequestCustomerDetailsShipperDetails.md) |  | [optional] 

## Example

```python
from openapi_client.models.supermodel_io_logistics_express_pickup_request_customer_details import SupermodelIoLogisticsExpressPickupRequestCustomerDetails

# TODO update the JSON string below
json = "{}"
# create an instance of SupermodelIoLogisticsExpressPickupRequestCustomerDetails from a JSON string
supermodel_io_logistics_express_pickup_request_customer_details_instance = SupermodelIoLogisticsExpressPickupRequestCustomerDetails.from_json(json)
# print the JSON string representation of the object
print(SupermodelIoLogisticsExpressPickupRequestCustomerDetails.to_json())

# convert the object into a dict
supermodel_io_logistics_express_pickup_request_customer_details_dict = supermodel_io_logistics_express_pickup_request_customer_details_instance.to_dict()
# create an instance of SupermodelIoLogisticsExpressPickupRequestCustomerDetails from a dict
supermodel_io_logistics_express_pickup_request_customer_details_from_dict = SupermodelIoLogisticsExpressPickupRequestCustomerDetails.from_dict(supermodel_io_logistics_express_pickup_request_customer_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


