# openapi_client.RatingApi

All URIs are relative to *https://api-mock.dhl.com/mydhlapi*

Method | HTTP request | Description
------------- | ------------- | -------------
[**exp_api_landed_cost**](RatingApi.md#exp_api_landed_cost) | **POST** /landed-cost | Landed Cost
[**exp_api_rates**](RatingApi.md#exp_api_rates) | **GET** /rates | Retrieve Rates for a one piece Shipment
[**exp_api_rates_many**](RatingApi.md#exp_api_rates_many) | **POST** /rates | Retrieve Rates for Multi-piece Shipments


# **exp_api_landed_cost**
> SupermodelIoLogisticsExpressRates exp_api_landed_cost(supermodel_io_logistics_express_landed_cost_request, message_reference=message_reference, message_reference_date=message_reference_date, plugin_name=plugin_name, plugin_version=plugin_version, shipping_system_platform_name=shipping_system_platform_name, shipping_system_platform_version=shipping_system_platform_version, webstore_platform_name=webstore_platform_name, webstore_platform_version=webstore_platform_version)

Landed Cost

The Landed Cost section allows further information around products being sold to be provided. In return the duty, tax and shipping charges are calculated in real time and provides transparency about any extra costs the buyer may have to pay before they reach them. 

### Example

* Basic Authentication (basicAuth):

```python
import openapi_client
from openapi_client.models.supermodel_io_logistics_express_landed_cost_request import SupermodelIoLogisticsExpressLandedCostRequest
from openapi_client.models.supermodel_io_logistics_express_rates import SupermodelIoLogisticsExpressRates
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

# Configure HTTP basic authorization: basicAuth
configuration = openapi_client.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.RatingApi(api_client)
    supermodel_io_logistics_express_landed_cost_request = openapi_client.SupermodelIoLogisticsExpressLandedCostRequest() # SupermodelIoLogisticsExpressLandedCostRequest | Details about the requested shipment
    message_reference = 'd0e7832e-5c98-11ea-bc55-0242ac13' # str | Please provide message reference  (optional)
    message_reference_date = 'Wed, 21 Oct 2015 07:28:00 GMT' # str | Optional reference date in the  HTTP-date format https://tools.ietf.org/html/rfc7231#section-7.1.1.2 (optional)
    plugin_name = ' ' # str | Please provide name of the plugin (applicable to 3PV only)  (optional)
    plugin_version = ' ' # str | Please provide version of the plugin (applicable to 3PV only)  (optional)
    shipping_system_platform_name = ' ' # str | Please provide name of the shipping platform(applicable to 3PV only)  (optional)
    shipping_system_platform_version = ' ' # str | Please provide version of the shipping platform (applicable to 3PV only)  (optional)
    webstore_platform_name = ' ' # str | Please provide name of the webstore platform (applicable to 3PV only)  (optional)
    webstore_platform_version = ' ' # str | Please provide version of the webstore platform (applicable to 3PV only)  (optional)

    try:
        # Landed Cost
        api_response = api_instance.exp_api_landed_cost(supermodel_io_logistics_express_landed_cost_request, message_reference=message_reference, message_reference_date=message_reference_date, plugin_name=plugin_name, plugin_version=plugin_version, shipping_system_platform_name=shipping_system_platform_name, shipping_system_platform_version=shipping_system_platform_version, webstore_platform_name=webstore_platform_name, webstore_platform_version=webstore_platform_version)
        print("The response of RatingApi->exp_api_landed_cost:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RatingApi->exp_api_landed_cost: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **supermodel_io_logistics_express_landed_cost_request** | [**SupermodelIoLogisticsExpressLandedCostRequest**](SupermodelIoLogisticsExpressLandedCostRequest.md)| Details about the requested shipment | 
 **message_reference** | **str**| Please provide message reference  | [optional] 
 **message_reference_date** | **str**| Optional reference date in the  HTTP-date format https://tools.ietf.org/html/rfc7231#section-7.1.1.2 | [optional] 
 **plugin_name** | **str**| Please provide name of the plugin (applicable to 3PV only)  | [optional] 
 **plugin_version** | **str**| Please provide version of the plugin (applicable to 3PV only)  | [optional] 
 **shipping_system_platform_name** | **str**| Please provide name of the shipping platform(applicable to 3PV only)  | [optional] 
 **shipping_system_platform_version** | **str**| Please provide version of the shipping platform (applicable to 3PV only)  | [optional] 
 **webstore_platform_name** | **str**| Please provide name of the webstore platform (applicable to 3PV only)  | [optional] 
 **webstore_platform_version** | **str**| Please provide version of the webstore platform (applicable to 3PV only)  | [optional] 

### Return type

[**SupermodelIoLogisticsExpressRates**](SupermodelIoLogisticsExpressRates.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Landed cost |  * Invocation-Id - Unique identifier of the transaction <br>  * Message-Reference - Message reference provided by customer as part of request or automatically generated when not provided <br>  * Quotation-Id - Quotation ID if getQuotationID is requested <br>  |
**400** | Wrong input parameters |  * Content-Type -  <br>  |
**500** | Process errors |  * Content-Type -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **exp_api_rates**
> SupermodelIoLogisticsExpressRates exp_api_rates(account_number, origin_country_code, origin_city_name, destination_country_code, destination_city_name, weight, length, width, height, planned_shipping_date, is_customs_declarable, unit_of_measurement, origin_postal_code=origin_postal_code, destination_postal_code=destination_postal_code, next_business_day=next_business_day, message_reference=message_reference, message_reference_date=message_reference_date, plugin_name=plugin_name, plugin_version=plugin_version, shipping_system_platform_name=shipping_system_platform_name, shipping_system_platform_version=shipping_system_platform_version, webstore_platform_name=webstore_platform_name, webstore_platform_version=webstore_platform_version, strict_validation=strict_validation, get_all_value_added_services=get_all_value_added_services, request_estimated_delivery_date=request_estimated_delivery_date, estimated_delivery_date_type=estimated_delivery_date_type)

Retrieve Rates for a one piece Shipment

The Rate request will return DHL's product capabilities and prices (where applicable) based on the input data. Using the shipper and receiver address as well as the dimension and weights of the pieces belonging to a shipment, this operation returns the available products including the shipping price (where applicable) 

### Example

* Basic Authentication (basicAuth):

```python
import openapi_client
from openapi_client.models.supermodel_io_logistics_express_rates import SupermodelIoLogisticsExpressRates
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

# Configure HTTP basic authorization: basicAuth
configuration = openapi_client.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.RatingApi(api_client)
    account_number = '123456789' # str | DHL Express customer account number
    origin_country_code = 'CZ' # str | A short text string code (see values defined in ISO 3166) specifying the shipment origin country. https://gs1.org/voc/Country, Alpha-2 Code
    origin_city_name = 'Prague' # str | Text specifying the city name
    destination_country_code = 'CZ' # str | A short text string code (see values defined in ISO 3166) specifying the shipment destination country. https://gs1.org/voc/Country, Alpha-2 Code
    destination_city_name = 'Prague' # str | Text specifying the city name
    weight = 5 # float | Gross weight of the shipment including packaging.
    length = 15 # float | Total length of the shipment including packaging.
    width = 10 # float | Total width of the shipment including packaging.
    height = 5 # float | Total height of the shipment including packaging.
    planned_shipping_date = '2020-02-26' # str | Timestamp represents the date you plan to ship your prospected shipment 
    is_customs_declarable = false # bool | 
    unit_of_measurement = 'metric' # str | The UnitOfMeasurement node conveys the unit of measurements used in the operation. This single value corresponds to the units of weight and measurement which are used throughout the message processing. 
    origin_postal_code = '14800' # str | Text specifying the postal code for an address. https://gs1.org/voc/postalCode (optional)
    destination_postal_code = '14800' # str | Text specifying the postal code for an address. https://gs1.org/voc/postalCode (optional)
    next_business_day = false # bool | When set to true and there are no products available for given plannedShippingDate then products available for the next possible pickup date are returned  (optional)
    message_reference = 'd0e7832e-5c98-11ea-bc55-0242ac13' # str | Please provide message reference  (optional)
    message_reference_date = 'Wed, 21 Oct 2015 07:28:00 GMT' # str | Optional reference date in the  HTTP-date format https://tools.ietf.org/html/rfc7231#section-7.1.1.2 (optional)
    plugin_name = ' ' # str | Please provide name of the plugin (applicable to 3PV only)  (optional)
    plugin_version = ' ' # str | Please provide version of the plugin (applicable to 3PV only)  (optional)
    shipping_system_platform_name = ' ' # str | Please provide name of the shipping platform(applicable to 3PV only)  (optional)
    shipping_system_platform_version = ' ' # str | Please provide version of the shipping platform (applicable to 3PV only)  (optional)
    webstore_platform_name = ' ' # str | Please provide name of the webstore platform (applicable to 3PV only)  (optional)
    webstore_platform_version = ' ' # str | Please provide version of the webstore platform (applicable to 3PV only)  (optional)
    strict_validation = False # bool | If set to true, indicate strict DCT validation of address details, and validation of product and service(s) combination provided in request. (optional) (default to False)
    get_all_value_added_services = False # bool | Option to return list of all value added services and its rule groups if applicable (optional) (default to False)
    request_estimated_delivery_date = True # bool | Option to return Estimated Delivery Date in response (optional) (default to True)
    estimated_delivery_date_type = 'QDDF' # str | Estimated Delivery Date Type. QDDF: is the fastest transit time as quoted to the customer at booking or shipment creation. When clearance or any other non-transport operational component is expected to impact transit time, QDDF does not constitute DHL's service commitment. QDDC: cconstitutes DHL's service commitment as quoted at booking or shipment creation. QDDC builds in clearance time, and potentially other special operational non-transport component(s), when relevant.  (optional) (default to 'QDDF')

    try:
        # Retrieve Rates for a one piece Shipment
        api_response = api_instance.exp_api_rates(account_number, origin_country_code, origin_city_name, destination_country_code, destination_city_name, weight, length, width, height, planned_shipping_date, is_customs_declarable, unit_of_measurement, origin_postal_code=origin_postal_code, destination_postal_code=destination_postal_code, next_business_day=next_business_day, message_reference=message_reference, message_reference_date=message_reference_date, plugin_name=plugin_name, plugin_version=plugin_version, shipping_system_platform_name=shipping_system_platform_name, shipping_system_platform_version=shipping_system_platform_version, webstore_platform_name=webstore_platform_name, webstore_platform_version=webstore_platform_version, strict_validation=strict_validation, get_all_value_added_services=get_all_value_added_services, request_estimated_delivery_date=request_estimated_delivery_date, estimated_delivery_date_type=estimated_delivery_date_type)
        print("The response of RatingApi->exp_api_rates:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RatingApi->exp_api_rates: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_number** | **str**| DHL Express customer account number | 
 **origin_country_code** | **str**| A short text string code (see values defined in ISO 3166) specifying the shipment origin country. https://gs1.org/voc/Country, Alpha-2 Code | 
 **origin_city_name** | **str**| Text specifying the city name | 
 **destination_country_code** | **str**| A short text string code (see values defined in ISO 3166) specifying the shipment destination country. https://gs1.org/voc/Country, Alpha-2 Code | 
 **destination_city_name** | **str**| Text specifying the city name | 
 **weight** | **float**| Gross weight of the shipment including packaging. | 
 **length** | **float**| Total length of the shipment including packaging. | 
 **width** | **float**| Total width of the shipment including packaging. | 
 **height** | **float**| Total height of the shipment including packaging. | 
 **planned_shipping_date** | **str**| Timestamp represents the date you plan to ship your prospected shipment  | 
 **is_customs_declarable** | **bool**|  | 
 **unit_of_measurement** | **str**| The UnitOfMeasurement node conveys the unit of measurements used in the operation. This single value corresponds to the units of weight and measurement which are used throughout the message processing.  | 
 **origin_postal_code** | **str**| Text specifying the postal code for an address. https://gs1.org/voc/postalCode | [optional] 
 **destination_postal_code** | **str**| Text specifying the postal code for an address. https://gs1.org/voc/postalCode | [optional] 
 **next_business_day** | **bool**| When set to true and there are no products available for given plannedShippingDate then products available for the next possible pickup date are returned  | [optional] 
 **message_reference** | **str**| Please provide message reference  | [optional] 
 **message_reference_date** | **str**| Optional reference date in the  HTTP-date format https://tools.ietf.org/html/rfc7231#section-7.1.1.2 | [optional] 
 **plugin_name** | **str**| Please provide name of the plugin (applicable to 3PV only)  | [optional] 
 **plugin_version** | **str**| Please provide version of the plugin (applicable to 3PV only)  | [optional] 
 **shipping_system_platform_name** | **str**| Please provide name of the shipping platform(applicable to 3PV only)  | [optional] 
 **shipping_system_platform_version** | **str**| Please provide version of the shipping platform (applicable to 3PV only)  | [optional] 
 **webstore_platform_name** | **str**| Please provide name of the webstore platform (applicable to 3PV only)  | [optional] 
 **webstore_platform_version** | **str**| Please provide version of the webstore platform (applicable to 3PV only)  | [optional] 
 **strict_validation** | **bool**| If set to true, indicate strict DCT validation of address details, and validation of product and service(s) combination provided in request. | [optional] [default to False]
 **get_all_value_added_services** | **bool**| Option to return list of all value added services and its rule groups if applicable | [optional] [default to False]
 **request_estimated_delivery_date** | **bool**| Option to return Estimated Delivery Date in response | [optional] [default to True]
 **estimated_delivery_date_type** | **str**| Estimated Delivery Date Type. QDDF: is the fastest transit time as quoted to the customer at booking or shipment creation. When clearance or any other non-transport operational component is expected to impact transit time, QDDF does not constitute DHL&#39;s service commitment. QDDC: cconstitutes DHL&#39;s service commitment as quoted at booking or shipment creation. QDDC builds in clearance time, and potentially other special operational non-transport component(s), when relevant.  | [optional] [default to &#39;QDDF&#39;]

### Return type

[**SupermodelIoLogisticsExpressRates**](SupermodelIoLogisticsExpressRates.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Rates found |  -  |
**400** | Wrong input parameters |  * Content-Type -  <br>  |
**500** | Process errors |  * Content-Type -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **exp_api_rates_many**
> SupermodelIoLogisticsExpressRates exp_api_rates_many(supermodel_io_logistics_express_rate_request, message_reference=message_reference, message_reference_date=message_reference_date, plugin_name=plugin_name, plugin_version=plugin_version, shipping_system_platform_name=shipping_system_platform_name, shipping_system_platform_version=shipping_system_platform_version, webstore_platform_name=webstore_platform_name, webstore_platform_version=webstore_platform_version, strict_validation=strict_validation)

Retrieve Rates for Multi-piece Shipments

The Rate request will return DHL's product capabilities and prices (where applicable) based on the input data. Using the shipper and receiver address as well as the dimension and weights of the pieces belonging to a shipment, this operation returns the available products including the shipping price (where applicable) 

### Example

* Basic Authentication (basicAuth):

```python
import openapi_client
from openapi_client.models.supermodel_io_logistics_express_rate_request import SupermodelIoLogisticsExpressRateRequest
from openapi_client.models.supermodel_io_logistics_express_rates import SupermodelIoLogisticsExpressRates
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

# Configure HTTP basic authorization: basicAuth
configuration = openapi_client.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.RatingApi(api_client)
    supermodel_io_logistics_express_rate_request = openapi_client.SupermodelIoLogisticsExpressRateRequest() # SupermodelIoLogisticsExpressRateRequest | Details about the requested shipment
    message_reference = 'd0e7832e-5c98-11ea-bc55-0242ac13' # str | Please provide message reference  (optional)
    message_reference_date = 'Wed, 21 Oct 2015 07:28:00 GMT' # str | Optional reference date in the  HTTP-date format https://tools.ietf.org/html/rfc7231#section-7.1.1.2 (optional)
    plugin_name = ' ' # str | Please provide name of the plugin (applicable to 3PV only)  (optional)
    plugin_version = ' ' # str | Please provide version of the plugin (applicable to 3PV only)  (optional)
    shipping_system_platform_name = ' ' # str | Please provide name of the shipping platform(applicable to 3PV only)  (optional)
    shipping_system_platform_version = ' ' # str | Please provide version of the shipping platform (applicable to 3PV only)  (optional)
    webstore_platform_name = ' ' # str | Please provide name of the webstore platform (applicable to 3PV only)  (optional)
    webstore_platform_version = ' ' # str | Please provide version of the webstore platform (applicable to 3PV only)  (optional)
    strict_validation = False # bool | If set to true, indicate strict DCT validation of address details, and validation of product and service(s) combination provided in request. (optional) (default to False)

    try:
        # Retrieve Rates for Multi-piece Shipments
        api_response = api_instance.exp_api_rates_many(supermodel_io_logistics_express_rate_request, message_reference=message_reference, message_reference_date=message_reference_date, plugin_name=plugin_name, plugin_version=plugin_version, shipping_system_platform_name=shipping_system_platform_name, shipping_system_platform_version=shipping_system_platform_version, webstore_platform_name=webstore_platform_name, webstore_platform_version=webstore_platform_version, strict_validation=strict_validation)
        print("The response of RatingApi->exp_api_rates_many:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RatingApi->exp_api_rates_many: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **supermodel_io_logistics_express_rate_request** | [**SupermodelIoLogisticsExpressRateRequest**](SupermodelIoLogisticsExpressRateRequest.md)| Details about the requested shipment | 
 **message_reference** | **str**| Please provide message reference  | [optional] 
 **message_reference_date** | **str**| Optional reference date in the  HTTP-date format https://tools.ietf.org/html/rfc7231#section-7.1.1.2 | [optional] 
 **plugin_name** | **str**| Please provide name of the plugin (applicable to 3PV only)  | [optional] 
 **plugin_version** | **str**| Please provide version of the plugin (applicable to 3PV only)  | [optional] 
 **shipping_system_platform_name** | **str**| Please provide name of the shipping platform(applicable to 3PV only)  | [optional] 
 **shipping_system_platform_version** | **str**| Please provide version of the shipping platform (applicable to 3PV only)  | [optional] 
 **webstore_platform_name** | **str**| Please provide name of the webstore platform (applicable to 3PV only)  | [optional] 
 **webstore_platform_version** | **str**| Please provide version of the webstore platform (applicable to 3PV only)  | [optional] 
 **strict_validation** | **bool**| If set to true, indicate strict DCT validation of address details, and validation of product and service(s) combination provided in request. | [optional] [default to False]

### Return type

[**SupermodelIoLogisticsExpressRates**](SupermodelIoLogisticsExpressRates.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Rates found |  -  |
**400** | Wrong input parameters |  * Content-Type -  <br>  |
**500** | Process errors |  * Content-Type -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

