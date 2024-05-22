# openapi_client.PickupApi

All URIs are relative to *https://api-mock.dhl.com/mydhlapi*

Method | HTTP request | Description
------------- | ------------- | -------------
[**exp_api_pickups**](PickupApi.md#exp_api_pickups) | **POST** /pickups | Create a DHL Express pickup booking request
[**exp_api_pickups_cancel**](PickupApi.md#exp_api_pickups_cancel) | **DELETE** /pickups/{dispatchConfirmationNumber} | Cancel a DHL Express pickup booking request
[**exp_api_pickups_update**](PickupApi.md#exp_api_pickups_update) | **PATCH** /pickups/{dispatchConfirmationNumber} | Update pickup information for an existing DHL Express pickup booking request


# **exp_api_pickups**
> SupermodelIoLogisticsExpressPickupResponse exp_api_pickups(supermodel_io_logistics_express_pickup_request, message_reference=message_reference, message_reference_date=message_reference_date, plugin_name=plugin_name, plugin_version=plugin_version, shipping_system_platform_name=shipping_system_platform_name, shipping_system_platform_version=shipping_system_platform_version, webstore_platform_name=webstore_platform_name, webstore_platform_version=webstore_platform_version)

Create a DHL Express pickup booking request

The Pickup service creates a DHL Express pickup booking request 

### Example

* Basic Authentication (basicAuth):

```python
import openapi_client
from openapi_client.models.supermodel_io_logistics_express_pickup_request import SupermodelIoLogisticsExpressPickupRequest
from openapi_client.models.supermodel_io_logistics_express_pickup_response import SupermodelIoLogisticsExpressPickupResponse
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
    api_instance = openapi_client.PickupApi(api_client)
    supermodel_io_logistics_express_pickup_request = openapi_client.SupermodelIoLogisticsExpressPickupRequest() # SupermodelIoLogisticsExpressPickupRequest | Details about the requested pickup
    message_reference = 'd0e7832e-5c98-11ea-bc55-0242ac13' # str | Please provide message reference  (optional)
    message_reference_date = 'Wed, 21 Oct 2015 07:28:00 GMT' # str | Optional reference date in the  HTTP-date format https://tools.ietf.org/html/rfc7231#section-7.1.1.2 (optional)
    plugin_name = ' ' # str | Please provide name of the plugin (applicable to 3PV only)  (optional)
    plugin_version = ' ' # str | Please provide version of the plugin (applicable to 3PV only)  (optional)
    shipping_system_platform_name = ' ' # str | Please provide name of the shipping platform(applicable to 3PV only)  (optional)
    shipping_system_platform_version = ' ' # str | Please provide version of the shipping platform (applicable to 3PV only)  (optional)
    webstore_platform_name = ' ' # str | Please provide name of the webstore platform (applicable to 3PV only)  (optional)
    webstore_platform_version = ' ' # str | Please provide version of the webstore platform (applicable to 3PV only)  (optional)

    try:
        # Create a DHL Express pickup booking request
        api_response = api_instance.exp_api_pickups(supermodel_io_logistics_express_pickup_request, message_reference=message_reference, message_reference_date=message_reference_date, plugin_name=plugin_name, plugin_version=plugin_version, shipping_system_platform_name=shipping_system_platform_name, shipping_system_platform_version=shipping_system_platform_version, webstore_platform_name=webstore_platform_name, webstore_platform_version=webstore_platform_version)
        print("The response of PickupApi->exp_api_pickups:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PickupApi->exp_api_pickups: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **supermodel_io_logistics_express_pickup_request** | [**SupermodelIoLogisticsExpressPickupRequest**](SupermodelIoLogisticsExpressPickupRequest.md)| Details about the requested pickup | 
 **message_reference** | **str**| Please provide message reference  | [optional] 
 **message_reference_date** | **str**| Optional reference date in the  HTTP-date format https://tools.ietf.org/html/rfc7231#section-7.1.1.2 | [optional] 
 **plugin_name** | **str**| Please provide name of the plugin (applicable to 3PV only)  | [optional] 
 **plugin_version** | **str**| Please provide version of the plugin (applicable to 3PV only)  | [optional] 
 **shipping_system_platform_name** | **str**| Please provide name of the shipping platform(applicable to 3PV only)  | [optional] 
 **shipping_system_platform_version** | **str**| Please provide version of the shipping platform (applicable to 3PV only)  | [optional] 
 **webstore_platform_name** | **str**| Please provide name of the webstore platform (applicable to 3PV only)  | [optional] 
 **webstore_platform_version** | **str**| Please provide version of the webstore platform (applicable to 3PV only)  | [optional] 

### Return type

[**SupermodelIoLogisticsExpressPickupResponse**](SupermodelIoLogisticsExpressPickupResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Pickup created |  -  |
**400** | Wrong input parameters |  * Content-Type -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **exp_api_pickups_cancel**
> exp_api_pickups_cancel(dispatch_confirmation_number, requestor_name, reason, message_reference=message_reference, message_reference_date=message_reference_date, plugin_name=plugin_name, plugin_version=plugin_version, shipping_system_platform_name=shipping_system_platform_name, shipping_system_platform_version=shipping_system_platform_version, webstore_platform_name=webstore_platform_name, webstore_platform_version=webstore_platform_version)

Cancel a DHL Express pickup booking request

The Cancel Pickup service can be used to cancel a DHL Express pickup booking request 

### Example

* Basic Authentication (basicAuth):

```python
import openapi_client
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
    api_instance = openapi_client.PickupApi(api_client)
    dispatch_confirmation_number = 'PRG999126012345' # str | Shipment pickup confirmation number for example `PRG999126012345`
    requestor_name = 'Fred Brent' # str | Name of the person requesting to cancel the scheduled pickup 
    reason = 'Unplanned leave' # str | Provide why scheduled pickup is being cancelled 
    message_reference = 'd0e7832e-5c98-11ea-bc55-0242ac13' # str | Please provide message reference  (optional)
    message_reference_date = 'Wed, 21 Oct 2015 07:28:00 GMT' # str | Optional reference date in the  HTTP-date format https://tools.ietf.org/html/rfc7231#section-7.1.1.2 (optional)
    plugin_name = ' ' # str | Please provide name of the plugin (applicable to 3PV only)  (optional)
    plugin_version = ' ' # str | Please provide version of the plugin (applicable to 3PV only)  (optional)
    shipping_system_platform_name = ' ' # str | Please provide name of the shipping platform(applicable to 3PV only)  (optional)
    shipping_system_platform_version = ' ' # str | Please provide version of the shipping platform (applicable to 3PV only)  (optional)
    webstore_platform_name = ' ' # str | Please provide name of the webstore platform (applicable to 3PV only)  (optional)
    webstore_platform_version = ' ' # str | Please provide version of the webstore platform (applicable to 3PV only)  (optional)

    try:
        # Cancel a DHL Express pickup booking request
        api_instance.exp_api_pickups_cancel(dispatch_confirmation_number, requestor_name, reason, message_reference=message_reference, message_reference_date=message_reference_date, plugin_name=plugin_name, plugin_version=plugin_version, shipping_system_platform_name=shipping_system_platform_name, shipping_system_platform_version=shipping_system_platform_version, webstore_platform_name=webstore_platform_name, webstore_platform_version=webstore_platform_version)
    except Exception as e:
        print("Exception when calling PickupApi->exp_api_pickups_cancel: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dispatch_confirmation_number** | **str**| Shipment pickup confirmation number for example &#x60;PRG999126012345&#x60; | 
 **requestor_name** | **str**| Name of the person requesting to cancel the scheduled pickup  | 
 **reason** | **str**| Provide why scheduled pickup is being cancelled  | 
 **message_reference** | **str**| Please provide message reference  | [optional] 
 **message_reference_date** | **str**| Optional reference date in the  HTTP-date format https://tools.ietf.org/html/rfc7231#section-7.1.1.2 | [optional] 
 **plugin_name** | **str**| Please provide name of the plugin (applicable to 3PV only)  | [optional] 
 **plugin_version** | **str**| Please provide version of the plugin (applicable to 3PV only)  | [optional] 
 **shipping_system_platform_name** | **str**| Please provide name of the shipping platform(applicable to 3PV only)  | [optional] 
 **shipping_system_platform_version** | **str**| Please provide version of the shipping platform (applicable to 3PV only)  | [optional] 
 **webstore_platform_name** | **str**| Please provide name of the webstore platform (applicable to 3PV only)  | [optional] 
 **webstore_platform_version** | **str**| Please provide version of the webstore platform (applicable to 3PV only)  | [optional] 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Pickup cancelled |  -  |
**400** | Pickup already cancelled or completed / Wrong input parameters |  * Content-Type -  <br>  |
**404** | Pickup not found |  * Content-Type -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **exp_api_pickups_update**
> SupermodelIoLogisticsExpressUpdatePickupResponse exp_api_pickups_update(dispatch_confirmation_number, supermodel_io_logistics_express_update_pickup_request, message_reference=message_reference, message_reference_date=message_reference_date, plugin_name=plugin_name, plugin_version=plugin_version, shipping_system_platform_name=shipping_system_platform_name, shipping_system_platform_version=shipping_system_platform_version, webstore_platform_name=webstore_platform_name, webstore_platform_version=webstore_platform_version)

Update pickup information for an existing DHL Express pickup booking request

The Update Pickup service can be used to update pickup information for an existing DHL Express pickup booking request 

### Example

* Basic Authentication (basicAuth):

```python
import openapi_client
from openapi_client.models.supermodel_io_logistics_express_update_pickup_request import SupermodelIoLogisticsExpressUpdatePickupRequest
from openapi_client.models.supermodel_io_logistics_express_update_pickup_response import SupermodelIoLogisticsExpressUpdatePickupResponse
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
    api_instance = openapi_client.PickupApi(api_client)
    dispatch_confirmation_number = 'PRG999126012345' # str | Shipment pickup confirmation number for example `PRG999126012345`
    supermodel_io_logistics_express_update_pickup_request = openapi_client.SupermodelIoLogisticsExpressUpdatePickupRequest() # SupermodelIoLogisticsExpressUpdatePickupRequest | Details about the requested pickup updates
    message_reference = 'd0e7832e-5c98-11ea-bc55-0242ac13' # str | Please provide message reference  (optional)
    message_reference_date = 'Wed, 21 Oct 2015 07:28:00 GMT' # str | Optional reference date in the  HTTP-date format https://tools.ietf.org/html/rfc7231#section-7.1.1.2 (optional)
    plugin_name = ' ' # str | Please provide name of the plugin (applicable to 3PV only)  (optional)
    plugin_version = ' ' # str | Please provide version of the plugin (applicable to 3PV only)  (optional)
    shipping_system_platform_name = ' ' # str | Please provide name of the shipping platform(applicable to 3PV only)  (optional)
    shipping_system_platform_version = ' ' # str | Please provide version of the shipping platform (applicable to 3PV only)  (optional)
    webstore_platform_name = ' ' # str | Please provide name of the webstore platform (applicable to 3PV only)  (optional)
    webstore_platform_version = ' ' # str | Please provide version of the webstore platform (applicable to 3PV only)  (optional)

    try:
        # Update pickup information for an existing DHL Express pickup booking request
        api_response = api_instance.exp_api_pickups_update(dispatch_confirmation_number, supermodel_io_logistics_express_update_pickup_request, message_reference=message_reference, message_reference_date=message_reference_date, plugin_name=plugin_name, plugin_version=plugin_version, shipping_system_platform_name=shipping_system_platform_name, shipping_system_platform_version=shipping_system_platform_version, webstore_platform_name=webstore_platform_name, webstore_platform_version=webstore_platform_version)
        print("The response of PickupApi->exp_api_pickups_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PickupApi->exp_api_pickups_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dispatch_confirmation_number** | **str**| Shipment pickup confirmation number for example &#x60;PRG999126012345&#x60; | 
 **supermodel_io_logistics_express_update_pickup_request** | [**SupermodelIoLogisticsExpressUpdatePickupRequest**](SupermodelIoLogisticsExpressUpdatePickupRequest.md)| Details about the requested pickup updates | 
 **message_reference** | **str**| Please provide message reference  | [optional] 
 **message_reference_date** | **str**| Optional reference date in the  HTTP-date format https://tools.ietf.org/html/rfc7231#section-7.1.1.2 | [optional] 
 **plugin_name** | **str**| Please provide name of the plugin (applicable to 3PV only)  | [optional] 
 **plugin_version** | **str**| Please provide version of the plugin (applicable to 3PV only)  | [optional] 
 **shipping_system_platform_name** | **str**| Please provide name of the shipping platform(applicable to 3PV only)  | [optional] 
 **shipping_system_platform_version** | **str**| Please provide version of the shipping platform (applicable to 3PV only)  | [optional] 
 **webstore_platform_name** | **str**| Please provide name of the webstore platform (applicable to 3PV only)  | [optional] 
 **webstore_platform_version** | **str**| Please provide version of the webstore platform (applicable to 3PV only)  | [optional] 

### Return type

[**SupermodelIoLogisticsExpressUpdatePickupResponse**](SupermodelIoLogisticsExpressUpdatePickupResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Pickup updated |  -  |
**400** | Wrong input parameters |  * Content-Type -  <br>  |
**404** | Pickup not found |  * Content-Type -  <br>  |
**422** | Unprocessable Entity |  * Content-Type -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

