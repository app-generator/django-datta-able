# SupermodelIoLogisticsExpressPackage

Package definition for /shipments

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type_code** | **str** | Please contact your DHL Express representative if you wish to use a DHL specific package otherwise ignore this element. | [optional] 
**weight** | **float** | The weight of the package. | 
**dimensions** | [**Dimensions**](Dimensions.md) |  | 
**customer_references** | [**List[SupermodelIoLogisticsExpressPackageReference]**](SupermodelIoLogisticsExpressPackageReference.md) | Here you can declare your customer references for each package | [optional] 
**identifiers** | [**List[SupermodelIoLogisticsExpressIdentifier]**](SupermodelIoLogisticsExpressIdentifier.md) | Identifiers section is on the package level where you can optionaly provide a DHL Express waybill number. This has to be enabled by your DHL Express IT contact. | [optional] 
**description** | **str** | Please enter description of content for each package | [optional] 
**label_barcodes** | [**List[SupermodelIoLogisticsExpressPackageLabelBarcodesInner]**](SupermodelIoLogisticsExpressPackageLabelBarcodesInner.md) | This allows you to define up to two bespoke barcodes on the DHL Express Tranport label. To use this feature please set outputImageProperties/imageOptions/templateName as ECOM26_84CI_003 for typeCode&#x3D;label | [optional] 
**label_text** | [**List[SupermodelIoLogisticsExpressPackageLabelTextInner]**](SupermodelIoLogisticsExpressPackageLabelTextInner.md) | This allows you to enter up to two bespoke texts on the DHL Express Tranport label. To use this feature please set outputImageProperties/imageOptions/templateName as ECOM26_84CI_003 for typeCode&#x3D;label | [optional] 
**label_description** | **str** | Please enter additional customer description | [optional] 
**reference_number** | **float** | Please enter package reference number. If package reference number is provided for at least one package, then package reference number must be provided for all packages. | [optional] 

## Example

```python
from openapi_client.models.supermodel_io_logistics_express_package import SupermodelIoLogisticsExpressPackage

# TODO update the JSON string below
json = "{}"
# create an instance of SupermodelIoLogisticsExpressPackage from a JSON string
supermodel_io_logistics_express_package_instance = SupermodelIoLogisticsExpressPackage.from_json(json)
# print the JSON string representation of the object
print(SupermodelIoLogisticsExpressPackage.to_json())

# convert the object into a dict
supermodel_io_logistics_express_package_dict = supermodel_io_logistics_express_package_instance.to_dict()
# create an instance of SupermodelIoLogisticsExpressPackage from a dict
supermodel_io_logistics_express_package_from_dict = SupermodelIoLogisticsExpressPackage.from_dict(supermodel_io_logistics_express_package_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


