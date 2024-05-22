# ShipmentLimitationsByPiece

Shipment Piece Limitations in this Service Point.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**piece_size_limit1** | [**ValueUnit**](ValueUnit.md) |  | [optional] 
**piece_size_limit2** | [**ValueUnit**](ValueUnit.md) |  | [optional] 
**piece_size_limit3** | [**ValueUnit**](ValueUnit.md) |  | [optional] 
**max_piece_weight** | [**ValueUnit**](ValueUnit.md) |  | [optional] 
**html** | **str** | Obsolete. This is planned to be removed in future releases. | [optional] 

## Example

```python
from openapi_client.models.shipment_limitations_by_piece import ShipmentLimitationsByPiece

# TODO update the JSON string below
json = "{}"
# create an instance of ShipmentLimitationsByPiece from a JSON string
shipment_limitations_by_piece_instance = ShipmentLimitationsByPiece.from_json(json)
# print the JSON string representation of the object
print(ShipmentLimitationsByPiece.to_json())

# convert the object into a dict
shipment_limitations_by_piece_dict = shipment_limitations_by_piece_instance.to_dict()
# create an instance of ShipmentLimitationsByPiece from a dict
shipment_limitations_by_piece_from_dict = ShipmentLimitationsByPiece.from_dict(shipment_limitations_by_piece_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


