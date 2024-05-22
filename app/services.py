import logging
from datetime import datetime
from zoneinfo import ZoneInfo

import requests
from python_dhl.resources.helper import MeasurementUnit
from python_dhl.resources.response import (
    DHLPickupResponse,
    DHLRatesResponse,
    DHLResponse,
    DHLShipmentResponse,
    DHLTrackingResponse,
    DHLUploadResponse,
    DHLValidateAddressResponse,
)
from requests.auth import HTTPBasicAuth

logger = logging.getLogger(__name__)


class DHLService:
    """
    Main class with static data and the main methods.
    """
    dhl_endpoint = 'https://express.api.dhl.com/mydhlapi'
    dhl_endpoint_test = 'https://express.api.dhl.com/mydhlapi/test'

    def __init__(self, api_key, api_secret, account_number, test_mode=False):
        self.api_key = api_key
        self.api_secret = api_secret
        self.account_number = account_number
        self.test_mode = test_mode
        self.endpoint_url = self.dhl_endpoint_test if test_mode else self.dhl_endpoint

    def validate_address(self, address, shipment_type):
        """
        Checks if an address is valid for a shipment
        :param address: DHLAddress
        :param shipment_type: ShipmentType
        :return: DHLValidateAddressResponse
        """
        try:
            params = {
                'type': shipment_type,
                'strictValidation': 'true',
                "postalCode": address.postal_code,
                "cityName": address.city,
                "countryCode": address.country_code,
            }
            dhl_response = requests.get(
                self.endpoint_url + '/address-validate', params,
                auth=HTTPBasicAuth(self.api_key, self.api_secret)
            )
            response = DHLValidateAddressResponse(
                success=True,
            )
            for attribute, value in dhl_response.json().items():
                if attribute == 'address':
                    response.address = value
                if attribute == 'warnings':
                    response.warnings = value
            return response
        except Exception as err:
            return DHLValidateAddressResponse(
                success=False,
                error_title='No address found.',
                error_detail=str(err)
            )

    def get_rates(self, sender, receiver, product, shipment_date, with_customs='false', unit_of_measurement=MeasurementUnit.METRIC.value):
        """
        Returns DHL's product capabilities and prices (where applicable)
        This is also used to get a detailed list of all available service codes for a prospect shipment
        :param sender: DHLPostalAddress
        :param receiver: DHLPostalAddress
        :param product: DHLProduct
        :param shipment_date: Datetime timezone aware
        :param with_customs: true/false as string
        :param unit_of_measurement: MeasurementUnit
        :return: DHLRatesResponse
        """
        try:
            if not (shipment_date.tzinfo is not None and shipment_date.tzinfo.utcoffset(
                    shipment_date) is not None):
                return DHLRatesResponse(
                    success=False,
                    error_title='Ship date is not timezone aware.'
                )
            dhl_ship_date = datetime.strftime(shipment_date, '%Y-%m-%d')
            params = {
                'accountNumber': self.account_number,
                'originCountryCode': sender.country_code,
                'originCityName': sender.city,
                'destinationCountryCode': receiver.country_code,
                'destinationCityName': receiver.city,
                'weight': product.weight,
                'length': product.length,
                'width': product.width,
                'height': product.height,
                'plannedShippingDate': dhl_ship_date,
                'isCustomsDeclarable': with_customs,
                'unitOfMeasurement': unit_of_measurement
            }
            dhl_response = requests.get(
                self.endpoint_url + '/rates', params=params,
                auth=HTTPBasicAuth(self.api_key, self.api_secret)
            )
            response = DHLRatesResponse(
                success=True,
                products=dhl_response.json()['products'],
            )
            return response
        except Exception as err:
            return DHLRatesResponse(
                success=False,
                error_title='No rates found.',
                error_detail=str(err)
            )

    def get_shipment_status(self, tracking_number):
        """
        Returns all statuses given a tracking number
        :param tracking_number: string
        """
        try:
            dhl_response = requests.get(
                self.endpoint_url + '/shipments' + str(tracking_number) + '/tracking',
                auth=HTTPBasicAuth(self.api_key, self.api_secret)
            )
            response = DHLTrackingResponse(
                success=True,
                shipments=dhl_response.json()['shipments'],
            )
            return response
        except Exception as err:
            return DHLTrackingResponse(
                success=False,
                error_title='No shipments found.',
                error_detail=str(err)
            )

    def check_shipment(self, tracking_number):
        """
        Returns all documents available given a tracking number
        :param tracking_number: string
        """
        try:
            dhl_response = requests.get(
                self.endpoint_url + '/shipments' + str(tracking_number) + '/proof-of-delivery',
                auth=HTTPBasicAuth(self.api_key, self.api_secret)
            )
            response = DHLUploadResponse(
                success=True,
                documents=dhl_response.json()['documents'],
            )
            return response
        except Exception as err:
            return DHLUploadResponse(
                success=False,
                error_title='No electronic proof of delivery found.',
                error_detail=str(err)
            )

    def ship(self, dhl_shipment):
        """
        Generates a shipping label and transmit shipment detail to DHL
        :param dhl_shipment: DHLShipment
        :return: DHLShipmentResponse
        """
        try:
            if not (dhl_shipment.ship_datetime.tzinfo is not None and dhl_shipment.ship_datetime.tzinfo.utcoffset(
                    dhl_shipment.ship_datetime) is not None):
                return DHLShipmentResponse(
                    success=False,
                    error_title='Ship date is not timezone aware.'
                )
            shipment = self._create_shipment(dhl_shipment)
            dhl_response = requests.post(
                self.endpoint_url + '/shipments', json=shipment,
                auth=HTTPBasicAuth(self.api_key, self.api_secret)
            )
            if 'detail' in dhl_response.json():
                error_title = None
                error_detail = None
                additional_error_details = []
                message = None
                status = None
                for attribute, value in dhl_response.json().items():
                    if attribute == 'title':
                        error_title = value
                    if attribute == 'detail':
                        error_detail = value
                    if attribute == 'additionalDetails':
                        for e in value:
                            additional_error_details.append(e)
                    if attribute == 'message':
                        message = value
                    if attribute == 'status':
                        status = value
                response = DHLShipmentResponse(
                    success=False,
                    error_title=error_title,
                    error_detail=error_detail,
                    additional_error_details=additional_error_details,
                    message=message,
                    status=status
                )
            else:
                response = DHLShipmentResponse(
                    success=True,
                    tracking_number=dhl_response.json()['shipmentTrackingNumber'],
                    documents_bytes=dhl_response.json()['documents'],
                )
            return response
        except Exception as err:
            return DHLShipmentResponse(
                success=False,
                error_title='Shipment error. No label.',
                error_detail=str(err)
            )

    def _create_shipment(self, dhl_shipment):
        dhl_ship_date = datetime.strftime(dhl_shipment.ship_datetime, '%Y-%m-%dT%H:%M:%S GMT%z')
        dhl_ship_date = "{0}:{1}".format(
            dhl_ship_date[:-2],
            dhl_ship_date[-2:]
        )

        json_data = {
            "plannedShippingDateAndTime": dhl_ship_date,
            "pickup": {
                "isRequested": dhl_shipment.request_pickup,
                "pickupDetails": {
                    "postalAddress": dhl_shipment.sender_address.to_dict(),
                    "contactInformation": dhl_shipment.sender_contact.to_dict(),
                    "typeCode": dhl_shipment.sender_contact.contact_type
                },
            },
            "productCode": dhl_shipment.product_code,
            "outputImageProperties": dhl_shipment.output_format.to_dict(),
            "customerDetails": {
                "shipperDetails": {
                    "postalAddress": dhl_shipment.sender_address.to_dict(),
                    "contactInformation": dhl_shipment.sender_contact.to_dict(),
                    "typeCode": dhl_shipment.sender_contact.contact_type
                },
                "receiverDetails": {
                    "postalAddress": dhl_shipment.receiver_address.to_dict(),
                    "contactInformation": dhl_shipment.receiver_contact.to_dict(),
                    "typeCode": dhl_shipment.receiver_contact.contact_type
                },
            },
            "content": dhl_shipment.content.to_dict()
        }

        accounts = []
        for a in dhl_shipment.accounts:
            accounts.append(a.to_dict())
        json_data['accounts'] = accounts

        if dhl_shipment.pickup_close_time:
            json_data['pickup']['closeTime'] = dhl_shipment.pickup_close_time
        if dhl_shipment.pickup_location:
            json_data['pickup']['location'] = dhl_shipment.pickup_location
        if dhl_shipment.sender_registration_numbers:
            registration_numbers = []
            for r in dhl_shipment.sender_registration_numbers:
                registration_numbers.append(r.to_dict())
            json_data['pickup']['pickupDetails']['registrationNumbers'] = registration_numbers
            json_data['customerDetails']['shipperDetails']['registrationNumbers'] = registration_numbers
        if dhl_shipment.added_services:
            added_services = []
            for a in dhl_shipment.added_services:
                added_services.append(a.to_dict())
            json_data['valueAddedServices'] = added_services
        if dhl_shipment.sender_address.street_line2:
            json_data['pickup']['pickupDetails']['postalAddress']['addressLine2'] = dhl_shipment.sender.street_line2
        if dhl_shipment.sender_address.street_line3:
            json_data['pickup']['pickupDetails']['postalAddress']['addressLine3'] = dhl_shipment.sender.street_line3
        if dhl_shipment.sender_address.county_name:
            json_data['pickup']['pickupDetails']['postalAddress']['countyName'] = dhl_shipment.sender.county_name
        if dhl_shipment.customer_references:
            references = []
            for cr in dhl_shipment.customer_references:
                references.append({'value': cr})
            json_data['customerReferences'] = references

        return json_data

    def pickup(self, dhl_pickup):
        """
        Creates a DHL Express pickup booking request
        :param dhl_pickup: DHLPickup
        :return: DHLShipmentResponse
        """
        try:
            if not (dhl_pickup.pickup_datetime.tzinfo is not None and dhl_pickup.pickup_datetime.tzinfo.utcoffset(
                    dhl_pickup.pickup_datetime) is not None):
                return DHLPickupResponse(
                    success=False,
                    error_title='Pickup date is not timezone aware.'
                )
            pickup = self._create_pickup(dhl_pickup)
            dhl_response = requests.post(
                self.endpoint_url + '/pickups', json=pickup,
                auth=HTTPBasicAuth(self.api_key, self.api_secret)
            )
            if 'detail' in dhl_response.json():
                error_title = None
                error_detail = None
                additional_error_details = []
                message = None
                status = None
                for attribute, value in dhl_response.json().items():
                    if attribute == 'title':
                        error_title = value
                    if attribute == 'detail':
                        error_detail = value
                    if attribute == 'additionalDetails':
                        for e in value:
                            additional_error_details.append(e)
                    if attribute == 'message':
                        message = value
                    if attribute == 'status':
                        status = value
                response = DHLShipmentResponse(
                    success=False,
                    error_title=error_title,
                    error_detail=error_detail,
                    additional_error_details=additional_error_details,
                    message=message,
                    status=status
                )
            else:
                response = DHLPickupResponse(
                    success=True,
                    dispatch_confirmation_numbers=dhl_response.json()['dispatchConfirmationNumbers'],
                )
                for attribute, value in dhl_response.json().items():
                    if attribute == 'readyByTime':
                        response.ready_by_time = value
                    if attribute == 'warnings':
                        response.warnings = value
            return response
        except Exception as err:
            return DHLPickupResponse(
                success=False,
                error_title='Pickup error. No label.',
                error_detail=str(err)
            )

    def _create_pickup(self, dhl_pickup):
        dhl_pickup_date = datetime.strftime(dhl_pickup.pickup_datetime, '%Y-%m-%dT%H:%M:%S GMT%z')
        dhl_pickup_date = "{0}:{1}".format(
            dhl_pickup_date[:-2],
            dhl_pickup_date[-2:]
        )

        json_data = {
            "plannedPickupDateAndTime": dhl_pickup_date,
            "customerDetails": {
                "shipperDetails": {
                    "postalAddress": dhl_pickup.sender_address.to_dict(),
                    "contactInformation": dhl_pickup.sender_contact.to_dict(),
                },
            },
            "shipmentDetails": [dhl_pickup.content.to_dict_pickup()]
        }

        accounts = []
        for a in dhl_pickup.accounts:
            accounts.append(a.to_dict())
        json_data['accounts'] = accounts

        return json_data

    def upload_document(self, dhl_document):
        """
        Uploads updated customs documentation for your DHL Express shipment that has not been picked up yet
        :param dhl_document: DHLDocument
        :return: DHLResponse
        """
        try:
            if not (dhl_document.original_planned_shipping_date.tzinfo is not None and dhl_document.original_planned_shipping_date.tzinfo.utcoffset(
                    dhl_document.original_planned_shipping_date) is not None):
                return DHLResponse(
                    success=False,
                    error_title='Ship date is not timezone aware.'
                )
            original_planned_shipping_date = datetime.strftime(dhl_document.original_planned_shipping_date, '%Y-%m-%d')
            document_data = {
                "shipmentTrackingNumber": dhl_document.tracking_number,
                "originalPlannedShippingDate": original_planned_shipping_date,
                "productCode": dhl_document.product_code,
            }

            accounts = []
            for a in dhl_document.accounts:
                accounts.append(a.to_dict())
            document_data['accounts'] = accounts

            if dhl_document.document_images:
                document_images = []
                for d in dhl_document.document_images:
                    document_images.append(d.to_dict())
                document_data['documentImages'] = document_images
            dhl_response = requests.patch(
                self.endpoint_url + '/shipments/' + dhl_document.tracking_number + '/upload-image',
                json=document_data,
                auth=HTTPBasicAuth(self.api_key, self.api_secret)
            )
            response = DHLResponse(
                success=True,
            )
            for attribute, value in dhl_response.json().items():
                if attribute == 'status':
                    response.status = value
            return response
        except Exception as err:
            return DHLResponse(
                success=False,
                error_title=str(err)
            )
