# ShipmentLimitations

Information about shipment piece / size

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**max_number_of_pieces** | [**ValueUnit**](ValueUnit.md) |  | [optional] 
**max_shipment_weight** | [**ValueUnit**](ValueUnit.md) |  | [optional] 
**html** | **str** | Obsolete. This is planned to be removed in future releases. | [optional] 

## Example

```python
from openapi_client.models.shipment_limitations import ShipmentLimitations

# TODO update the JSON string below
json = "{}"
# create an instance of ShipmentLimitations from a JSON string
shipment_limitations_instance = ShipmentLimitations.from_json(json)
# print the JSON string representation of the object
print(ShipmentLimitations.to_json())

# convert the object into a dict
shipment_limitations_dict = shipment_limitations_instance.to_dict()
# create an instance of ShipmentLimitations from a dict
shipment_limitations_from_dict = ShipmentLimitations.from_dict(shipment_limitations_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


