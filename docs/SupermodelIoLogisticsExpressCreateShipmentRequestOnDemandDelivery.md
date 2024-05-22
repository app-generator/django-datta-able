# SupermodelIoLogisticsExpressCreateShipmentRequestOnDemandDelivery

Here you can provide data in case you wish to use DHL Express On demand delivery service

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**delivery_option** | **str** | Please choose from one of the delivery options | 
**location** | **str** | If delivery option is signatureDelivery please specify location where to leave the shipment | [optional] 
**special_instructions** | **str** | Please enter additional information that might be useful for the DHL Express courier. This field is conditionally mandatory if selected location is &#39;Other&#39;. | [optional] 
**gate_code** | **str** | Please provide entry code to gain access to an apartment complex or gate | [optional] 
**where_to_leave** | **str** | In ase your deliveryOption is &#39;neighbour&#39; please specify where to leave the package  | [optional] 
**neighbour_name** | **str** | In case you wish to leave the package with neighbour please provide the neighbour&#39;s name | [optional] 
**neighbour_house_number** | **str** | In case you wish to leave the package with neighbour please provide the neighbour&#39;s house number | [optional] 
**authorizer_name** | **str** | In case your delivery option is &#39;signatureRelease&#39; please provide name of the person who is authorized to sign and receive the package | [optional] 
**service_point_id** | **str** | In case your delivery option is &#39;servicepoint&#39; please provide unique DHL Express Service point location ID of where the parcel should be delieverd (please contact your local DHL Express Account Manager to obtain the list of the servicepoint IDs) | [optional] 
**requested_delivery_date** | **str** | for future use | [optional] 

## Example

```python
from openapi_client.models.supermodel_io_logistics_express_create_shipment_request_on_demand_delivery import SupermodelIoLogisticsExpressCreateShipmentRequestOnDemandDelivery

# TODO update the JSON string below
json = "{}"
# create an instance of SupermodelIoLogisticsExpressCreateShipmentRequestOnDemandDelivery from a JSON string
supermodel_io_logistics_express_create_shipment_request_on_demand_delivery_instance = SupermodelIoLogisticsExpressCreateShipmentRequestOnDemandDelivery.from_json(json)
# print the JSON string representation of the object
print(SupermodelIoLogisticsExpressCreateShipmentRequestOnDemandDelivery.to_json())

# convert the object into a dict
supermodel_io_logistics_express_create_shipment_request_on_demand_delivery_dict = supermodel_io_logistics_express_create_shipment_request_on_demand_delivery_instance.to_dict()
# create an instance of SupermodelIoLogisticsExpressCreateShipmentRequestOnDemandDelivery from a dict
supermodel_io_logistics_express_create_shipment_request_on_demand_delivery_from_dict = SupermodelIoLogisticsExpressCreateShipmentRequestOnDemandDelivery.from_dict(supermodel_io_logistics_express_create_shipment_request_on_demand_delivery_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


