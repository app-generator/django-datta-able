# SupermodelIoLogisticsExpressPackageLabelBarcodesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**position** | **str** | Position of the bespoke barcode | 
**symbology_code** | **str** | Please enter valid Symbology code | 
**content** | **str** | Please enter barcode content | 
**text_below_barcode** | **str** | Please enter text below customer barcode | 

## Example

```python
from openapi_client.models.supermodel_io_logistics_express_package_label_barcodes_inner import SupermodelIoLogisticsExpressPackageLabelBarcodesInner

# TODO update the JSON string below
json = "{}"
# create an instance of SupermodelIoLogisticsExpressPackageLabelBarcodesInner from a JSON string
supermodel_io_logistics_express_package_label_barcodes_inner_instance = SupermodelIoLogisticsExpressPackageLabelBarcodesInner.from_json(json)
# print the JSON string representation of the object
print(SupermodelIoLogisticsExpressPackageLabelBarcodesInner.to_json())

# convert the object into a dict
supermodel_io_logistics_express_package_label_barcodes_inner_dict = supermodel_io_logistics_express_package_label_barcodes_inner_instance.to_dict()
# create an instance of SupermodelIoLogisticsExpressPackageLabelBarcodesInner from a dict
supermodel_io_logistics_express_package_label_barcodes_inner_from_dict = SupermodelIoLogisticsExpressPackageLabelBarcodesInner.from_dict(supermodel_io_logistics_express_package_label_barcodes_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


