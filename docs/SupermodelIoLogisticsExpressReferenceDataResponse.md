# SupermodelIoLogisticsExpressReferenceDataResponse

MyDHL API REST ReferenceData response JSON Schema

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**reference_data** | [**List[SupermodelIoLogisticsExpressReferenceData]**](SupermodelIoLogisticsExpressReferenceData.md) | The result of search from provided reference criteria | [optional] 
**warnings** | **List[str]** |  | [optional] 

## Example

```python
from openapi_client.models.supermodel_io_logistics_express_reference_data_response import SupermodelIoLogisticsExpressReferenceDataResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SupermodelIoLogisticsExpressReferenceDataResponse from a JSON string
supermodel_io_logistics_express_reference_data_response_instance = SupermodelIoLogisticsExpressReferenceDataResponse.from_json(json)
# print the JSON string representation of the object
print(SupermodelIoLogisticsExpressReferenceDataResponse.to_json())

# convert the object into a dict
supermodel_io_logistics_express_reference_data_response_dict = supermodel_io_logistics_express_reference_data_response_instance.to_dict()
# create an instance of SupermodelIoLogisticsExpressReferenceDataResponse from a dict
supermodel_io_logistics_express_reference_data_response_from_dict = SupermodelIoLogisticsExpressReferenceDataResponse.from_dict(supermodel_io_logistics_express_reference_data_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


