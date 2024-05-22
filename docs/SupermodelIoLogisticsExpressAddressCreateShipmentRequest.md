# SupermodelIoLogisticsExpressAddressCreateShipmentRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**postal_code** | **str** | Please enter your postcode or leave empty if the address doesn&#39;t have a postcode | 
**city_name** | **str** | Please enter the city | 
**country_code** | **str** | Please enter ISO country code | 
**province_code** | **str** | Please enter your province or state code | [optional] 
**address_line1** | **str** | Please enter address line 1 | 
**address_line2** | **str** | Please enter address line 2 | [optional] 
**address_line3** | **str** | Please enter address line 3 | [optional] 
**county_name** | **str** | Please enter your suburb or county name | [optional] 
**province_name** | **str** | Please enter your state or province name | [optional] 
**country_name** | **str** | Please enter your country name | [optional] 

## Example

```python
from openapi_client.models.supermodel_io_logistics_express_address_create_shipment_request import SupermodelIoLogisticsExpressAddressCreateShipmentRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SupermodelIoLogisticsExpressAddressCreateShipmentRequest from a JSON string
supermodel_io_logistics_express_address_create_shipment_request_instance = SupermodelIoLogisticsExpressAddressCreateShipmentRequest.from_json(json)
# print the JSON string representation of the object
print(SupermodelIoLogisticsExpressAddressCreateShipmentRequest.to_json())

# convert the object into a dict
supermodel_io_logistics_express_address_create_shipment_request_dict = supermodel_io_logistics_express_address_create_shipment_request_instance.to_dict()
# create an instance of SupermodelIoLogisticsExpressAddressCreateShipmentRequest from a dict
supermodel_io_logistics_express_address_create_shipment_request_from_dict = SupermodelIoLogisticsExpressAddressCreateShipmentRequest.from_dict(supermodel_io_logistics_express_address_create_shipment_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


