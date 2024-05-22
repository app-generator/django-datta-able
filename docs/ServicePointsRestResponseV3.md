# ServicePointsRestResponseV3


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | [**RestResponseStatus**](RestResponseStatus.md) |  | [optional] 
**search_address** | **str** | The address used for the search (value of request parameter &#39;address&#39;) | [optional] 
**search_location** | [**GeoLocation**](GeoLocation.md) |  | [optional] 
**map_culture** | **str** | The culture parameter for Bing Maps API (derived from the country parameter in the request) | [optional] 
**map_language** | **str** | Map Culture Used for Third party Maps | [optional] 
**service_points** | [**List[ServicePoint]**](ServicePoint.md) | Array of the found Service Points. Each Service Point entity contains details about the service point. | [optional] 
**messages** | **List[str]** | Array of strings. Contains information messages  - e.g. required language is not available, result was filtered due to incoming holidays. | [optional] 
**translations** | [**Translations**](Translations.md) |  | [optional] 
**lite_mode** | **bool** | Indicates whether lite mode is acitvated or not. | [optional] 
**promotion** | [**Promotion**](Promotion.md) |  | [optional] 

## Example

```python
from openapi_client.models.service_points_rest_response_v3 import ServicePointsRestResponseV3

# TODO update the JSON string below
json = "{}"
# create an instance of ServicePointsRestResponseV3 from a JSON string
service_points_rest_response_v3_instance = ServicePointsRestResponseV3.from_json(json)
# print the JSON string representation of the object
print(ServicePointsRestResponseV3.to_json())

# convert the object into a dict
service_points_rest_response_v3_dict = service_points_rest_response_v3_instance.to_dict()
# create an instance of ServicePointsRestResponseV3 from a dict
service_points_rest_response_v3_from_dict = ServicePointsRestResponseV3.from_dict(service_points_rest_response_v3_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


