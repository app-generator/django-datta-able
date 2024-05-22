# Weight1


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**volumetric** | **float** | The dimensional weight of the shipment | [optional] 
**provided** | **float** | The quoted weight of the shipment | [optional] 
**unit_of_measurement** | **str** | The unit of measurement for the dimensions of the package. | [optional] 

## Example

```python
from openapi_client.models.weight1 import Weight1

# TODO update the JSON string below
json = "{}"
# create an instance of Weight1 from a JSON string
weight1_instance = Weight1.from_json(json)
# print the JSON string representation of the object
print(Weight1.to_json())

# convert the object into a dict
weight1_dict = weight1_instance.to_dict()
# create an instance of Weight1 from a dict
weight1_from_dict = Weight1.from_dict(weight1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


