# SupermodelIoLogisticsExpressValueAddedServicesRates


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**service_code** | **str** | Please enter DHL Express value added global service code. For detailed list of all available service codes for your prospect shipment please invoke /products or /rates | 
**local_service_code** | **str** | Please enter DHL Express value added local service code. For detailed list of all available service codes for your prospect shipment please invoke /products or /rates | [optional] 
**value** | **float** | Please enter monetary value of service (e.g. Insured Value) | [optional] 
**currency** | **str** | Please enter currency code (e.g. Insured Value currency code) | [optional] 
**method** | **str** | For future use | [optional] 

## Example

```python
from openapi_client.models.supermodel_io_logistics_express_value_added_services_rates import SupermodelIoLogisticsExpressValueAddedServicesRates

# TODO update the JSON string below
json = "{}"
# create an instance of SupermodelIoLogisticsExpressValueAddedServicesRates from a JSON string
supermodel_io_logistics_express_value_added_services_rates_instance = SupermodelIoLogisticsExpressValueAddedServicesRates.from_json(json)
# print the JSON string representation of the object
print(SupermodelIoLogisticsExpressValueAddedServicesRates.to_json())

# convert the object into a dict
supermodel_io_logistics_express_value_added_services_rates_dict = supermodel_io_logistics_express_value_added_services_rates_instance.to_dict()
# create an instance of SupermodelIoLogisticsExpressValueAddedServicesRates from a dict
supermodel_io_logistics_express_value_added_services_rates_from_dict = SupermodelIoLogisticsExpressValueAddedServicesRates.from_dict(supermodel_io_logistics_express_value_added_services_rates_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


