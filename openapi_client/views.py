# api/views.py

from django.http import JsonResponse
from rest_framework.decorators import api_view

from .api import (
    address_api, identifier_api, invoice_api, pickup_api,
    product_api, rating_api, reference_data_api, servicepoint_api,
    shipment_api, tracking_api
)
import urllib3
import ssl
import requests

# Disable warnings for SSL verification (for development purposes only)
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


@api_view(['GET'])
def address_validate_view(request):
    api_instance = address_api.AddressApi()
    try:
        response = api_instance.exp_api_address_validate(
            type=request.GET.get('type'),
            country_code=request.GET.get('CZ'),
            postal_code=request.GET.get('14800'),
            city_name=request.GET.get('Prague'),
            county_name=request.GET.get('praha'),
            strict_validation=request.GET.get('TRUE'),
            message_reference=request.GET.get('d0e7832e-5c98-11ea-bc55-0242ac13'),
            message_reference_date=request.GET.get('Wed, 21 Oct 2015 07:28:00 GMT'),
            plugin_name=request.GET.get(''),
            plugin_version=request.GET.get(''),
            shipping_system_platform_name=request.GET.get(''),
            shipping_system_platform_version=request.GET.get(''),
            webstore_platform_name=request.GET.get(''),
            webstore_platform_version=request.GET.get('')
        )
        return JsonResponse(response.to_dict())
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=400)


@api_view(['GET'])
def identifier_view(request):
    api_instance = identifier_api.IdentifierApi()
    try:
        response = api_instance.exp_api_identifier(
            type=request.GET.get('type'),
            message_reference=request.GET.get('message_reference'),
            message_reference_date=request.GET.get('message_reference_date'),
            plugin_name=request.GET.get('plugin_name'),
            plugin_version=request.GET.get('plugin_version'),
            shipping_system_platform_name=request.GET.get('shipping_system_platform_name'),
            shipping_system_platform_version=request.GET.get('shipping_system_platform_version'),
            webstore_platform_name=request.GET.get('webstore_platform_name'),
            webstore_platform_version=request.GET.get('webstore_platform_version')
        )
        return JsonResponse(response.to_dict())
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=400)


@api_view(['GET'])
def invoice_view(request):
    api_instance = invoice_api.InvoiceApi()
    try:
        response = api_instance.exp_api_invoice(
            message_reference=request.GET.get('message_reference'),
            message_reference_date=request.GET.get('message_reference_date'),
            plugin_name=request.GET.get('plugin_name'),
            plugin_version=request.GET.get('plugin_version'),
            shipping_system_platform_name=request.GET.get('shipping_system_platform_name'),
            shipping_system_platform_version=request.GET.get('shipping_system_platform_version'),
            webstore_platform_name=request.GET.get('webstore_platform_name'),
            webstore_platform_version=request.GET.get('webstore_platform_version')
        )
        return JsonResponse(response.to_dict())
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=400)



@api_view(['GET'])
def ratings_view(request):
    url = "https://api-mock.dhl.com/mydhlapi/rates"
    headers = {
        'Message-Reference': request.GET.get('message_reference', 'SOME_STRING_VALUE'),
        'Message-Reference-Date': request.GET.get('message_reference_date', 'SOME_STRING_VALUE'),
        'Plugin-Name': request.GET.get('plugin_name', 'SOME_STRING_VALUE'),
        'Plugin-Version': request.GET.get('plugin_version', 'SOME_STRING_VALUE'),
        'Shipping-System-Platform-Name': request.GET.get('shipping_system_platform_name', 'SOME_STRING_VALUE'),
        'Shipping-System-Platform-Version': request.GET.get('shipping_system_platform_version', 'SOME_STRING_VALUE'),
        'Webstore-Platform-Name': request.GET.get('webstore_platform_name', 'SOME_STRING_VALUE'),
        'Webstore-Platform-Version': request.GET.get('webstore_platform_version', 'SOME_STRING_VALUE'),
        'Authorization': 'Basic REPLACE_BASIC_AUTH'
    }
    params = {
        'accountNumber': request.GET.get('accountNumber', '123456789'),
        'originCountryCode': request.GET.get('originCountryCode', 'CZ'),
        'originCityName': request.GET.get('originCityName', 'Prague'),
        'destinationCountryCode': request.GET.get('destinationCountryCode', 'CZ'),
        'destinationCityName': request.GET.get('destinationCityName', 'Prague'),
        'weight': request.GET.get('weight', '5'),
        'length': request.GET.get('length', '15'),
        'width': request.GET.get('width', '10'),
        'height': request.GET.get('height', '5'),
        'plannedShippingDate': request.GET.get('plannedShippingDate', '2020-02-26'),
        'isCustomsDeclarable': request.GET.get('isCustomsDeclarable', 'false').lower() == 'true',
        'unitOfMeasurement': request.GET.get('unitOfMeasurement', 'metric'),
        'nextBusinessDay': request.GET.get('nextBusinessDay', 'false').lower() == 'true',
        'strictValidation': request.GET.get('strictValidation', 'false').lower() == 'true',
        'getAllValueAddedServices': request.GET.get('getAllValueAddedServices', 'false').lower() == 'true',
        'requestEstimatedDeliveryDate': request.GET.get('requestEstimatedDeliveryDate', 'true').lower() == 'true',
        'estimatedDeliveryDateType': request.GET.get('estimatedDeliveryDateType', 'QDDF')
    }

    response = requests.get(url, headers=headers, params=params, verify=False)

    if response.status_code == 200:
        return JsonResponse(response.json(), safe=False)
    else:
        return JsonResponse({'error': response.text}, status=response.status_code)


