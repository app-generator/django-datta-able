# SupermodelIoLogisticsExpressCreateShipmentResponseShipmentDetailsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**service_handling_feature_codes** | **List[str]** | This array contains all the DHL Express special handling feature codes | [optional] 
**volumetric_weight** | **float** | Here you can find calculated volumetric weight based on dimensions provided in the request | [optional] 
**billing_code** | **str** | Here you can find billing code which was applied on your shipment | [optional] 
**service_content_code** | **str** | Here you can find the DHL Express shipment content code of your shipment | [optional] 
**customer_details** | [**SupermodelIoLogisticsExpressCreateShipmentResponseShipmentDetailsInnerCustomerDetails**](SupermodelIoLogisticsExpressCreateShipmentResponseShipmentDetailsInnerCustomerDetails.md) |  | [optional] 
**origin_service_area** | [**SupermodelIoLogisticsExpressCreateShipmentResponseShipmentDetailsInnerOriginServiceArea**](SupermodelIoLogisticsExpressCreateShipmentResponseShipmentDetailsInnerOriginServiceArea.md) |  | [optional] 
**destination_service_area** | [**SupermodelIoLogisticsExpressCreateShipmentResponseShipmentDetailsInnerDestinationServiceArea**](SupermodelIoLogisticsExpressCreateShipmentResponseShipmentDetailsInnerDestinationServiceArea.md) |  | [optional] 
**dhl_routing_code** | **str** | Here you can find DHL Routing Code which was applied on your shipment | [optional] 
**dhl_routing_data_id** | **str** | Here you can find DHL Routing Data ID which was applied on your shipment | [optional] 
**delivery_date_code** | **str** | Here you can find Delivery Date Code which was applied on your shipment | [optional] 
**delivery_time_code** | **str** | Here you can find Delivery Time Code which was applied on your shipment | [optional] 
**product_short_name** | **str** | Here you can find the product short name of your shipment | [optional] 
**value_added_services** | [**List[SupermodelIoLogisticsExpressCreateShipmentResponseShipmentDetailsInnerValueAddedServicesInner]**](SupermodelIoLogisticsExpressCreateShipmentResponseShipmentDetailsInnerValueAddedServicesInner.md) |  | [optional] 
**pickup_details** | [**SupermodelIoLogisticsExpressCreateShipmentResponseShipmentDetailsInnerPickupDetails**](SupermodelIoLogisticsExpressCreateShipmentResponseShipmentDetailsInnerPickupDetails.md) |  | [optional] 

## Example

```python
from openapi_client.models.supermodel_io_logistics_express_create_shipment_response_shipment_details_inner import SupermodelIoLogisticsExpressCreateShipmentResponseShipmentDetailsInner

# TODO update the JSON string below
json = "{}"
# create an instance of SupermodelIoLogisticsExpressCreateShipmentResponseShipmentDetailsInner from a JSON string
supermodel_io_logistics_express_create_shipment_response_shipment_details_inner_instance = SupermodelIoLogisticsExpressCreateShipmentResponseShipmentDetailsInner.from_json(json)
# print the JSON string representation of the object
print(SupermodelIoLogisticsExpressCreateShipmentResponseShipmentDetailsInner.to_json())

# convert the object into a dict
supermodel_io_logistics_express_create_shipment_response_shipment_details_inner_dict = supermodel_io_logistics_express_create_shipment_response_shipment_details_inner_instance.to_dict()
# create an instance of SupermodelIoLogisticsExpressCreateShipmentResponseShipmentDetailsInner from a dict
supermodel_io_logistics_express_create_shipment_response_shipment_details_inner_from_dict = SupermodelIoLogisticsExpressCreateShipmentResponseShipmentDetailsInner.from_dict(supermodel_io_logistics_express_create_shipment_response_shipment_details_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


