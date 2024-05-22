# SupermodelIoLogisticsExpressRateRequestCustomerDetails


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**shipper_details** | [**SupermodelIoLogisticsExpressAddressRatesRequest**](SupermodelIoLogisticsExpressAddressRatesRequest.md) |  | 
**receiver_details** | [**SupermodelIoLogisticsExpressAddressRatesRequest**](SupermodelIoLogisticsExpressAddressRatesRequest.md) |  | 

## Example

```python
from openapi_client.models.supermodel_io_logistics_express_rate_request_customer_details import SupermodelIoLogisticsExpressRateRequestCustomerDetails

# TODO update the JSON string below
json = "{}"
# create an instance of SupermodelIoLogisticsExpressRateRequestCustomerDetails from a JSON string
supermodel_io_logistics_express_rate_request_customer_details_instance = SupermodelIoLogisticsExpressRateRequestCustomerDetails.from_json(json)
# print the JSON string representation of the object
print(SupermodelIoLogisticsExpressRateRequestCustomerDetails.to_json())

# convert the object into a dict
supermodel_io_logistics_express_rate_request_customer_details_dict = supermodel_io_logistics_express_rate_request_customer_details_instance.to_dict()
# create an instance of SupermodelIoLogisticsExpressRateRequestCustomerDetails from a dict
supermodel_io_logistics_express_rate_request_customer_details_from_dict = SupermodelIoLogisticsExpressRateRequestCustomerDetails.from_dict(supermodel_io_logistics_express_rate_request_customer_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


