# SupermodelIoLogisticsExpressPackageReference

Package Reference model description

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | **str** | Please provide reference | 
**type_code** | **str** | Please provide reference type&lt;BR&gt;      &lt;BR&gt;      AAO, shipment reference number of receiver&lt;BR&gt;      CU, reference number of consignor - default&lt;BR&gt;      FF, reference number of freight forwarder&lt;BR&gt;      FN, freight bill number for &lt;ex works invoice number&gt;&lt;BR&gt;      IBC, inbound center reference number&lt;BR&gt;      LLR, load list reference for &lt;10-digit Shipment ID&gt;&lt;BR&gt;      OBC, outbound center reference number for &lt;SHIPMEN IDENTIFIER (COUNTRY OF ORIGIN)&gt;&lt;BR&gt;      PRN, pickup request number for &lt;BOOKINGREFERENCE NUMBER&gt;&lt;BR&gt;      ACP, local payer account number&lt;BR&gt;      ACS, local shipper account number&lt;BR&gt;      ACR, local receiver account number&lt;BR&gt;      CDN, customs declaration number&lt;BR&gt;      STD, eurolog 15-digit shipment id&lt;BR&gt;      CO, buyers order number   | [optional] [default to 'CU']

## Example

```python
from openapi_client.models.supermodel_io_logistics_express_package_reference import SupermodelIoLogisticsExpressPackageReference

# TODO update the JSON string below
json = "{}"
# create an instance of SupermodelIoLogisticsExpressPackageReference from a JSON string
supermodel_io_logistics_express_package_reference_instance = SupermodelIoLogisticsExpressPackageReference.from_json(json)
# print the JSON string representation of the object
print(SupermodelIoLogisticsExpressPackageReference.to_json())

# convert the object into a dict
supermodel_io_logistics_express_package_reference_dict = supermodel_io_logistics_express_package_reference_instance.to_dict()
# create an instance of SupermodelIoLogisticsExpressPackageReference from a dict
supermodel_io_logistics_express_package_reference_from_dict = SupermodelIoLogisticsExpressPackageReference.from_dict(supermodel_io_logistics_express_package_reference_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


