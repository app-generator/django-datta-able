from django.urls import path
from . import views

urlpatterns = [
    path('address-validate-example/', views.address_validate_view_EXAMPLE, name='address-validate-example'),
    path('address-validate/', views.address_validate_view, name='address-validate'),
    path('identifier/', views.identifier_view, name='identifier'),
    path('invoice/', views.invoice_view, name='invoice'),
    # path('pickup/', views.pickup_view, name='pickup'),
    # path('product/', views.product_view, name='product'),
    # path('rating/', views.ratings_view, name='rating'),
    # path('reference_data/', views.reference_data_view, name='reference-data'),
    # path('servicepoint/', views.servicepoint_view, name='servicepoint'),
    # path('shipment/', views.shipment_view, name='shipment'),
    # path('tracking/', views.tracking_view, name='tracking'),
]
