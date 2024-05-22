# SupermodelIoLogisticsExpressRegistrationNumbers

Should your country require registration numbers, such as VAT, EOR etc., please declare it here

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type_code** | **str** | VAT, Value-Added tax&lt;BR&gt;      EIN, Employer Identification Number&lt;BR&gt;      GST, Goods and Service Tax&lt;BR&gt;      SSN, Social Security Number&lt;BR&gt;      EOR, European Union Registration and Identification&lt;BR&gt;      DUN, Data Universal Numberin System&lt;BR&gt;      FED, Federal Tax ID&lt;BR&gt;      STA, State Tax ID&lt;BR&gt;      CNP, Brazil CNPJ/CPF Federal Tax&lt;BR&gt;      IE, Brazil type IE/RG Federal Tax&lt;BR&gt;      INN, Russia bank details section INN&lt;BR&gt;      KPP, Russia bank details section KPP&lt;BR&gt;      OGR, Russia bank details section OGRN&lt;BR&gt;      OKP, Russia bank details sectionOKPO&lt;BR&gt;      SDT, Overseas Registered Supplier or Import One-Stop-Shop or GB VAT (foreign) registration or AUSid GST Registration or VAT on E-Commerce&lt;BR&gt;      FTZ, Free Trade Zone ID&lt;BR&gt;      DAN, Deferment Account Duties Only&lt;BR&gt;      TAN, Deferment Account Tax Only&lt;BR&gt;      DTF, Deferment Account Duties, Taxes and Fees Only&lt;BR&gt;      RGP, EU Registered Exporters registration ID&lt;BR&gt;       DLI,Driver&#39;s License &lt;BR&gt;      NID,National Identity Card&lt;BR&gt;      ,PAS:Passport&lt;BR&gt;      ,MID:Manufacturer ID | [default to 'VAT']
**number** | **str** | Please enter registration number | 
**issuer_country_code** | **str** | Please enter 2 character code of the country where the Registration Number has been issued by | 

## Example

```python
from openapi_client.models.supermodel_io_logistics_express_registration_numbers import SupermodelIoLogisticsExpressRegistrationNumbers

# TODO update the JSON string below
json = "{}"
# create an instance of SupermodelIoLogisticsExpressRegistrationNumbers from a JSON string
supermodel_io_logistics_express_registration_numbers_instance = SupermodelIoLogisticsExpressRegistrationNumbers.from_json(json)
# print the JSON string representation of the object
print(SupermodelIoLogisticsExpressRegistrationNumbers.to_json())

# convert the object into a dict
supermodel_io_logistics_express_registration_numbers_dict = supermodel_io_logistics_express_registration_numbers_instance.to_dict()
# create an instance of SupermodelIoLogisticsExpressRegistrationNumbers from a dict
supermodel_io_logistics_express_registration_numbers_from_dict = SupermodelIoLogisticsExpressRegistrationNumbers.from_dict(supermodel_io_logistics_express_registration_numbers_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


