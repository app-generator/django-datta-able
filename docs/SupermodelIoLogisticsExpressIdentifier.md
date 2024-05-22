# SupermodelIoLogisticsExpressIdentifier


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type_code** | **str** | Please provide type of the identifier you want to set value for | 
**value** | **str** | Please enter value of your identifier (WB number, PieceID) | 
**data_identifier** | **str** | Please enter value of Piece Data Identifier. Note: Piece identification data should be same for all the pieces provided in single shipment. | [optional] 

## Example

```python
from openapi_client.models.supermodel_io_logistics_express_identifier import SupermodelIoLogisticsExpressIdentifier

# TODO update the JSON string below
json = "{}"
# create an instance of SupermodelIoLogisticsExpressIdentifier from a JSON string
supermodel_io_logistics_express_identifier_instance = SupermodelIoLogisticsExpressIdentifier.from_json(json)
# print the JSON string representation of the object
print(SupermodelIoLogisticsExpressIdentifier.to_json())

# convert the object into a dict
supermodel_io_logistics_express_identifier_dict = supermodel_io_logistics_express_identifier_instance.to_dict()
# create an instance of SupermodelIoLogisticsExpressIdentifier from a dict
supermodel_io_logistics_express_identifier_from_dict = SupermodelIoLogisticsExpressIdentifier.from_dict(supermodel_io_logistics_express_identifier_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


