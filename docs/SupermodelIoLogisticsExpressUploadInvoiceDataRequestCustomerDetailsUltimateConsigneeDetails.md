# SupermodelIoLogisticsExpressUploadInvoiceDataRequestCustomerDetailsUltimateConsigneeDetails

Please enter address and contact details related to ultimate consignee

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**postal_address** | [**SupermodelIoLogisticsExpressAddress**](SupermodelIoLogisticsExpressAddress.md) |  | 
**contact_information** | [**SupermodelIoLogisticsExpressContact**](SupermodelIoLogisticsExpressContact.md) |  | 
**type_code** | **str** | Please enter the business party type of the ultimate consignee | [optional] 
**registration_numbers** | [**List[SupermodelIoLogisticsExpressRegistrationNumbers]**](SupermodelIoLogisticsExpressRegistrationNumbers.md) |  | [optional] 

## Example

```python
from openapi_client.models.supermodel_io_logistics_express_upload_invoice_data_request_customer_details_ultimate_consignee_details import SupermodelIoLogisticsExpressUploadInvoiceDataRequestCustomerDetailsUltimateConsigneeDetails

# TODO update the JSON string below
json = "{}"
# create an instance of SupermodelIoLogisticsExpressUploadInvoiceDataRequestCustomerDetailsUltimateConsigneeDetails from a JSON string
supermodel_io_logistics_express_upload_invoice_data_request_customer_details_ultimate_consignee_details_instance = SupermodelIoLogisticsExpressUploadInvoiceDataRequestCustomerDetailsUltimateConsigneeDetails.from_json(json)
# print the JSON string representation of the object
print(SupermodelIoLogisticsExpressUploadInvoiceDataRequestCustomerDetailsUltimateConsigneeDetails.to_json())

# convert the object into a dict
supermodel_io_logistics_express_upload_invoice_data_request_customer_details_ultimate_consignee_details_dict = supermodel_io_logistics_express_upload_invoice_data_request_customer_details_ultimate_consignee_details_instance.to_dict()
# create an instance of SupermodelIoLogisticsExpressUploadInvoiceDataRequestCustomerDetailsUltimateConsigneeDetails from a dict
supermodel_io_logistics_express_upload_invoice_data_request_customer_details_ultimate_consignee_details_from_dict = SupermodelIoLogisticsExpressUploadInvoiceDataRequestCustomerDetailsUltimateConsigneeDetails.from_dict(supermodel_io_logistics_express_upload_invoice_data_request_customer_details_ultimate_consignee_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


