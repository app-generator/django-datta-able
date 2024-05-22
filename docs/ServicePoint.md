# ServicePoint

Array of the found Service Points. Each Service Point entity contains details about the service point.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The facility ID from GREF database | [optional] 
**facility_id** | **str** | Service Point ID is a unique key with 6 characters, consisting of Service Area for first 3 characters (e.g. BRU) and the last 3 characters is the Facility code (e.g. 001); Service point ID &#x3D; BRU001.  If address is used id not possible to use.   | [optional] 
**facility_type_code** | **str** | The facility type code from GREF database | [optional] 
**service_area_code** | **str** | The service point’s Service Area Code | [optional] 
**service_point_name** | **str** | Name of the service point | [optional] 
**service_point_name_formatted** | **str** | Formatted name of the service point | [optional] 
**local_name** | **str** | The local trading name of the Service Point | [optional] 
**service_point_type** | **str** | The type of the Service Point. CITY, STATION, PARTNER or TWENTYFOURSEVEN. | [optional] 
**address** | [**Address**](Address.md) |  | [optional] 
**geo_location** | [**GeoLocation**](GeoLocation.md) |  | [optional] 
**distance** | **str** | The distance from the search address to this Service Point (beeline).  | [optional] 
**shipping_cut_off_time** | **str** | Time until which a shipment can be handed in at the Service Point, and is still shipped on the same day | [optional] 
**opening_hours** | [**OpeningHours**](OpeningHours.md) |  | [optional] 
**service_point_capabilities** | [**ServicePointCapabilities**](ServicePointCapabilities.md) |  | [optional] 
**contact_details** | [**ContactDetails**](ContactDetails.md) |  | [optional] 
**shipping_cut_off_time_html** | **str** | Obsolete. This is planned to be removed in future releases. | [optional] 
**distance_value** | **str** | Distance of SVP from searched location | [optional] 
**distance_metric** | **float** | Metric of distance | [optional] 
**language** | [**Language**](Language.md) |  | [optional] 
**shipment_limitations** | [**ShipmentLimitations**](ShipmentLimitations.md) |  | [optional] 
**shipment_limitations_by_piece** | [**ShipmentLimitationsByPiece**](ShipmentLimitationsByPiece.md) |  | [optional] 
**charge_code** | **str** | Charge code, e.g. XX | [optional] 
**partner** | [**Partner**](Partner.md) |  | [optional] 
**promotion** | [**Promotion**](Promotion.md) |  | [optional] 
**capacity_status** | [**CapacityStatus**](CapacityStatus.md) |  | [optional] 
**svp_status** | **str** | Status of the service point(Active or Inactive) | [optional] 
**work_week_start** | **int** | Number of day when the work week starts. It starts from 0 to 6(Sunday to Saturday) | [optional] 
**located_at** | **str** |  | [optional] 
**time_zone** | [**DateTimeZone**](DateTimeZone.md) |  | [optional] 

## Example

```python
from openapi_client.models.service_point import ServicePoint

# TODO update the JSON string below
json = "{}"
# create an instance of ServicePoint from a JSON string
service_point_instance = ServicePoint.from_json(json)
# print the JSON string representation of the object
print(ServicePoint.to_json())

# convert the object into a dict
service_point_dict = service_point_instance.to_dict()
# create an instance of ServicePoint from a dict
service_point_from_dict = ServicePoint.from_dict(service_point_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


