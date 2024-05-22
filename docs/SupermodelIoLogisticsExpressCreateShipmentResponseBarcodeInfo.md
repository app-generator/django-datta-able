# SupermodelIoLogisticsExpressCreateShipmentResponseBarcodeInfo

Here you can find barcode details in base64

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**shipment_identification_number_barcode_content** | **str** | Barcode base64 encoded airwaybill number | [optional] 
**origin_destination_service_type_barcode_content** | **str** | Barcode base64 image of origin service area code, destination service area code and global product code | [optional] 
**routing_barcode_content** | **str** | Barcode base64 image of DHL routing code | [optional] 
**tracking_number_barcodes** | [**List[SupermodelIoLogisticsExpressCreateShipmentResponseBarcodeInfoTrackingNumberBarcodesInner]**](SupermodelIoLogisticsExpressCreateShipmentResponseBarcodeInfoTrackingNumberBarcodesInner.md) | Here you can find barcode details for each piece | [optional] 

## Example

```python
from openapi_client.models.supermodel_io_logistics_express_create_shipment_response_barcode_info import SupermodelIoLogisticsExpressCreateShipmentResponseBarcodeInfo

# TODO update the JSON string below
json = "{}"
# create an instance of SupermodelIoLogisticsExpressCreateShipmentResponseBarcodeInfo from a JSON string
supermodel_io_logistics_express_create_shipment_response_barcode_info_instance = SupermodelIoLogisticsExpressCreateShipmentResponseBarcodeInfo.from_json(json)
# print the JSON string representation of the object
print(SupermodelIoLogisticsExpressCreateShipmentResponseBarcodeInfo.to_json())

# convert the object into a dict
supermodel_io_logistics_express_create_shipment_response_barcode_info_dict = supermodel_io_logistics_express_create_shipment_response_barcode_info_instance.to_dict()
# create an instance of SupermodelIoLogisticsExpressCreateShipmentResponseBarcodeInfo from a dict
supermodel_io_logistics_express_create_shipment_response_barcode_info_from_dict = SupermodelIoLogisticsExpressCreateShipmentResponseBarcodeInfo.from_dict(supermodel_io_logistics_express_create_shipment_response_barcode_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


