# SupermodelIoLogisticsExpressCreateShipmentRequestGetAdditionalInformationInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type_code** | **str** | Provide type code of data that can be returned in response.  Values can be pickupDetails, optionalShipmentData, transliterateResponse and linkLabelsByPieces (link label image generated for each package level) | [optional] 
**is_requested** | **bool** |  | 

## Example

```python
from openapi_client.models.supermodel_io_logistics_express_create_shipment_request_get_additional_information_inner import SupermodelIoLogisticsExpressCreateShipmentRequestGetAdditionalInformationInner

# TODO update the JSON string below
json = "{}"
# create an instance of SupermodelIoLogisticsExpressCreateShipmentRequestGetAdditionalInformationInner from a JSON string
supermodel_io_logistics_express_create_shipment_request_get_additional_information_inner_instance = SupermodelIoLogisticsExpressCreateShipmentRequestGetAdditionalInformationInner.from_json(json)
# print the JSON string representation of the object
print(SupermodelIoLogisticsExpressCreateShipmentRequestGetAdditionalInformationInner.to_json())

# convert the object into a dict
supermodel_io_logistics_express_create_shipment_request_get_additional_information_inner_dict = supermodel_io_logistics_express_create_shipment_request_get_additional_information_inner_instance.to_dict()
# create an instance of SupermodelIoLogisticsExpressCreateShipmentRequestGetAdditionalInformationInner from a dict
supermodel_io_logistics_express_create_shipment_request_get_additional_information_inner_from_dict = SupermodelIoLogisticsExpressCreateShipmentRequestGetAdditionalInformationInner.from_dict(supermodel_io_logistics_express_create_shipment_request_get_additional_information_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


