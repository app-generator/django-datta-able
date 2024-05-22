# ExchangeRatesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**current_exchange_rate** | **float** | Rate of the currency exchange | 
**currency** | **str** | The currency code | 
**base_currency** | **str** | The currency code of the base currency is either USD or EUR | 

## Example

```python
from openapi_client.models.exchange_rates_inner import ExchangeRatesInner

# TODO update the JSON string below
json = "{}"
# create an instance of ExchangeRatesInner from a JSON string
exchange_rates_inner_instance = ExchangeRatesInner.from_json(json)
# print the JSON string representation of the object
print(ExchangeRatesInner.to_json())

# convert the object into a dict
exchange_rates_inner_dict = exchange_rates_inner_instance.to_dict()
# create an instance of ExchangeRatesInner from a dict
exchange_rates_inner_from_dict = ExchangeRatesInner.from_dict(exchange_rates_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


