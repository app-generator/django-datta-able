from django.urls import include, path
from rest_framework.routers import DefaultRouter

# from .views import ShipmentViewSet

router = DefaultRouter()
# router.register(r'shipments', ShipmentViewSet)

urlpatterns = [
    path('', include(router.urls)),
    # path('dhl-address-validation',views.DhlAddressValidationView.as_view()),

]
