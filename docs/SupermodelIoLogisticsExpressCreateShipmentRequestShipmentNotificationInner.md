# SupermodelIoLogisticsExpressCreateShipmentRequestShipmentNotificationInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type_code** | **str** | Please enter channel type to send the notification by. At this moment only email is supported | 
**receiver_id** | **str** | Please enter notification receiver email address | 
**language_code** | **str** | Please enter three letter lanuage code in which you wish to receive the notification in | [optional] [default to 'eng']
**language_country_code** | **str** | Please enter two letter language country code | [optional] [default to 'UK']
**bespoke_message** | **str** | Please enter your message which will be added to the DHL Express notification email | [optional] 

## Example

```python
from openapi_client.models.supermodel_io_logistics_express_create_shipment_request_shipment_notification_inner import SupermodelIoLogisticsExpressCreateShipmentRequestShipmentNotificationInner

# TODO update the JSON string below
json = "{}"
# create an instance of SupermodelIoLogisticsExpressCreateShipmentRequestShipmentNotificationInner from a JSON string
supermodel_io_logistics_express_create_shipment_request_shipment_notification_inner_instance = SupermodelIoLogisticsExpressCreateShipmentRequestShipmentNotificationInner.from_json(json)
# print the JSON string representation of the object
print(SupermodelIoLogisticsExpressCreateShipmentRequestShipmentNotificationInner.to_json())

# convert the object into a dict
supermodel_io_logistics_express_create_shipment_request_shipment_notification_inner_dict = supermodel_io_logistics_express_create_shipment_request_shipment_notification_inner_instance.to_dict()
# create an instance of SupermodelIoLogisticsExpressCreateShipmentRequestShipmentNotificationInner from a dict
supermodel_io_logistics_express_create_shipment_request_shipment_notification_inner_from_dict = SupermodelIoLogisticsExpressCreateShipmentRequestShipmentNotificationInner.from_dict(supermodel_io_logistics_express_create_shipment_request_shipment_notification_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


