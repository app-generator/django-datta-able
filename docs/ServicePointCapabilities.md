# ServicePointCapabilities

An entity that lists all capabilities of a Service Point.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**parking_available** | **bool** | Indicates whether parking facility is available in the service point or not | [optional] 
**disabled_access** | **bool** | Indicates whether disabled access is available in the service point or not | [optional] 
**shipment_drop_off** | **bool** | Indicates whether Shipment Drop Off is available in the service point or not | [optional] 
**shipment_collection** | **bool** | Indicates whether Shipment Collection is available in the service point or not | [optional] 
**international_shipping** | **bool** | Indicates whether International Shipping is available in the service point or not | [optional] 
**domestic_shipping** | **bool** | Indicates whether Domestic Shipping is available in the service point or not | [optional] 
**account_shippers** | **bool** | Indicates whether Account Shipping is available in the service point or not | [optional] 
**label_printing** | **bool** | Indicates whether Label Printing is available in the service point or not | [optional] 
**insurance** | **bool** | Indicates whether Insurance facility is available in the service point or not | [optional] 
**import_charges** | **bool** | Indicates whether Import Charges is applicable in the service point or not | [optional] 
**packaging** | **bool** | Indicates whether Packaging facility is available in the service point or not | [optional] 
**receiver_paid** | **bool** | Indicates whether Receiver Paying option is available in the service point or not | [optional] 
**visa_program** | **bool** | Indicates whether VISA program is applicable in the service point or not | [optional] 
**pay_with_cash** | **bool** | Indicates whether pay by cash option is available in the service point or not | [optional] 
**pay_with_credit_card** | **bool** | Indicates whether pay with credit card option is available in the service point or not | [optional] 
**pay_with_cheque** | **bool** | Indicates whether pay with cheque option is available in the service point or not | [optional] 
**pay_with_mobile** | **bool** | Indicates whether pay with mobile option is available in the service point or not | [optional] 
**pay_with_pay_pal** | **bool** | Indicates whether pay with paypal option is available in the service point or not | [optional] 
**parking_title** | **str** | Title for the parking icon | [optional] 
**disabled_access_title** | **str** | Title for the disable wheel chair icon | [optional] 
**piece_weight_limit** | **float** | Piece Weight Limit | [optional] 
**piece_weight_limit_unit** | **str** | Enumeration (KG or LB) | [optional] 
**piece_dimensions_limit** | [**Dimensions**](Dimensions.md) |  | [optional] 
**piece_dimensions_limit_unit** | **str** | Enumeration (CM or IN) | [optional] 
**piece_count_limit** | **float** | Number (integer) | [optional] 
**account_prepaid_shippers** | **bool** | Account prepaid shippers | [optional] 
**prepaid_shippers** | **bool** | Prepaid shippers | [optional] 
**pre_print_return_label** | **bool** | Pre-printed return label | [optional] 
**label_free** | **bool** | Indicates whether this particular service point can handle label free shipments or not | [optional] 
**ppc_list** | **List[str]** | PPC list. | [optional] 
**html** | **str** | Obsolete. This is planned to be removed in future releases. | [optional] 
**capability_codes** | **str** | PPC codes available for this service point | [optional] 

## Example

```python
from openapi_client.models.service_point_capabilities import ServicePointCapabilities

# TODO update the JSON string below
json = "{}"
# create an instance of ServicePointCapabilities from a JSON string
service_point_capabilities_instance = ServicePointCapabilities.from_json(json)
# print the JSON string representation of the object
print(ServicePointCapabilities.to_json())

# convert the object into a dict
service_point_capabilities_dict = service_point_capabilities_instance.to_dict()
# create an instance of ServicePointCapabilities from a dict
service_point_capabilities_from_dict = ServicePointCapabilities.from_dict(service_point_capabilities_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


