# SupermodelIoLogisticsExpressAddressCreateShipmentResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**postal_code** | **str** | Postal code | 
**city_name** | **str** | City name | 
**country_code** | **str** | Country code | 
**province_code** | **str** | Province or state code | [optional] 
**address_line1** | **str** | Address line 1 | 
**address_line2** | **str** | Address line 2 | [optional] 
**address_line3** | **str** | Address line 3 | [optional] 
**city_district_name** | **str** | Suburb or county name | [optional] 
**province_name** | **str** | Please enter your state or province name | [optional] 
**country_name** | **str** | Please enter your country name | [optional] 

## Example

```python
from openapi_client.models.supermodel_io_logistics_express_address_create_shipment_response import SupermodelIoLogisticsExpressAddressCreateShipmentResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SupermodelIoLogisticsExpressAddressCreateShipmentResponse from a JSON string
supermodel_io_logistics_express_address_create_shipment_response_instance = SupermodelIoLogisticsExpressAddressCreateShipmentResponse.from_json(json)
# print the JSON string representation of the object
print(SupermodelIoLogisticsExpressAddressCreateShipmentResponse.to_json())

# convert the object into a dict
supermodel_io_logistics_express_address_create_shipment_response_dict = supermodel_io_logistics_express_address_create_shipment_response_instance.to_dict()
# create an instance of SupermodelIoLogisticsExpressAddressCreateShipmentResponse from a dict
supermodel_io_logistics_express_address_create_shipment_response_from_dict = SupermodelIoLogisticsExpressAddressCreateShipmentResponse.from_dict(supermodel_io_logistics_express_address_create_shipment_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


