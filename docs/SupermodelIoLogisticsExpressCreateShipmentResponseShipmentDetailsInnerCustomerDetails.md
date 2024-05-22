# SupermodelIoLogisticsExpressCreateShipmentResponseShipmentDetailsInnerCustomerDetails

Here you need to define all the parties needed to ship the package

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**shipper_details** | [**SupermodelIoLogisticsExpressCreateShipmentResponseShipmentDetailsInnerCustomerDetailsShipperDetails**](SupermodelIoLogisticsExpressCreateShipmentResponseShipmentDetailsInnerCustomerDetailsShipperDetails.md) |  | [optional] 
**receiver_details** | [**SupermodelIoLogisticsExpressCreateShipmentResponseShipmentDetailsInnerCustomerDetailsShipperDetails**](SupermodelIoLogisticsExpressCreateShipmentResponseShipmentDetailsInnerCustomerDetailsShipperDetails.md) |  | [optional] 

## Example

```python
from openapi_client.models.supermodel_io_logistics_express_create_shipment_response_shipment_details_inner_customer_details import SupermodelIoLogisticsExpressCreateShipmentResponseShipmentDetailsInnerCustomerDetails

# TODO update the JSON string below
json = "{}"
# create an instance of SupermodelIoLogisticsExpressCreateShipmentResponseShipmentDetailsInnerCustomerDetails from a JSON string
supermodel_io_logistics_express_create_shipment_response_shipment_details_inner_customer_details_instance = SupermodelIoLogisticsExpressCreateShipmentResponseShipmentDetailsInnerCustomerDetails.from_json(json)
# print the JSON string representation of the object
print(SupermodelIoLogisticsExpressCreateShipmentResponseShipmentDetailsInnerCustomerDetails.to_json())

# convert the object into a dict
supermodel_io_logistics_express_create_shipment_response_shipment_details_inner_customer_details_dict = supermodel_io_logistics_express_create_shipment_response_shipment_details_inner_customer_details_instance.to_dict()
# create an instance of SupermodelIoLogisticsExpressCreateShipmentResponseShipmentDetailsInnerCustomerDetails from a dict
supermodel_io_logistics_express_create_shipment_response_shipment_details_inner_customer_details_from_dict = SupermodelIoLogisticsExpressCreateShipmentResponseShipmentDetailsInnerCustomerDetails.from_dict(supermodel_io_logistics_express_create_shipment_response_shipment_details_inner_customer_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


