from django.urls import re_path, path
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse

from api import (
    address_api, identifier_api, invoice_api, pickup_api,
    product_api, rating_api, reference_data_api, servicepoint_api,
    shipment_api, tracking_api
)
from api.views import *

urlpatterns = [
    path('address-validate/', address_api.AddressApi().exp_api_address_validate, name='address-validate'),
    path('identifier/', identifier_api.IdentifierApi().exp_api_identifiers, name='identifier'),
    path('invoice/', invoice_api.InvoiceApi().exp_api_shipments_invoice_data, name='invoice'),
    path('pickup/', pickup_api.PickupApi().exp_api_pickups, name='pickup'),
    path('product/', product_api.ProductApi().exp_api_products, name='product'),
    path('rating/', rating_api.RatingApi().exp_api_rates_with_http_info, name='rating'),
    path('reference_data/', reference_data_api.ReferenceDataApi().exp_api_reference_data, name='reference-data'),
    path('servicepoint/', servicepoint_api.ServicepointApi().exp_api_servicepoints, name='servicepoint'),
    path('shipment/', shipment_api.ShipmentApi().exp_api_shipments, name='shipment'),
    path('tracking/', tracking_api.TrackingApi().exp_api_shipments_tracking, name='tracking'),
	re_path("product/((?P<pk>\d+)/)?", csrf_exempt(ProductView.as_view())),
]

# print("Loaded openapi_client.urls with urlpatterns:", urlpatterns)
