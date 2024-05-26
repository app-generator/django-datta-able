from http import HTTPStatus
from django.http import Http404
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from django.http import JsonResponse


from api.serializers import *
from api import (
    address_api, identifier_api, invoice_api, pickup_api,
    product_api, rating_api, reference_data_api, servicepoint_api,
    shipment_api, tracking_api
)

# try:

#     from home.models import Product

# except:
#     pass

class ProductView(APIView):

    permission_classes = (IsAuthenticatedOrReadOnly,)

    def post(self, request):
        serializer = ProductSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(data={
                **serializer.errors,
                'success': False
            }, status=HTTPStatus.BAD_REQUEST)
        serializer.save()
        return Response(data={
            'message': 'Record Created.',
            'success': True
        }, status=HTTPStatus.OK)

    def get(self, request, pk=None):
        if not pk:
            return Response({
                'data': [ProductSerializer(instance=obj).data for obj in Product.objects.all()],
                'success': True
            }, status=HTTPStatus.OK)
        try:
            obj = get_object_or_404(Product, pk=pk)
        except Http404:
            return Response(data={
                'message': 'object with given id not found.',
                'success': False
            }, status=HTTPStatus.NOT_FOUND)
        return Response({
            'data': ProductSerializer(instance=obj).data,
            'success': True
        }, status=HTTPStatus.OK)

    def put(self, request, pk):
        try:
            obj = get_object_or_404(Product, pk=pk)
        except Http404:
            return Response(data={
                'message': 'object with given id not found.',
                'success': False
            }, status=HTTPStatus.NOT_FOUND)
        serializer = ProductSerializer(instance=obj, data=request.data, partial=True)
        if not serializer.is_valid():
            return Response(data={
                **serializer.errors,
                'success': False
            }, status=HTTPStatus.BAD_REQUEST)
        serializer.save()
        return Response(data={
            'message': 'Record Updated.',
            'success': True
        }, status=HTTPStatus.OK)

    def delete(self, request, pk):
        try:
            obj = get_object_or_404(Product, pk=pk)
        except Http404:
            return Response(data={
                'message': 'object with given id not found.',
                'success': False
            }, status=HTTPStatus.NOT_FOUND)
        obj.delete()
        return Response(data={
            'message': 'Record Deleted.',
            'success': True
        }, status=HTTPStatus.OK)


@api_view(['GET'])
def address_validate_view(request):
    api_instance = address_api.AddressApi()
    try:
        response = api_instance.exp_api_address_validate(
            type=request.GET.get('type'),  # Corrected: 'type' is the parameter name
            country_code=request.GET.get('country_code'),  # Corrected: 'country_code' is the parameter name
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