class DHLResponse:
    def __init__(self, success, error_title=None, error_detail=None, additional_error_details=None, status=None):
        self.success = success
        self.error_title = error_title
        self.error_detail = error_detail
        self.additional_error_details = additional_error_details
        self.status = status

    def __str__(self):
        return '%s' % ('Success' if self.success else 'Fail: '+str(self.error_title))


class DHLShipmentResponse(DHLResponse):
    def __init__(self, success, tracking_number=None, identification_number=None, dispatch_number=None,
                 documents_bytes=None, error_title=None, error_detail=None, additional_error_details=None,
                 message=None, status=None):
        DHLResponse.__init__(self, success, error_title, error_detail, additional_error_details)

        self.tracking_number = tracking_number
        self.identification_number = identification_number
        self.dispatch_number = dispatch_number
        self.documents_bytes = documents_bytes
        self.message = message
        self.status = status


class DHLPickupResponse(DHLResponse):
    def __init__(self, success, dispatch_confirmation_numbers=None, ready_by_time=None,
                 next_pickup_date=None, error_title=None, error_detail=None, additional_error_details=None,
                 warnings=None, status=None):
        DHLResponse.__init__(self, success, error_title, error_detail, additional_error_details)

        self.dispatch_confirmation_numbers = dispatch_confirmation_numbers
        self.ready_by_time = ready_by_time
        self.next_pickup_date = next_pickup_date
        self.warnings = warnings
        self.status = status


class DHLUploadResponse(DHLResponse):
    def __init__(self, success, error_title=None, error_detail=None, additional_error_details=None, documents=None):
        DHLResponse.__init__(self, success, error_title, error_detail, additional_error_details)

        self.documents = documents


class DHLTrackingResponse(DHLResponse):
    def __init__(self, success, error_title=None, error_detail=None, additional_error_details=None, shipments=None):
        DHLResponse.__init__(self, success, error_title, error_detail, additional_error_details)

        self.shipments = shipments


class DHLRatesResponse(DHLResponse):
    def __init__(self, success, error_title=None, error_detail=None, additional_error_details=None, products=None):
        DHLResponse.__init__(self, success, error_title, error_detail, additional_error_details)

        self.products = products


class DHLValidateAddressResponse(DHLResponse):
    def __init__(self, success, error_title=None, error_detail=None, additional_error_details=None, warnings=None, address=None):
        DHLResponse.__init__(self, success, error_title, error_detail, additional_error_details)

        self.warnings = warnings
        self.address = address