# openapi_client.TrackingApi

All URIs are relative to *https://api-mock.dhl.com/mydhlapi*

Method | HTTP request | Description
------------- | ------------- | -------------
[**exp_api_shipments_tracking**](TrackingApi.md#exp_api_shipments_tracking) | **GET** /shipments/{shipmentTrackingNumber}/tracking | Track a single DHL Express Shipment
[**exp_api_shipments_tracking_multi**](TrackingApi.md#exp_api_shipments_tracking_multi) | **GET** /tracking | Track a single or multiple DHL Express Shipments


# **exp_api_shipments_tracking**
> SupermodelIoLogisticsExpressTrackingResponse exp_api_shipments_tracking(shipment_tracking_number, tracking_view=tracking_view, level_of_detail=level_of_detail, request_controlled_access_data_codes=request_controlled_access_data_codes, request_gmt_offset_per_event=request_gmt_offset_per_event, message_reference=message_reference, message_reference_date=message_reference_date, accept_language=accept_language, plugin_name=plugin_name, plugin_version=plugin_version, shipping_system_platform_name=shipping_system_platform_name, shipping_system_platform_version=shipping_system_platform_version, webstore_platform_name=webstore_platform_name, webstore_platform_version=webstore_platform_version)

Track a single DHL Express Shipment

The Tracking service retrieves tracking statuses for a single DHL Express Shipment 

### Example

* Basic Authentication (basicAuth):

```python
import openapi_client
from openapi_client.models.supermodel_io_logistics_express_tracking_response import SupermodelIoLogisticsExpressTrackingResponse
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
    api_instance = openapi_client.TrackingApi(api_client)
    shipment_tracking_number = '9356579890' # str | DHL Express shipment identification number
    tracking_view = 'all-checkpoints' # str |  (optional) (default to 'all-checkpoints')
    level_of_detail = 'shipment' # str |  (optional) (default to 'shipment')
    request_controlled_access_data_codes = false # bool | Query parameter to request to return values of controlled access code fields in response. (optional)
    request_gmt_offset_per_event = false # bool | Query parameter to request to return GMT Offset of each event in response, for both shipment level and piece level. (optional)
    message_reference = 'd0e7832e-5c98-11ea-bc55-0242ac13' # str | Please provide message reference  (optional)
    message_reference_date = 'Wed, 21 Oct 2015 07:28:00 GMT' # str | Optional reference date in the  HTTP-date format https://tools.ietf.org/html/rfc7231#section-7.1.1.2 (optional)
    accept_language = 'eng' # str | Format {3-character language code} (optional) (default to 'eng')
    plugin_name = ' ' # str | Please provide name of the plugin (applicable to 3PV only)  (optional)
    plugin_version = ' ' # str | Please provide version of the plugin (applicable to 3PV only)  (optional)
    shipping_system_platform_name = ' ' # str | Please provide name of the shipping platform(applicable to 3PV only)  (optional)
    shipping_system_platform_version = ' ' # str | Please provide version of the shipping platform (applicable to 3PV only)  (optional)
    webstore_platform_name = ' ' # str | Please provide name of the webstore platform (applicable to 3PV only)  (optional)
    webstore_platform_version = ' ' # str | Please provide version of the webstore platform (applicable to 3PV only)  (optional)

    try:
        # Track a single DHL Express Shipment
        api_response = api_instance.exp_api_shipments_tracking(shipment_tracking_number, tracking_view=tracking_view, level_of_detail=level_of_detail, request_controlled_access_data_codes=request_controlled_access_data_codes, request_gmt_offset_per_event=request_gmt_offset_per_event, message_reference=message_reference, message_reference_date=message_reference_date, accept_language=accept_language, plugin_name=plugin_name, plugin_version=plugin_version, shipping_system_platform_name=shipping_system_platform_name, shipping_system_platform_version=shipping_system_platform_version, webstore_platform_name=webstore_platform_name, webstore_platform_version=webstore_platform_version)
        print("The response of TrackingApi->exp_api_shipments_tracking:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TrackingApi->exp_api_shipments_tracking: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **shipment_tracking_number** | **str**| DHL Express shipment identification number | 
 **tracking_view** | **str**|  | [optional] [default to &#39;all-checkpoints&#39;]
 **level_of_detail** | **str**|  | [optional] [default to &#39;shipment&#39;]
 **request_controlled_access_data_codes** | **bool**| Query parameter to request to return values of controlled access code fields in response. | [optional] 
 **request_gmt_offset_per_event** | **bool**| Query parameter to request to return GMT Offset of each event in response, for both shipment level and piece level. | [optional] 
 **message_reference** | **str**| Please provide message reference  | [optional] 
 **message_reference_date** | **str**| Optional reference date in the  HTTP-date format https://tools.ietf.org/html/rfc7231#section-7.1.1.2 | [optional] 
 **accept_language** | **str**| Format {3-character language code} | [optional] [default to &#39;eng&#39;]
 **plugin_name** | **str**| Please provide name of the plugin (applicable to 3PV only)  | [optional] 
 **plugin_version** | **str**| Please provide version of the plugin (applicable to 3PV only)  | [optional] 
 **shipping_system_platform_name** | **str**| Please provide name of the shipping platform(applicable to 3PV only)  | [optional] 
 **shipping_system_platform_version** | **str**| Please provide version of the shipping platform (applicable to 3PV only)  | [optional] 
 **webstore_platform_name** | **str**| Please provide name of the webstore platform (applicable to 3PV only)  | [optional] 
 **webstore_platform_version** | **str**| Please provide version of the webstore platform (applicable to 3PV only)  | [optional] 

### Return type

[**SupermodelIoLogisticsExpressTrackingResponse**](SupermodelIoLogisticsExpressTrackingResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Shipment details found |  * Invocation-Id - Unique identifier of the transaction <br>  * Message-Reference - Message reference provided by customer as part of request or automatically generated when not provided <br>  * Content-Language -  <br>  |
**400** | Wrong input parameters |  * Content-Type -  <br>  |
**404** | No data found |  * Content-Type -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **exp_api_shipments_tracking_multi**
> SupermodelIoLogisticsExpressTrackingResponse exp_api_shipments_tracking_multi(shipment_tracking_number=shipment_tracking_number, piece_tracking_number=piece_tracking_number, shipment_reference=shipment_reference, shipment_reference_type=shipment_reference_type, shipper_account_number=shipper_account_number, date_range_from=date_range_from, date_range_to=date_range_to, tracking_view=tracking_view, level_of_detail=level_of_detail, request_controlled_access_data_codes=request_controlled_access_data_codes, message_reference=message_reference, message_reference_date=message_reference_date, accept_language=accept_language, plugin_name=plugin_name, plugin_version=plugin_version, shipping_system_platform_name=shipping_system_platform_name, shipping_system_platform_version=shipping_system_platform_version, webstore_platform_name=webstore_platform_name, webstore_platform_version=webstore_platform_version)

Track a single or multiple DHL Express Shipments

The Tracking service retrieves tracking statuses for a single or multiple DHL Express Shipments 

### Example

* Basic Authentication (basicAuth):

```python
import openapi_client
from openapi_client.models.supermodel_io_logistics_express_tracking_response import SupermodelIoLogisticsExpressTrackingResponse
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
    api_instance = openapi_client.TrackingApi(api_client)
    shipment_tracking_number = ['9356579890'] # List[str] | DHL Express shipment identification number (optional)
    piece_tracking_number = ['piece_tracking_number_example'] # List[str] | DHL Express shipment piece tracking number (optional)
    shipment_reference = 'CustomerReference1' # str | Shipment reference which was provided during the shipment label creation  (optional)
    shipment_reference_type = 'CU' # str | Shipment reference type which was provided during the shipment label creation  (optional)
    shipper_account_number = '123456789' # str | Shipper DHL Express Account number under which the shipment label was created  (optional)
    date_range_from = '2020-05-01' # str | When tracking by Shipment reference you need to restrict the search by timeframe. Please provide the start of the period.  (optional)
    date_range_to = '2020-06-01' # str | When tracking by Shipment reference you need to restrict the search by timeframe. Please provide the end of the period.  (optional)
    tracking_view = 'all-checkpoints' # str |  (optional) (default to 'all-checkpoints')
    level_of_detail = 'shipment' # str |  (optional) (default to 'shipment')
    request_controlled_access_data_codes = false # bool | Query parameter to request to return values of controlled access code fields in response. (optional)
    message_reference = 'd0e7832e-5c98-11ea-bc55-0242ac13' # str | Please provide message reference  (optional)
    message_reference_date = 'Wed, 21 Oct 2015 07:28:00 GMT' # str | Optional reference date in the  HTTP-date format https://tools.ietf.org/html/rfc7231#section-7.1.1.2 (optional)
    accept_language = 'eng' # str | Format {3-character language code} (optional) (default to 'eng')
    plugin_name = ' ' # str | Please provide name of the plugin (applicable to 3PV only)  (optional)
    plugin_version = ' ' # str | Please provide version of the plugin (applicable to 3PV only)  (optional)
    shipping_system_platform_name = ' ' # str | Please provide name of the shipping platform(applicable to 3PV only)  (optional)
    shipping_system_platform_version = ' ' # str | Please provide version of the shipping platform (applicable to 3PV only)  (optional)
    webstore_platform_name = ' ' # str | Please provide name of the webstore platform (applicable to 3PV only)  (optional)
    webstore_platform_version = ' ' # str | Please provide version of the webstore platform (applicable to 3PV only)  (optional)

    try:
        # Track a single or multiple DHL Express Shipments
        api_response = api_instance.exp_api_shipments_tracking_multi(shipment_tracking_number=shipment_tracking_number, piece_tracking_number=piece_tracking_number, shipment_reference=shipment_reference, shipment_reference_type=shipment_reference_type, shipper_account_number=shipper_account_number, date_range_from=date_range_from, date_range_to=date_range_to, tracking_view=tracking_view, level_of_detail=level_of_detail, request_controlled_access_data_codes=request_controlled_access_data_codes, message_reference=message_reference, message_reference_date=message_reference_date, accept_language=accept_language, plugin_name=plugin_name, plugin_version=plugin_version, shipping_system_platform_name=shipping_system_platform_name, shipping_system_platform_version=shipping_system_platform_version, webstore_platform_name=webstore_platform_name, webstore_platform_version=webstore_platform_version)
        print("The response of TrackingApi->exp_api_shipments_tracking_multi:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TrackingApi->exp_api_shipments_tracking_multi: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **shipment_tracking_number** | [**List[str]**](str.md)| DHL Express shipment identification number | [optional] 
 **piece_tracking_number** | [**List[str]**](str.md)| DHL Express shipment piece tracking number | [optional] 
 **shipment_reference** | **str**| Shipment reference which was provided during the shipment label creation  | [optional] 
 **shipment_reference_type** | **str**| Shipment reference type which was provided during the shipment label creation  | [optional] 
 **shipper_account_number** | **str**| Shipper DHL Express Account number under which the shipment label was created  | [optional] 
 **date_range_from** | **str**| When tracking by Shipment reference you need to restrict the search by timeframe. Please provide the start of the period.  | [optional] 
 **date_range_to** | **str**| When tracking by Shipment reference you need to restrict the search by timeframe. Please provide the end of the period.  | [optional] 
 **tracking_view** | **str**|  | [optional] [default to &#39;all-checkpoints&#39;]
 **level_of_detail** | **str**|  | [optional] [default to &#39;shipment&#39;]
 **request_controlled_access_data_codes** | **bool**| Query parameter to request to return values of controlled access code fields in response. | [optional] 
 **message_reference** | **str**| Please provide message reference  | [optional] 
 **message_reference_date** | **str**| Optional reference date in the  HTTP-date format https://tools.ietf.org/html/rfc7231#section-7.1.1.2 | [optional] 
 **accept_language** | **str**| Format {3-character language code} | [optional] [default to &#39;eng&#39;]
 **plugin_name** | **str**| Please provide name of the plugin (applicable to 3PV only)  | [optional] 
 **plugin_version** | **str**| Please provide version of the plugin (applicable to 3PV only)  | [optional] 
 **shipping_system_platform_name** | **str**| Please provide name of the shipping platform(applicable to 3PV only)  | [optional] 
 **shipping_system_platform_version** | **str**| Please provide version of the shipping platform (applicable to 3PV only)  | [optional] 
 **webstore_platform_name** | **str**| Please provide name of the webstore platform (applicable to 3PV only)  | [optional] 
 **webstore_platform_version** | **str**| Please provide version of the webstore platform (applicable to 3PV only)  | [optional] 

### Return type

[**SupermodelIoLogisticsExpressTrackingResponse**](SupermodelIoLogisticsExpressTrackingResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Shipment details found |  * Invocation-Id - Unique identifier of the transaction <br>  * Message-Reference - Message reference provided by customer as part of request or automatically generated when not provided <br>  * Content-Language -  <br>  |
**400** | Wrong input parameters |  * Content-Type -  <br>  |
**404** | No data found |  * Content-Type -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

