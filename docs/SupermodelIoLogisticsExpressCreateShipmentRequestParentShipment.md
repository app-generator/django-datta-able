# SupermodelIoLogisticsExpressCreateShipmentRequestParentShipment

Please provide the parent (mother) shipment details

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**product_code** | **str** | Please provide the parent (mother) Product Code | [optional] 
**packages_count** | **float** | Please provide the parent (mother) shipment&#39;s Number of Packages | [optional] 

## Example

```python
from openapi_client.models.supermodel_io_logistics_express_create_shipment_request_parent_shipment import SupermodelIoLogisticsExpressCreateShipmentRequestParentShipment

# TODO update the JSON string below
json = "{}"
# create an instance of SupermodelIoLogisticsExpressCreateShipmentRequestParentShipment from a JSON string
supermodel_io_logistics_express_create_shipment_request_parent_shipment_instance = SupermodelIoLogisticsExpressCreateShipmentRequestParentShipment.from_json(json)
# print the JSON string representation of the object
print(SupermodelIoLogisticsExpressCreateShipmentRequestParentShipment.to_json())

# convert the object into a dict
supermodel_io_logistics_express_create_shipment_request_parent_shipment_dict = supermodel_io_logistics_express_create_shipment_request_parent_shipment_instance.to_dict()
# create an instance of SupermodelIoLogisticsExpressCreateShipmentRequestParentShipment from a dict
supermodel_io_logistics_express_create_shipment_request_parent_shipment_from_dict = SupermodelIoLogisticsExpressCreateShipmentRequestParentShipment.from_dict(supermodel_io_logistics_express_create_shipment_request_parent_shipment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


