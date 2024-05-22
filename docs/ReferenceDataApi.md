# openapi_client.ReferenceDataApi

All URIs are relative to *https://api-mock.dhl.com/mydhlapi*

Method | HTTP request | Description
------------- | ------------- | -------------
[**exp_api_reference_data**](ReferenceDataApi.md#exp_api_reference_data) | **GET** /reference-data | provide reference data currently used for MyDHL API services usage.


# **exp_api_reference_data**
> SupermodelIoLogisticsExpressReferenceDataResponse exp_api_reference_data(dataset_name, filter_by_value=filter_by_value, filter_by_attribute=filter_by_attribute, comparison_operator=comparison_operator, query_string=query_string, message_reference=message_reference, message_reference_date=message_reference_date, plugin_name=plugin_name, plugin_version=plugin_version, shipping_system_platform_name=shipping_system_platform_name, shipping_system_platform_version=shipping_system_platform_version, webstore_platform_name=webstore_platform_name, webstore_platform_version=webstore_platform_version)

provide reference data currently used for MyDHL API services usage.

The reference data service retrieves the reference data used for MyDHL API shipment or upload invoice data service. 

### Example

* Api Key Authentication (apiKey):
* Basic Authentication (basicAuth):

```python
import openapi_client
from openapi_client.models.supermodel_io_logistics_express_reference_data_response import SupermodelIoLogisticsExpressReferenceDataResponse
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api-mock.dhl.com/mydhlapi
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api-mock.dhl.com/mydhlapi"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiKey
configuration.api_key['apiKey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKey'] = 'Bearer'

# Configure HTTP basic authorization: basicAuth
configuration = openapi_client.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.ReferenceDataApi(api_client)
    dataset_name = 'country' # str | Must provide at least one datasetName value. If providing just the datasetName with no filterBy fields - the response will return the entire data set from the dataset table (bulk).
    filter_by_value = 'MY' # str | Use filter by value to query based on the specific string for optimized search.<br> <br> List of supported filterByValue per dataset (eg. dataset: filterByAttribute| supported filterByValue) <br><br> a) returnStatusMessage: serviceName|CreateShipment,DocumentImageRequest,RateRequest,RequestIdentifier,RequestPickup,AddressValidateRequest,TrackingRequest,UpdatePickup,UpdateShipment,UploadInvoiceData,DeleteShipment,DocumentRetrieve-ePOD <br> b) returnStatusMessage: operationName|get-image,identifiers,address-validate,    RouteRequest, shipments, tracking, upload-image,landed-cost,rates,upload-invoice-data,pickup,proof-of-delivery <br> c) returnStatusMessage: protocol|REST,SOAP,XMLPI <br> d) productCode: docNonDocIndicator|Y,N (optional)
    filter_by_attribute = 'countryCode' # str | Use filter by attribute to define the list of supported attibuted for the specified datasetName. <br> List of supported attributes per dataset <br> (eg. dataset: supported filterByAttributes values) <br><br> a) country: countryCode, countryName <br> b) countryPostalcodeFormat: countryCode <br> c) dangerousGoods: serviceCode <br> d) incoterm: incoterm <br> e) productCode: productCode, countryCode, docNonDocIndicator <br> f) serviceCode: serviceCode, countryCode, chargeCodeTypeCode, serviceGroupDescription <br> g) packageTypeCode: packageTypeCode <br> h) documentTypeCode: customsDocumentTypeCode <br> i) customerShipmentReferenceType: shipmentReferenceTypeCode <br> j) customerPackageReferenceType: packageReferenceTypeCode <br> k) invoiceReferenceType: invoiceReferenceTypeCode <br> l) invoiceItemReferenceType: itemReferenceTypeCode <br> m) registrationNumberTypeCode: registrationTypeCode <br> n) commodityCategory: commodityCategoryCode, commodityCategoryGroup, commodityCategoryDescription <br> o) returnStatusMessage: statusCode, serviceName, operationName, protocol <br> p) trackingEventCode: eventTypeCode, eventTypeDescription, visibleToCustomer <br> q) unitOfMeasurement: unitOfMeasurement (optional)
    comparison_operator = 'equal' # str | Use comparison operator to define the specific match condition for optimized search. (optional) (default to 'equal')
    query_string = 'queryString=operationName:shipment:equal' # str | Use queryString for additional filter criteria in format of '[attribute]:[value]:[comparisonOperator]'. <br> All additional filters are applied together with logical connector 'AND'. <br> Maximum of three additional attribute-value-comparisonOperator combinations. <br> Multiple queryString parameters will be separated  by comma \",\" separator (optional)
    message_reference = 'd0e7832e-5c98-11ea-bc55-0242ac13' # str | Please provide message reference  (optional)
    message_reference_date = 'Wed, 21 Oct 2015 07:28:00 GMT' # str | Optional reference date in the  HTTP-date format https://tools.ietf.org/html/rfc7231#section-7.1.1.2 (optional)
    plugin_name = ' ' # str | Please provide name of the plugin (applicable to 3PV only)  (optional)
    plugin_version = ' ' # str | Please provide version of the plugin (applicable to 3PV only)  (optional)
    shipping_system_platform_name = ' ' # str | Please provide name of the shipping platform(applicable to 3PV only)  (optional)
    shipping_system_platform_version = ' ' # str | Please provide version of the shipping platform (applicable to 3PV only)  (optional)
    webstore_platform_name = ' ' # str | Please provide name of the webstore platform (applicable to 3PV only)  (optional)
    webstore_platform_version = ' ' # str | Please provide version of the webstore platform (applicable to 3PV only)  (optional)

    try:
        # provide reference data currently used for MyDHL API services usage.
        api_response = api_instance.exp_api_reference_data(dataset_name, filter_by_value=filter_by_value, filter_by_attribute=filter_by_attribute, comparison_operator=comparison_operator, query_string=query_string, message_reference=message_reference, message_reference_date=message_reference_date, plugin_name=plugin_name, plugin_version=plugin_version, shipping_system_platform_name=shipping_system_platform_name, shipping_system_platform_version=shipping_system_platform_version, webstore_platform_name=webstore_platform_name, webstore_platform_version=webstore_platform_version)
        print("The response of ReferenceDataApi->exp_api_reference_data:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReferenceDataApi->exp_api_reference_data: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dataset_name** | **str**| Must provide at least one datasetName value. If providing just the datasetName with no filterBy fields - the response will return the entire data set from the dataset table (bulk). | 
 **filter_by_value** | **str**| Use filter by value to query based on the specific string for optimized search.&lt;br&gt; &lt;br&gt; List of supported filterByValue per dataset (eg. dataset: filterByAttribute| supported filterByValue) &lt;br&gt;&lt;br&gt; a) returnStatusMessage: serviceName|CreateShipment,DocumentImageRequest,RateRequest,RequestIdentifier,RequestPickup,AddressValidateRequest,TrackingRequest,UpdatePickup,UpdateShipment,UploadInvoiceData,DeleteShipment,DocumentRetrieve-ePOD &lt;br&gt; b) returnStatusMessage: operationName|get-image,identifiers,address-validate,    RouteRequest, shipments, tracking, upload-image,landed-cost,rates,upload-invoice-data,pickup,proof-of-delivery &lt;br&gt; c) returnStatusMessage: protocol|REST,SOAP,XMLPI &lt;br&gt; d) productCode: docNonDocIndicator|Y,N | [optional] 
 **filter_by_attribute** | **str**| Use filter by attribute to define the list of supported attibuted for the specified datasetName. &lt;br&gt; List of supported attributes per dataset &lt;br&gt; (eg. dataset: supported filterByAttributes values) &lt;br&gt;&lt;br&gt; a) country: countryCode, countryName &lt;br&gt; b) countryPostalcodeFormat: countryCode &lt;br&gt; c) dangerousGoods: serviceCode &lt;br&gt; d) incoterm: incoterm &lt;br&gt; e) productCode: productCode, countryCode, docNonDocIndicator &lt;br&gt; f) serviceCode: serviceCode, countryCode, chargeCodeTypeCode, serviceGroupDescription &lt;br&gt; g) packageTypeCode: packageTypeCode &lt;br&gt; h) documentTypeCode: customsDocumentTypeCode &lt;br&gt; i) customerShipmentReferenceType: shipmentReferenceTypeCode &lt;br&gt; j) customerPackageReferenceType: packageReferenceTypeCode &lt;br&gt; k) invoiceReferenceType: invoiceReferenceTypeCode &lt;br&gt; l) invoiceItemReferenceType: itemReferenceTypeCode &lt;br&gt; m) registrationNumberTypeCode: registrationTypeCode &lt;br&gt; n) commodityCategory: commodityCategoryCode, commodityCategoryGroup, commodityCategoryDescription &lt;br&gt; o) returnStatusMessage: statusCode, serviceName, operationName, protocol &lt;br&gt; p) trackingEventCode: eventTypeCode, eventTypeDescription, visibleToCustomer &lt;br&gt; q) unitOfMeasurement: unitOfMeasurement | [optional] 
 **comparison_operator** | **str**| Use comparison operator to define the specific match condition for optimized search. | [optional] [default to &#39;equal&#39;]
 **query_string** | **str**| Use queryString for additional filter criteria in format of &#39;[attribute]:[value]:[comparisonOperator]&#39;. &lt;br&gt; All additional filters are applied together with logical connector &#39;AND&#39;. &lt;br&gt; Maximum of three additional attribute-value-comparisonOperator combinations. &lt;br&gt; Multiple queryString parameters will be separated  by comma \&quot;,\&quot; separator | [optional] 
 **message_reference** | **str**| Please provide message reference  | [optional] 
 **message_reference_date** | **str**| Optional reference date in the  HTTP-date format https://tools.ietf.org/html/rfc7231#section-7.1.1.2 | [optional] 
 **plugin_name** | **str**| Please provide name of the plugin (applicable to 3PV only)  | [optional] 
 **plugin_version** | **str**| Please provide version of the plugin (applicable to 3PV only)  | [optional] 
 **shipping_system_platform_name** | **str**| Please provide name of the shipping platform(applicable to 3PV only)  | [optional] 
 **shipping_system_platform_version** | **str**| Please provide version of the shipping platform (applicable to 3PV only)  | [optional] 
 **webstore_platform_name** | **str**| Please provide name of the webstore platform (applicable to 3PV only)  | [optional] 
 **webstore_platform_version** | **str**| Please provide version of the webstore platform (applicable to 3PV only)  | [optional] 

### Return type

[**SupermodelIoLogisticsExpressReferenceDataResponse**](SupermodelIoLogisticsExpressReferenceDataResponse.md)

### Authorization

[apiKey](../README.md#apiKey), [basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Reference Data found. |  * Invocation-Id - Unique identifier of the transaction <br>  * Message-Reference - Message reference provided by customer as part of request or automatically generated when not provided <br>  * Content-Language -  <br>  |
**400** | Wrong input parameters |  * Content-Type -  <br>  |
**404** | Reference Data not found |  * Content-Type -  <br>  |
**403** | Forbidden |  * Content-Type -  <br>  |
**500** | Process errors |  * Content-Type -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

