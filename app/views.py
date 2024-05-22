import os
from datetime import datetime, timedelta
from zoneinfo import ZoneInfo

from python_dhl.resources import address, shipment
from python_dhl.service import DHLService
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import Shipment
from .serializers import ShipmentSerializer

# Use os.getenv to get the value of an environment variable
api_key = os.getenv('DHL_API_KEY')
api_secret = os.getenv('DHL_API_SECRET')
account = os.getenv('DHL_ACCOUNT')

print(api_key, api_secret, 'test')
print(309049009)

# Initialize DHL API client
dhl_service = DHLService(
    api_key='DHL_API_KEY',
    api_secret='DHL_API_SECRET',
    account_number='309049009',
    test_mode=True
)

class ShipmentViewSet(viewsets.ModelViewSet):
    queryset = Shipment.objects.all()
    serializer_class = ShipmentSerializer

    @action(detail=False, methods=['post'])
    def create_shipment(self, request):
        data = request.data
        print(data)
        # Create sender and receiver contact and address details
        sender_contact = address.DHLContactInformation(
            company_name='Test Co.',
            full_name='Name and surname',
            phone='+39000000000',
            email='your_email@example.com',
            contact_type='business'
        )
        sender_address = address.DHLPostalAddress(
            street_line1='Via Maestro Zampieri, 14',
            postal_code='36016',
            province_code='VI',
            country_code='IT',
            city_name='Thiene'
        )
        registration_numbers = [address.DHLRegistrationNumber(
            type_code='VAT',
            number='42342423423',
            issuer_country_code='IT'
        )]
        receiver_contact = address.DHLContactInformation(
            full_name='Customer',
            phone='+39000000000',
            email='customer@example.com',
            contact_type='private'
        )
        receiver_address = address.DHLPostalAddress(
            street_line1='Rue Poncelet, 17',
            postal_code='75017',
            country_code='FR',
            city_name='Paris'
        )

        # Create shipment packages
        packages = [shipment.DHLProduct(
            weight=1,
            length=35,
            width=28,
            height=8
        )]

        # Set shipment content and label output
        shipment_date = datetime.now() + timedelta(days=1)
        shipment_date = shipment_date.replace(hour=14, minute=0, second=0, microsecond=0, tzinfo=ZoneInfo('Europe/Rome'))
        added_service = [shipment.DHLAddedService(
            service_code='W'
        )]
        content = shipment.DHLShipmentContent(
            packages=packages,
            is_custom_declarable=False,
            description='Shipment test',
            incoterm_code='DAP',
            unit_of_measurement='metric',
            product_code='EUROPE'
        )
        output = shipment.DHLShipmentOutput(
            dpi=300,
            encoding_format='pdf',
            logo_file_format='png',
            logo_file_base64='LOGO_BASE64'
        )
        customer_references = ['id1', 'id2']

        # Create shipment object
        dhl_shipment = shipment.DHLShipment(
            accounts=[shipment.DHLAccountType(type_code='shipper', number='your_account_number')],
            sender_contact=sender_contact,
            sender_address=sender_address,
            sender_registration_numbers=registration_numbers,
            receiver_contact=receiver_contact,
            receiver_address=receiver_address,
            ship_datetime=shipment_date,
            added_services=added_service,
            product_code='EUROPE',
            content=content,
            output_format=output,
            customer_references=customer_references
        )

        # Make the shipment
        try:
            ship_response = dhl_service.ship(dhl_shipment)
            return Response(ship_response)
        except Exception as e:
            return Response({'error': str(e)}, status=400)

    @action(detail=False, methods=['get'])
    def get_rates(self, request):
        origin = request.query_params.get('origin')
        destination = request.query_params.get('destination')
        weight = request.query_params.get('weight')
        try:
            rates = dhl_service.get_rates(origin=origin, destination=destination, weight=weight)
            return Response(rates)
        except Exception as e:
            return Response({'error': str(e)}, status=400)

    @action(detail=False, methods=['get'])
    def track_shipment(self, request):
        tracking_number = request.query_params.get('tracking_number')
        try:
            tracking_info = dhl_service.get_shipment_status(tracking_number)
            return Response(tracking_info)
        except Exception as e:
            return Response({'error': str(e)}, status=400)

