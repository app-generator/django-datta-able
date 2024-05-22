# ProductsInner1DeliveryCapabilities


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**delivery_type_code** | **str** | Delivery Date capabilities considering customs clearance days.Estimated Delivery Date Type. QDDF: is the fastest transit time as quoted to the customer at booking or shipment creation. When clearance or any other non-transport operational component is expected to impact transit time, QDDF does not constitute DHL&#39;s service commitment. QDDC: cconstitutes DHL&#39;s service commitment as quoted at booking or shipment creation. QDDC builds in clearance time, and potentially other special operational non-transport component(s), when relevant. | [optional] 
**estimated_delivery_date_and_time** | **str** | This is the estimated date/time the shipment will be delivered by for the rated shipment and product listed | [optional] 
**destination_service_area_code** | **str** | The DHL Service Area Code for the destination of the Shipment | [optional] 
**destination_facility_area_code** | **str** | The DHL Facility Code for the Destination | [optional] 
**delivery_additional_days** | **float** | This is additional transit delays (in days) for shipment delivered to the&lt;BR&gt;                mentioned city or postal area following arrival at the service area. | [optional] 
**delivery_day_of_week** | **float** | Destination day of the week number | [optional] 
**total_transit_days** | **float** | The number of transit days | [optional] 

## Example

```python
from openapi_client.models.products_inner1_delivery_capabilities import ProductsInner1DeliveryCapabilities

# TODO update the JSON string below
json = "{}"
# create an instance of ProductsInner1DeliveryCapabilities from a JSON string
products_inner1_delivery_capabilities_instance = ProductsInner1DeliveryCapabilities.from_json(json)
# print the JSON string representation of the object
print(ProductsInner1DeliveryCapabilities.to_json())

# convert the object into a dict
products_inner1_delivery_capabilities_dict = products_inner1_delivery_capabilities_instance.to_dict()
# create an instance of ProductsInner1DeliveryCapabilities from a dict
products_inner1_delivery_capabilities_from_dict = ProductsInner1DeliveryCapabilities.from_dict(products_inner1_delivery_capabilities_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


