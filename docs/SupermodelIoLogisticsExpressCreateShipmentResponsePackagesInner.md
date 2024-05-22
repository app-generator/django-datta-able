# SupermodelIoLogisticsExpressCreateShipmentResponsePackagesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**reference_number** | **float** | Piece serial number | [optional] 
**tracking_number** | **str** | Here is provided each piece its Identification number | 
**tracking_url** | **str** | You can use ths URL to track your shipment by Piece Identification Number | [optional] 
**volumetric_weight** | **float** | Here is provided each piece volumetric/ dimensional weight | [optional] 
**documents** | [**List[SupermodelIoLogisticsExpressCreateShipmentResponsePackagesInnerDocumentsInner]**](SupermodelIoLogisticsExpressCreateShipmentResponsePackagesInnerDocumentsInner.md) | Here you can find all documents created for the piece&#39;s QRcode | [optional] 

## Example

```python
from openapi_client.models.supermodel_io_logistics_express_create_shipment_response_packages_inner import SupermodelIoLogisticsExpressCreateShipmentResponsePackagesInner

# TODO update the JSON string below
json = "{}"
# create an instance of SupermodelIoLogisticsExpressCreateShipmentResponsePackagesInner from a JSON string
supermodel_io_logistics_express_create_shipment_response_packages_inner_instance = SupermodelIoLogisticsExpressCreateShipmentResponsePackagesInner.from_json(json)
# print the JSON string representation of the object
print(SupermodelIoLogisticsExpressCreateShipmentResponsePackagesInner.to_json())

# convert the object into a dict
supermodel_io_logistics_express_create_shipment_response_packages_inner_dict = supermodel_io_logistics_express_create_shipment_response_packages_inner_instance.to_dict()
# create an instance of SupermodelIoLogisticsExpressCreateShipmentResponsePackagesInner from a dict
supermodel_io_logistics_express_create_shipment_response_packages_inner_from_dict = SupermodelIoLogisticsExpressCreateShipmentResponsePackagesInner.from_dict(supermodel_io_logistics_express_create_shipment_response_packages_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


