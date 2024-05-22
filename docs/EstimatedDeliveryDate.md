# EstimatedDeliveryDate

Estimated delivery date option for QDDF or QDDC.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_requested** | **bool** | Please indicate if requesting to get EDD for this shipment.  Estimated Delivery Date Type. QDDF: is the fastest transit time as quoted to the customer at booking or shipment creation. When clearance or any other non-transport operational component is expected to impact transit time, QDDF does not constitute DHL&#39;s service commitment. QDDC: cconstitutes DHL&#39;s service commitment as quoted at booking or shipment creation. QDDC builds in clearance time, and potentially other special operational non-transport component(s), when relevant. | [default to False]
**type_code** | **str** | Please indicate the EDD type being requested | [optional] 

## Example

```python
from openapi_client.models.estimated_delivery_date import EstimatedDeliveryDate

# TODO update the JSON string below
json = "{}"
# create an instance of EstimatedDeliveryDate from a JSON string
estimated_delivery_date_instance = EstimatedDeliveryDate.from_json(json)
# print the JSON string representation of the object
print(EstimatedDeliveryDate.to_json())

# convert the object into a dict
estimated_delivery_date_dict = estimated_delivery_date_instance.to_dict()
# create an instance of EstimatedDeliveryDate from a dict
estimated_delivery_date_from_dict = EstimatedDeliveryDate.from_dict(estimated_delivery_date_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


