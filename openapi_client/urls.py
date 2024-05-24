from django.urls import path
from django.http import JsonResponse
from rest_framework.decorators import api_view
from .api import (
    address_api, identifier_api, invoice_api, pickup_api,
    product_api, rating_api, reference_data_api, servicepoint_api,
    shipment_api, tracking_api
)

@api_view(['GET'])
def address_validate_view(request):
    api_instance = address_api.AddressApi()
    try:
        response = api_instance.exp_api_address_validate(
            type=request.GET.get('type'),
            country_code=request.GET.get('country_code'),
            postal_code=request.GET.get('postal_code'),
            city_name=request.GET.get('city_name'),
            county_name=request.GET.get('county_name'),
            strict_validation=request.GET.get('strict_validation'),
            message_reference=request.GET.get('message_reference'),
            message_reference_date=request.GET.get('message_reference_date'),
            plugin_name=request.GET.get('plugin_name'),
            plugin_version=request.GET.get('plugin_version'),
            shipping_system_platform_name=request.GET.get('shipping_system_platform_name'),
            shipping_system_platform_version=request.GET.get('shipping_system_platform_version'),
            webstore_platform_name=request.GET.get('webstore_platform_name'),
            webstore_platform_version=request.GET.get('webstore_platform_version')
        )
        return JsonResponse(response.to_dict(), safe=False)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=400)

urlpatterns = [
    path('address-validate/', address_validate_view, name='address-validate'),
    # path('address-validate/', address_api.AddressApi().exp_api_address_validate, name='address-validate'),
    path('identifier/', identifier_api.IdentifierApi().exp_api_identifiers, name='identifier'),
    path('invoice/', invoice_api.InvoiceApi().exp_api_shipments_invoice_data, name='invoice'),
    path('pickup/', pickup_api.PickupApi().exp_api_pickups, name='pickup'),
    path('product/', product_api.ProductApi().exp_api_products, name='product'),
    path('rating/', rating_api.RatingApi().exp_api_rates_with_http_info, name='rating'),
    path('reference_data/', reference_data_api.ReferenceDataApi().exp_api_reference_data, name='reference-data'),
    path('servicepoint/', servicepoint_api.ServicepointApi().exp_api_servicepoints, name='servicepoint'),
    path('shipment/', shipment_api.ShipmentApi().exp_api_shipments, name='shipment'),
    path('tracking/', tracking_api.TrackingApi().exp_api_shipments_tracking, name='tracking'),
    # Repeat for other views in a similar manner
]

print("Loaded openapi_client.urls with urlpatterns:", urlpatterns)
