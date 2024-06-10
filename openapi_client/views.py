# api/views.py
import os
import ssl
import json
import urllib3
import requests

from django.shortcuts import render
from django.http import JsonResponse
from django.shortcuts import redirect, render
from rest_framework.decorators import api_view

# from app.forms import ShipmentForm

from .api import (
    address_api, identifier_api, invoice_api, pickup_api,
    product_api, rating_api, reference_data_api, servicepoint_api,
    shipment_api, tracking_api
)

from openapi_client import Configuration
from openapi_client import ApiClient

from openapi_client.forms import AddressValidateForm


# Disable warnings for SSL verification (for development purposes only)
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


def address_validate_view_EXAMPLE(request):
    # Example with django templates
    if request.method == 'POST':
        form = AddressValidateForm(request.POST)

        if form.is_valid():
            api_instance = address_api.AddressApi()

            response = api_instance.exp_api_address_validate(
                type=form.cleaned_data.get('type_'),
                country_code=form.cleaned_data.get('country_code'),
                postal_code=form.cleaned_data.get('postal_code'),
                city_name=form.cleaned_data.get('city_name'),
                county_name=form.cleaned_data.get('county_name'),
                strict_validation=form.cleaned_data.get('strict_validation'),
                message_reference=form.cleaned_data.get('message_reference'),
                message_reference_date=form.cleaned_data.get('message_reference_date'),
                plugin_name=form.cleaned_data.get('plugin_name'),
                plugin_version=form.cleaned_data.get('plugin_version'),
                shipping_system_platform_name=form.cleaned_data.get('shipping_system_platform_name'),
                shipping_system_platform_version=form.cleaned_data.get('shipping_system_platform_version'),
                webstore_platform_name=form.cleaned_data.get('webstore_platform_name'),
                webstore_platform_version=form.cleaned_data.get('webstore_platform_version'),
            )

            # You can do whatever you want with the response. I'll just pass it to the template
            # and display it for this example
            result = json.dumps(response.to_dict())
        else:
            result = None

    else:
        form = AddressValidateForm
        result = None

    context = {
        'form': form,
        'result': result
    }
    return render(request, 'address_validate.html', context)


@api_view(['GET'])
def test_endpoint(request):
    return JsonResponse({'message': 'Hello, World!'})


@api_view(['GET'])
def address_validate_view(request):
    api_instance = address_api.AddressApi()
    try:
        response = api_instance.exp_api_address_validate(
            type=request.GET.get('type'),
            country_code=request.GET.get('countryCode'),
            postal_code=request.GET.get('postalCode'),
            city_name=request.GET.get('cityName'),
            county_name=request.GET.get('countyName'),
            strict_validation=request.GET.get('strictValidation'),
            message_reference=request.GET.get('messageReference'),
            message_reference_date=request.GET.get('messageReferenceDate'),
            plugin_name=request.GET.get('pluginName'),
            plugin_version=request.GET.get('pluginVersion'),
            shipping_system_platform_name=request.GET.get('shippingSystemPlatformName'),
            shipping_system_platform_version=request.GET.get('shippingSystemPlatformVersion'),
            webstore_platform_name=request.GET.get('webstorePlatformName'),
            webstore_platform_version=request.GET.get('webstorePlatformVersion')
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



# @api_view(['GET'])
# def ratings_view(request):
#     url = "https://api-mock.dhl.com/mydhlapi/rates"
#     headers = {
#         'Message-Reference': request.GET.get('message_reference', 'SOME_STRING_VALUE'),
#         'Message-Reference-Date': request.GET.get('message_reference_date', 'SOME_STRING_VALUE'),
#         'Plugin-Name': request.GET.get('plugin_name', 'SOME_STRING_VALUE'),
#         'Plugin-Version': request.GET.get('plugin_version', 'SOME_STRING_VALUE'),
#         'Shipping-System-Platform-Name': request.GET.get('shipping_system_platform_name', 'SOME_STRING_VALUE'),
#         'Shipping-System-Platform-Version': request.GET.get('shipping_system_platform_version', 'SOME_STRING_VALUE'),
#         'Webstore-Platform-Name': request.GET.get('webstore_platform_name', 'SOME_STRING_VALUE'),
#         'Webstore-Platform-Version': request.GET.get('webstore_platform_version', 'SOME_STRING_VALUE'),
#         'Authorization': 'Basic REPLACE_BASIC_AUTH'
#     }
#     params = {
#         'accountNumber': request.GET.get('accountNumber', '123456789'),
#         'originCountryCode': request.GET.get('originCountryCode', 'CZ'),
#         'originCityName': request.GET.get('originCityName', 'Prague'),
#         'destinationCountryCode': request.GET.get('destinationCountryCode', 'CZ'),
#         'destinationCityName': request.GET.get('destinationCityName', 'Prague'),
#         'weight': request.GET.get('weight', '5'),
#         'length': request.GET.get('length', '15'),
#         'width': request.GET.get('width', '10'),
#         'height': request.GET.get('height', '5'),
#         'plannedShippingDate': request.GET.get('plannedShippingDate', '2020-02-26'),
#         'isCustomsDeclarable': request.GET.get('isCustomsDeclarable', 'false').lower() == 'true',
#         'unitOfMeasurement': request.GET.get('unitOfMeasurement', 'metric'),
#         'nextBusinessDay': request.GET.get('nextBusinessDay', 'false').lower() == 'true',
#         'strictValidation': request.GET.get('strictValidation', 'false').lower() == 'true',
#         'getAllValueAddedServices': request.GET.get('getAllValueAddedServices', 'false').lower() == 'true',
#         'requestEstimatedDeliveryDate': request.GET.get('requestEstimatedDeliveryDate', 'true').lower() == 'true',
#         'estimatedDeliveryDateType': request.GET.get('estimatedDeliveryDateType', 'QDDF')
#     }

#     response = requests.get(url, headers=headers, params=params, verify=False)

#     if response.status_code == 200:
#         return JsonResponse(response.json(), safe=False)
#     else:
#         return JsonResponse({'error': response.text}, status=response.status_code)


