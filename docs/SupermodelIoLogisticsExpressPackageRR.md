# SupermodelIoLogisticsExpressPackageRR

Package defintion for rating related services

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type_code** | **str** | Please contact your DHL Express representative if you wish to use a DHL specific package otherwise ignore this element. | [optional] 
**weight** | **float** | The weight of the package. | 
**dimensions** | [**Dimensions1**](Dimensions1.md) |  | 

## Example

```python
from openapi_client.models.supermodel_io_logistics_express_package_rr import SupermodelIoLogisticsExpressPackageRR

# TODO update the JSON string below
json = "{}"
# create an instance of SupermodelIoLogisticsExpressPackageRR from a JSON string
supermodel_io_logistics_express_package_rr_instance = SupermodelIoLogisticsExpressPackageRR.from_json(json)
# print the JSON string representation of the object
print(SupermodelIoLogisticsExpressPackageRR.to_json())

# convert the object into a dict
supermodel_io_logistics_express_package_rr_dict = supermodel_io_logistics_express_package_rr_instance.to_dict()
# create an instance of SupermodelIoLogisticsExpressPackageRR from a dict
supermodel_io_logistics_express_package_rr_from_dict = SupermodelIoLogisticsExpressPackageRR.from_dict(supermodel_io_logistics_express_package_rr_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


