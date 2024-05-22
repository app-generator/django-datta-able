# SupermodelIoLogisticsExpressRateRequestProductsAndServicesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**product_code** | **str** | Please enter DHL Express Global Product code | 
**local_product_code** | **str** | Please enter DHL Express Local Product code | [optional] 
**value_added_services** | [**List[SupermodelIoLogisticsExpressValueAddedServicesRates]**](SupermodelIoLogisticsExpressValueAddedServicesRates.md) | Please use if you wish to filter the response by value added services | [optional] 

## Example

```python
from openapi_client.models.supermodel_io_logistics_express_rate_request_products_and_services_inner import SupermodelIoLogisticsExpressRateRequestProductsAndServicesInner

# TODO update the JSON string below
json = "{}"
# create an instance of SupermodelIoLogisticsExpressRateRequestProductsAndServicesInner from a JSON string
supermodel_io_logistics_express_rate_request_products_and_services_inner_instance = SupermodelIoLogisticsExpressRateRequestProductsAndServicesInner.from_json(json)
# print the JSON string representation of the object
print(SupermodelIoLogisticsExpressRateRequestProductsAndServicesInner.to_json())

# convert the object into a dict
supermodel_io_logistics_express_rate_request_products_and_services_inner_dict = supermodel_io_logistics_express_rate_request_products_and_services_inner_instance.to_dict()
# create an instance of SupermodelIoLogisticsExpressRateRequestProductsAndServicesInner from a dict
supermodel_io_logistics_express_rate_request_products_and_services_inner_from_dict = SupermodelIoLogisticsExpressRateRequestProductsAndServicesInner.from_dict(supermodel_io_logistics_express_rate_request_products_and_services_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


