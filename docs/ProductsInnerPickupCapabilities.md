# ProductsInnerPickupCapabilities


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**next_business_day** | **bool** | This indicator has values of Y or N, and tells the consumer if the service in the response has a pickup date on the same day as the requested shipment date (per the request). | [optional] 
**local_cutoff_date_and_time** | **str** | This is the cutoff time for the service&lt;BR&gt;                offered in the response. This represents the latest time (local to origin) which the shipment can be tendered to the courier for that service on that day. | [optional] 
**gmt_cutoff_time** | **str** | Pickup cut off time in GMT | [optional] 
**pickup_earliest** | **str** | The DHL earliest time possible for pickup | [optional] 
**pickup_latest** | **str** | The DHL latest time possible for pickup | [optional] 
**origin_service_area_code** | **str** | The DHL Service Area Code for the origin of the Shipment | [optional] 
**origin_facility_area_code** | **str** | The DHL Facility Code for the Origin | [optional] 
**pickup_additional_days** | **float** | This is additional transit delays (in days) for shipment picked up from the mentioned city or postal area to arrival at the service area. | [optional] 
**pickup_day_of_week** | **float** | Pickup day of the week number | [optional] 

## Example

```python
from openapi_client.models.products_inner_pickup_capabilities import ProductsInnerPickupCapabilities

# TODO update the JSON string below
json = "{}"
# create an instance of ProductsInnerPickupCapabilities from a JSON string
products_inner_pickup_capabilities_instance = ProductsInnerPickupCapabilities.from_json(json)
# print the JSON string representation of the object
print(ProductsInnerPickupCapabilities.to_json())

# convert the object into a dict
products_inner_pickup_capabilities_dict = products_inner_pickup_capabilities_instance.to_dict()
# create an instance of ProductsInnerPickupCapabilities from a dict
products_inner_pickup_capabilities_from_dict = ProductsInnerPickupCapabilities.from_dict(products_inner_pickup_capabilities_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


