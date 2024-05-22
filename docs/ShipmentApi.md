# openapi_client.ShipmentApi

All URIs are relative to *https://api-mock.dhl.com/mydhlapi*

Method | HTTP request | Description
------------- | ------------- | -------------
[**exp_api_shipments**](ShipmentApi.md#exp_api_shipments) | **POST** /shipments | Create Shipment
[**exp_api_shipments_documentimage**](ShipmentApi.md#exp_api_shipments_documentimage) | **GET** /shipments/{shipmentTrackingNumber}/get-image | Get Image
[**exp_api_shipments_epod**](ShipmentApi.md#exp_api_shipments_epod) | **GET** /shipments/{shipmentTrackingNumber}/proof-of-delivery | Electronic Proof of Delivery
[**exp_api_shipments_img_upload**](ShipmentApi.md#exp_api_shipments_img_upload) | **PATCH** /shipments/{shipmentTrackingNumber}/upload-image | Upload Paperless Trade shipment (PLT) images of previously created shipment.
[**exp_api_shipments_invoice_data_awb**](ShipmentApi.md#exp_api_shipments_invoice_data_awb) | **PATCH** /shipments/{shipmentTrackingNumber}/upload-invoice-data | Upload Commercial Invoice data for your DHL Express shipment


# **exp_api_shipments**
> SupermodelIoLogisticsExpressCreateShipmentResponse exp_api_shipments(supermodel_io_logistics_express_create_shipment_request, message_reference=message_reference, message_reference_date=message_reference_date, plugin_name=plugin_name, plugin_version=plugin_version, shipping_system_platform_name=shipping_system_platform_name, shipping_system_platform_version=shipping_system_platform_version, webstore_platform_name=webstore_platform_name, webstore_platform_version=webstore_platform_version, strict_validation=strict_validation, bypass_plt_error=bypass_plt_error, validate_data_only=validate_data_only)

Create Shipment

## Create Shipment The ShipmentRequest Operation will allow you to generate an AWB number and piece IDs, generate a shipping label, transmit manifest shipment detail to DHL, and optionally book a courier for the pickup of a shipment. The key elements in the response of the Shipment Request will be a base64 encoded PDF label and the Shipment and Piece identification numbers, which you can use for tracking on the DHL web site. While the RateRequest and ShipmentRequest services can be used independently, DHL recommends the use of RateRequest to first validate the products available for the shipper/receiver. The global product codes which are output during the RateResponse can be used directly as input into the Shipment Request, as both perform similar validations in terms of service capability. 

### Example

* Basic Authentication (basicAuth):

```python
import openapi_client
from openapi_client.models.supermodel_io_logistics_express_create_shipment_request import SupermodelIoLogisticsExpressCreateShipmentRequest
from openapi_client.models.supermodel_io_logistics_express_create_shipment_response import SupermodelIoLogisticsExpressCreateShipmentResponse
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
    api_instance = openapi_client.ShipmentApi(api_client)
    supermodel_io_logistics_express_create_shipment_request = openapi_client.SupermodelIoLogisticsExpressCreateShipmentRequest() # SupermodelIoLogisticsExpressCreateShipmentRequest | Details about the shipment to be created
    message_reference = 'd0e7832e-5c98-11ea-bc55-0242ac13' # str | Please provide message reference  (optional)
    message_reference_date = 'Wed, 21 Oct 2015 07:28:00 GMT' # str | Optional reference date in the  HTTP-date format https://tools.ietf.org/html/rfc7231#section-7.1.1.2 (optional)
    plugin_name = ' ' # str | Please provide name of the plugin (applicable to 3PV only)  (optional)
    plugin_version = ' ' # str | Please provide version of the plugin (applicable to 3PV only)  (optional)
    shipping_system_platform_name = ' ' # str | Please provide name of the shipping platform(applicable to 3PV only)  (optional)
    shipping_system_platform_version = ' ' # str | Please provide version of the shipping platform (applicable to 3PV only)  (optional)
    webstore_platform_name = ' ' # str | Please provide name of the webstore platform (applicable to 3PV only)  (optional)
    webstore_platform_version = ' ' # str | Please provide version of the webstore platform (applicable to 3PV only)  (optional)
    strict_validation = False # bool | If set to true, indicate strict DCT validation of address details, and validation of product and service(s) combination provided in request. (optional) (default to False)
    bypass_plt_error = false # bool | Option to bypass PLT - WY service code lane capability validation  (optional)
    validate_data_only = False # bool | If set to true, indicate to perform shipment data compliant validation on the shipment information. (optional) (default to False)

    try:
        # Create Shipment
        api_response = api_instance.exp_api_shipments(supermodel_io_logistics_express_create_shipment_request, message_reference=message_reference, message_reference_date=message_reference_date, plugin_name=plugin_name, plugin_version=plugin_version, shipping_system_platform_name=shipping_system_platform_name, shipping_system_platform_version=shipping_system_platform_version, webstore_platform_name=webstore_platform_name, webstore_platform_version=webstore_platform_version, strict_validation=strict_validation, bypass_plt_error=bypass_plt_error, validate_data_only=validate_data_only)
        print("The response of ShipmentApi->exp_api_shipments:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ShipmentApi->exp_api_shipments: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **supermodel_io_logistics_express_create_shipment_request** | [**SupermodelIoLogisticsExpressCreateShipmentRequest**](SupermodelIoLogisticsExpressCreateShipmentRequest.md)| Details about the shipment to be created | 
 **message_reference** | **str**| Please provide message reference  | [optional] 
 **message_reference_date** | **str**| Optional reference date in the  HTTP-date format https://tools.ietf.org/html/rfc7231#section-7.1.1.2 | [optional] 
 **plugin_name** | **str**| Please provide name of the plugin (applicable to 3PV only)  | [optional] 
 **plugin_version** | **str**| Please provide version of the plugin (applicable to 3PV only)  | [optional] 
 **shipping_system_platform_name** | **str**| Please provide name of the shipping platform(applicable to 3PV only)  | [optional] 
 **shipping_system_platform_version** | **str**| Please provide version of the shipping platform (applicable to 3PV only)  | [optional] 
 **webstore_platform_name** | **str**| Please provide name of the webstore platform (applicable to 3PV only)  | [optional] 
 **webstore_platform_version** | **str**| Please provide version of the webstore platform (applicable to 3PV only)  | [optional] 
 **strict_validation** | **bool**| If set to true, indicate strict DCT validation of address details, and validation of product and service(s) combination provided in request. | [optional] [default to False]
 **bypass_plt_error** | **bool**| Option to bypass PLT - WY service code lane capability validation  | [optional] 
 **validate_data_only** | **bool**| If set to true, indicate to perform shipment data compliant validation on the shipment information. | [optional] [default to False]

### Return type

[**SupermodelIoLogisticsExpressCreateShipmentResponse**](SupermodelIoLogisticsExpressCreateShipmentResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Shipment Created |  * Location - Location of the created resource e.g. &#x60;/shipments/1117120421&#x60; <br>  * Message-Reference - Message reference provided by customer as part of request or automatically generated when not provided <br>  * Invocation-Id - Unique identifier of the transaction <br>  |
**400** | Wrong input parameters |  * Content-Type -  <br>  |
**422** | Wrong input parameters |  * Content-Type -  <br>  |
**500** | Process errors |  * Content-Type -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **exp_api_shipments_documentimage**
> SupermodelIoLogisticsExpressDocumentImageResponse exp_api_shipments_documentimage(shipment_tracking_number, shipper_account_number, type_code, pickup_year_and_month, encoding_format=encoding_format, all_in_one_pdf=all_in_one_pdf, compressed_package=compressed_package, message_reference=message_reference, message_reference_date=message_reference_date, plugin_name=plugin_name, plugin_version=plugin_version, shipping_system_platform_name=shipping_system_platform_name, shipping_system_platform_version=shipping_system_platform_version, webstore_platform_name=webstore_platform_name, webstore_platform_version=webstore_platform_version)

Get Image

The Get Image service can be used to retrieve customer's own uploaded Commercial Invoice, Waybill Document  or supporting documents that uploaded during shipment creation.  

### Example

* Basic Authentication (basicAuth):

```python
import openapi_client
from openapi_client.models.supermodel_io_logistics_express_document_image_response import SupermodelIoLogisticsExpressDocumentImageResponse
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
    api_instance = openapi_client.ShipmentApi(api_client)
    shipment_tracking_number = '9356579890' # str | DHL Express shipment identification number
    shipper_account_number = '123456789' # str | DHL Express customer shipper account number
    type_code = 'type_code_example' # str | Please provide correct document type.
    pickup_year_and_month = 'YYYY-MM' # str | Please provide the pickup's date in YYYY-MM format 
    encoding_format = 'encoding_format_example' # str | Please provide the document image encoding format in pdf or tiff format  (optional)
    all_in_one_pdf = false # bool | Option to return all the document images in a single PDF file  (optional)
    compressed_package = false # bool | Option to return all the document images in a compressed package  (optional)
    message_reference = 'd0e7832e-5c98-11ea-bc55-0242ac13' # str | Please provide message reference  (optional)
    message_reference_date = 'Wed, 21 Oct 2015 07:28:00 GMT' # str | Optional reference date in the  HTTP-date format https://tools.ietf.org/html/rfc7231#section-7.1.1.2 (optional)
    plugin_name = ' ' # str | Please provide name of the plugin (applicable to 3PV only)  (optional)
    plugin_version = ' ' # str | Please provide version of the plugin (applicable to 3PV only)  (optional)
    shipping_system_platform_name = ' ' # str | Please provide name of the shipping platform(applicable to 3PV only)  (optional)
    shipping_system_platform_version = ' ' # str | Please provide version of the shipping platform (applicable to 3PV only)  (optional)
    webstore_platform_name = ' ' # str | Please provide name of the webstore platform (applicable to 3PV only)  (optional)
    webstore_platform_version = ' ' # str | Please provide version of the webstore platform (applicable to 3PV only)  (optional)

    try:
        # Get Image
        api_response = api_instance.exp_api_shipments_documentimage(shipment_tracking_number, shipper_account_number, type_code, pickup_year_and_month, encoding_format=encoding_format, all_in_one_pdf=all_in_one_pdf, compressed_package=compressed_package, message_reference=message_reference, message_reference_date=message_reference_date, plugin_name=plugin_name, plugin_version=plugin_version, shipping_system_platform_name=shipping_system_platform_name, shipping_system_platform_version=shipping_system_platform_version, webstore_platform_name=webstore_platform_name, webstore_platform_version=webstore_platform_version)
        print("The response of ShipmentApi->exp_api_shipments_documentimage:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ShipmentApi->exp_api_shipments_documentimage: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **shipment_tracking_number** | **str**| DHL Express shipment identification number | 
 **shipper_account_number** | **str**| DHL Express customer shipper account number | 
 **type_code** | **str**| Please provide correct document type. | 
 **pickup_year_and_month** | **str**| Please provide the pickup&#39;s date in YYYY-MM format  | 
 **encoding_format** | **str**| Please provide the document image encoding format in pdf or tiff format  | [optional] 
 **all_in_one_pdf** | **bool**| Option to return all the document images in a single PDF file  | [optional] 
 **compressed_package** | **bool**| Option to return all the document images in a compressed package  | [optional] 
 **message_reference** | **str**| Please provide message reference  | [optional] 
 **message_reference_date** | **str**| Optional reference date in the  HTTP-date format https://tools.ietf.org/html/rfc7231#section-7.1.1.2 | [optional] 
 **plugin_name** | **str**| Please provide name of the plugin (applicable to 3PV only)  | [optional] 
 **plugin_version** | **str**| Please provide version of the plugin (applicable to 3PV only)  | [optional] 
 **shipping_system_platform_name** | **str**| Please provide name of the shipping platform(applicable to 3PV only)  | [optional] 
 **shipping_system_platform_version** | **str**| Please provide version of the shipping platform (applicable to 3PV only)  | [optional] 
 **webstore_platform_name** | **str**| Please provide name of the webstore platform (applicable to 3PV only)  | [optional] 
 **webstore_platform_version** | **str**| Please provide version of the webstore platform (applicable to 3PV only)  | [optional] 

### Return type

[**SupermodelIoLogisticsExpressDocumentImageResponse**](SupermodelIoLogisticsExpressDocumentImageResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Document Image found |  * Invocation-Id - Unique identifier of the transaction <br>  * Message-Reference - Message reference provided by customer as part of request or automatically generated when not provided <br>  * Content-Language -  <br>  |
**400** | Wrong input parameters |  * Content-Type -  <br>  |
**404** | No document image found |  * Content-Type -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **exp_api_shipments_epod**
> SupermodelIoLogisticsExpressEPODResponse exp_api_shipments_epod(shipment_tracking_number, shipper_account_number=shipper_account_number, content=content, message_reference=message_reference, message_reference_date=message_reference_date, plugin_name=plugin_name, plugin_version=plugin_version, shipping_system_platform_name=shipping_system_platform_name, shipping_system_platform_version=shipping_system_platform_version, webstore_platform_name=webstore_platform_name, webstore_platform_version=webstore_platform_version)

Electronic Proof of Delivery

The electronic proof of delivery service can be used to retrieve proof of delivery for certain delivered DHL Express shipments 

### Example

* Basic Authentication (basicAuth):

```python
import openapi_client
from openapi_client.models.supermodel_io_logistics_express_epod_response import SupermodelIoLogisticsExpressEPODResponse
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
    api_instance = openapi_client.ShipmentApi(api_client)
    shipment_tracking_number = '9356579890' # str | DHL Express shipment identification number
    shipper_account_number = '123456789' # str | DHL Express customer shipper account number (optional)
    content = 'epod-summary' # str |  (optional) (default to 'epod-summary')
    message_reference = 'd0e7832e-5c98-11ea-bc55-0242ac13' # str | Please provide message reference  (optional)
    message_reference_date = 'Wed, 21 Oct 2015 07:28:00 GMT' # str | Optional reference date in the  HTTP-date format https://tools.ietf.org/html/rfc7231#section-7.1.1.2 (optional)
    plugin_name = ' ' # str | Please provide name of the plugin (applicable to 3PV only)  (optional)
    plugin_version = ' ' # str | Please provide version of the plugin (applicable to 3PV only)  (optional)
    shipping_system_platform_name = ' ' # str | Please provide name of the shipping platform(applicable to 3PV only)  (optional)
    shipping_system_platform_version = ' ' # str | Please provide version of the shipping platform (applicable to 3PV only)  (optional)
    webstore_platform_name = ' ' # str | Please provide name of the webstore platform (applicable to 3PV only)  (optional)
    webstore_platform_version = ' ' # str | Please provide version of the webstore platform (applicable to 3PV only)  (optional)

    try:
        # Electronic Proof of Delivery
        api_response = api_instance.exp_api_shipments_epod(shipment_tracking_number, shipper_account_number=shipper_account_number, content=content, message_reference=message_reference, message_reference_date=message_reference_date, plugin_name=plugin_name, plugin_version=plugin_version, shipping_system_platform_name=shipping_system_platform_name, shipping_system_platform_version=shipping_system_platform_version, webstore_platform_name=webstore_platform_name, webstore_platform_version=webstore_platform_version)
        print("The response of ShipmentApi->exp_api_shipments_epod:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ShipmentApi->exp_api_shipments_epod: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **shipment_tracking_number** | **str**| DHL Express shipment identification number | 
 **shipper_account_number** | **str**| DHL Express customer shipper account number | [optional] 
 **content** | **str**|  | [optional] [default to &#39;epod-summary&#39;]
 **message_reference** | **str**| Please provide message reference  | [optional] 
 **message_reference_date** | **str**| Optional reference date in the  HTTP-date format https://tools.ietf.org/html/rfc7231#section-7.1.1.2 | [optional] 
 **plugin_name** | **str**| Please provide name of the plugin (applicable to 3PV only)  | [optional] 
 **plugin_version** | **str**| Please provide version of the plugin (applicable to 3PV only)  | [optional] 
 **shipping_system_platform_name** | **str**| Please provide name of the shipping platform(applicable to 3PV only)  | [optional] 
 **shipping_system_platform_version** | **str**| Please provide version of the shipping platform (applicable to 3PV only)  | [optional] 
 **webstore_platform_name** | **str**| Please provide name of the webstore platform (applicable to 3PV only)  | [optional] 
 **webstore_platform_version** | **str**| Please provide version of the webstore platform (applicable to 3PV only)  | [optional] 

### Return type

[**SupermodelIoLogisticsExpressEPODResponse**](SupermodelIoLogisticsExpressEPODResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Electronic Proof of delivery found |  * Invocation-Id - Unique identifier of the transaction <br>  * Message-Reference - Message reference provided by customer as part of request or automatically generated when not provided <br>  * Content-Language -  <br>  |
**400** | Wrong input parameters |  * Content-Type -  <br>  |
**404** | No electronic proof of delivery found |  * Content-Type -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **exp_api_shipments_img_upload**
> exp_api_shipments_img_upload(shipment_tracking_number, supermodel_io_logistics_express_image_upload_request)

Upload Paperless Trade shipment (PLT) images of previously created shipment.

The upload-image service can be used to upload PLT images to a previously created shipment.  The PLT images for the shipment can be uploaded before the shipment has been physically  collected by DHL courier. However, the original shipment must contain WY as the special service otherwise,  an error will be returned when the customer wants to use the reupload function in this upload-image service.     IMPORTANT: Please note that at least 10mins must be given between the initial createShipment request and then  the upload-image request (including subsequent upload-image request).  

### Example

* Basic Authentication (basicAuth):

```python
import openapi_client
from openapi_client.models.supermodel_io_logistics_express_image_upload_request import SupermodelIoLogisticsExpressImageUploadRequest
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
    api_instance = openapi_client.ShipmentApi(api_client)
    shipment_tracking_number = '9356579890' # str | DHL Express shipment identification number
    supermodel_io_logistics_express_image_upload_request = openapi_client.SupermodelIoLogisticsExpressImageUploadRequest() # SupermodelIoLogisticsExpressImageUploadRequest | Details about the shipment images

    try:
        # Upload Paperless Trade shipment (PLT) images of previously created shipment.
        api_instance.exp_api_shipments_img_upload(shipment_tracking_number, supermodel_io_logistics_express_image_upload_request)
    except Exception as e:
        print("Exception when calling ShipmentApi->exp_api_shipments_img_upload: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **shipment_tracking_number** | **str**| DHL Express shipment identification number | 
 **supermodel_io_logistics_express_image_upload_request** | [**SupermodelIoLogisticsExpressImageUploadRequest**](SupermodelIoLogisticsExpressImageUploadRequest.md)| Details about the shipment images | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Images uploaded |  * Invocation-Id - Unique identifier of the transaction <br>  * Message-Reference - Message reference provided by customer as part of request or automatically generated when not provided <br>  * Content-Language -  <br>  |
**400** | Wrong input parameters |  * Content-Type -  <br>  |
**404** | No shipment details found |  * Content-Type -  <br>  |
**422** | Unprocessable Entity |  * Content-Type -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **exp_api_shipments_invoice_data_awb**
> exp_api_shipments_invoice_data_awb(shipment_tracking_number, supermodel_io_logistics_express_upload_invoice_data_request, message_reference=message_reference, message_reference_date=message_reference_date, plugin_name=plugin_name, plugin_version=plugin_version, shipping_system_platform_name=shipping_system_platform_name, shipping_system_platform_version=shipping_system_platform_version, webstore_platform_name=webstore_platform_name, webstore_platform_version=webstore_platform_version)

Upload Commercial Invoice data for your DHL Express shipment

## Upload Invoice Data with Shipment ID The upload invoice data service can be used to upload Commerical Invoice data with Shipment Identification Number for your DHL Express shipment.Customer can provide Commercial Invoice data before Shipment Data via Create Shipment flow or vice versa.  Important Note: UploadInvoiceData service is not enabled by default and must be requested per customer. Use of this service is only enabled on exceptional basis and DHL Express recommends to submit shipment requests together with a commercial invoice data.To enable use of UploadInvoiceData service, please contact your DHL Express IT representative. To use UploadInvoiceData service, it is required that \"PM\" service code is provided in MyDHL API Create Shipment request. \"PM\" service code is not enabled by  default for the customers, and needs to be enabled upon request.  When Shipment is created via MyDHL API Create Shipment service before uploading the Commercial Invoice (CIN) data,it is mandatory to provide the Shipment Identification Number as received in MyDHL API Create Shipment service Response. When Commercial Invoice (CIN) data is uploaded prior to creating a shipment via MyDHL API Create Shipment service, it is mandatory to provide Invoice Reference Number with Invoice Reference Type value \"CU\" and Shipper Account Number.   These elements are mandatory to facilitate an effective data merge of the Commercial Invoice (CIN) data with Shipment Data. As an output customer will receive Notification element value '0' on successful upload of Commercial Invoice (CIN) data.  DHL backend application performs the subsequent data merging process of the Shipment Data and Commercial Invoice data. 

### Example

* Basic Authentication (basicAuth):

```python
import openapi_client
from openapi_client.models.supermodel_io_logistics_express_upload_invoice_data_request import SupermodelIoLogisticsExpressUploadInvoiceDataRequest
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
    api_instance = openapi_client.ShipmentApi(api_client)
    shipment_tracking_number = '9356579890' # str | DHL Express shipment identification number
    supermodel_io_logistics_express_upload_invoice_data_request = openapi_client.SupermodelIoLogisticsExpressUploadInvoiceDataRequest() # SupermodelIoLogisticsExpressUploadInvoiceDataRequest | Details about the invoice data
    message_reference = 'd0e7832e-5c98-11ea-bc55-0242ac13' # str | Please provide message reference  (optional)
    message_reference_date = 'Wed, 21 Oct 2015 07:28:00 GMT' # str | Optional reference date in the  HTTP-date format https://tools.ietf.org/html/rfc7231#section-7.1.1.2 (optional)
    plugin_name = ' ' # str | Please provide name of the plugin (applicable to 3PV only)  (optional)
    plugin_version = ' ' # str | Please provide version of the plugin (applicable to 3PV only)  (optional)
    shipping_system_platform_name = ' ' # str | Please provide name of the shipping platform(applicable to 3PV only)  (optional)
    shipping_system_platform_version = ' ' # str | Please provide version of the shipping platform (applicable to 3PV only)  (optional)
    webstore_platform_name = ' ' # str | Please provide name of the webstore platform (applicable to 3PV only)  (optional)
    webstore_platform_version = ' ' # str | Please provide version of the webstore platform (applicable to 3PV only)  (optional)

    try:
        # Upload Commercial Invoice data for your DHL Express shipment
        api_instance.exp_api_shipments_invoice_data_awb(shipment_tracking_number, supermodel_io_logistics_express_upload_invoice_data_request, message_reference=message_reference, message_reference_date=message_reference_date, plugin_name=plugin_name, plugin_version=plugin_version, shipping_system_platform_name=shipping_system_platform_name, shipping_system_platform_version=shipping_system_platform_version, webstore_platform_name=webstore_platform_name, webstore_platform_version=webstore_platform_version)
    except Exception as e:
        print("Exception when calling ShipmentApi->exp_api_shipments_invoice_data_awb: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **shipment_tracking_number** | **str**| DHL Express shipment identification number | 
 **supermodel_io_logistics_express_upload_invoice_data_request** | [**SupermodelIoLogisticsExpressUploadInvoiceDataRequest**](SupermodelIoLogisticsExpressUploadInvoiceDataRequest.md)| Details about the invoice data | 
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

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | invoice data uploaded |  * Invocation-Id - Unique identifier of the transaction <br>  * Message-Reference - Message reference provided by customer as part of request or automatically generated when not provided <br>  * Content-Language -  <br>  |
**400** | Wrong input parameters |  * Content-Type -  <br>  |
**422** | Unprocessable Entity |  * Content-Type -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

