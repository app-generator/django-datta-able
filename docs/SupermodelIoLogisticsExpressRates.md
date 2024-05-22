# SupermodelIoLogisticsExpressRates

Comment describing your JSON Schema

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**products** | [**List[ProductsInner1]**](ProductsInner1.md) |  | 
**exchange_rates** | [**List[ExchangeRatesInner]**](ExchangeRatesInner.md) |  | [optional] 
**warnings** | **List[str]** |  | [optional] 

## Example

```python
from openapi_client.models.supermodel_io_logistics_express_rates import SupermodelIoLogisticsExpressRates

# TODO update the JSON string below
json = "{}"
# create an instance of SupermodelIoLogisticsExpressRates from a JSON string
supermodel_io_logistics_express_rates_instance = SupermodelIoLogisticsExpressRates.from_json(json)
# print the JSON string representation of the object
print(SupermodelIoLogisticsExpressRates.to_json())

# convert the object into a dict
supermodel_io_logistics_express_rates_dict = supermodel_io_logistics_express_rates_instance.to_dict()
# create an instance of SupermodelIoLogisticsExpressRates from a dict
supermodel_io_logistics_express_rates_from_dict = SupermodelIoLogisticsExpressRates.from_dict(supermodel_io_logistics_express_rates_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


