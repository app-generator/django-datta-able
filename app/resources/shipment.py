class DHLProduct:
    def __init__(self, weight, length, width, height):
        self.weight = weight
        self.length = length
        self.width = width
        self.height = height

    def to_dict(self):
        return {
            "weight": self.weight,
            "dimensions": {
                "length": self.length,
                "width": self.width,
                "height": self.height
            },
        }


class DHLDangerousGood:
    def __init__(self, content_id, dry_ice_total_net_weight, un_code):
        self.content_id = content_id
        self.dry_ice_total_net_weight = dry_ice_total_net_weight
        self.un_code = un_code


class DHLAccountType:
    def __init__(self, type_code, number):
        self.type_code = type_code
        self.number = number

    def to_dict(self):
        dict = {
            'typeCode': self.type_code.value,
            'number': self.number,
        }
        return dict


class DHLAddedService:
    """
    This section adds shipping services, such as Insurance (or Shipment Value Protection).
    For detailed list of all available service codes "added_services" for your prospect shipment use service.get_rates.
    For instance:
    "PT" if you do not know when they will be entrusted to DHL, they must be managed with the datastaging service.
    "WY" (Paper Less Trade) in case of non-EEC countries because the declaration of free export and the invoice must also be loaded.
    "PK" (Deferred Image Acquisition o Deferred Paperless) as WY but if documents are uploaded after the shipment.
    "DD" (DTP service) commonly referred to as Duties and Taxes Paid (DTP) indicates that the shipper or account holder incurs the full costs of the shipment, including any duties or taxes that might be incurred from customs.
    "DU" (IOR service) the official importer of the shipment, meaning that duties, taxes, or any other payments will go through the IOR, but the end destination of the shipment will go to the receiver, who doesn’t have to pay for a thing.
    """
    def __init__(self, service_code, value=None, currency=None, method=None, dangerous_goods=None):
        self.service_code = service_code
        self.value = value
        self.currency = currency
        self.method = method
        self.dangerous_goods = dangerous_goods

    def to_dict(self):
        dict = {
            'serviceCode': self.service_code,
        }
        if self.value:
            dict['value'] = self.value
        if self.currency:
            dict['currency'] = self.currency
        if self.currency:
            dict['method'] = self.method
        if self.currency:
            dict['dangerousGoods'] = self.dangerous_goods
        return dict


class DHLShipmentContent:
    def __init__(self, packages, is_custom_declarable, description, incoterm_code, unit_of_measurement,
                 declared_value=None, declared_value_currency=None, product_code=None):
        self.packages = packages
        self.is_custom_declarable = is_custom_declarable
        self.description = description
        self.incoterm_code = incoterm_code
        self.unit_of_measurement = unit_of_measurement
        self.declared_value = declared_value
        self.declared_value_currency = declared_value_currency
        self.product_code = product_code

    def to_dict(self):
        packages = []
        for p in self.packages:
            packages.append(p.to_dict())
        dict = {
            'packages': packages,
            'isCustomsDeclarable': self.is_custom_declarable,
            'description': self.description,
            'incoterm': self.incoterm_code,
            'unitOfMeasurement': self.unit_of_measurement,
        }
        if self.declared_value:
            dict['declaredValue'] = self.declared_value
        if self.declared_value_currency:
            dict['declaredValueCurrency'] = self.declared_value_currency
        return dict

    def to_dict_pickup(self):
        packages = []
        for p in self.packages:
            packages.append(p.to_dict())
        dict = {
            'productCode': self.product_code,
            'packages': packages,
            'isCustomsDeclarable': self.is_custom_declarable,
            'unitOfMeasurement': self.unit_of_measurement,
        }
        if self.declared_value:
            dict['declaredValue'] = self.declared_value
        if self.declared_value_currency:
            dict['declaredValueCurrency'] = self.declared_value_currency
        return dict


class DHLShipmentOutput:
    def __init__(self, dpi, logo_file_format, logo_file_base64, encoding_format='pdf',
                 split_transport_and_waybill_doc_labels=True,
                 all_documents_in_one_image=True, split_documents_by_pages=True, split_invoice_and_receipt=True):
        self.dpi = dpi
        self.logo_file_format = logo_file_format
        self.logo_file_base64 = logo_file_base64
        self.encoding_format = encoding_format
        self.split_transport_and_waybill_doc_labels = split_transport_and_waybill_doc_labels
        self.all_documents_in_one_image = all_documents_in_one_image
        self.split_documents_by_pages = split_documents_by_pages
        self.split_invoice_and_receipt = split_invoice_and_receipt

    def to_dict(self):
        return {
            'printerDPI': self.dpi,
            'customerLogos': [{
                'fileFormat': self.logo_file_format.upper(),
                'content': self.logo_file_base64
            }],
            'encodingFormat': self.encoding_format.lower(),
            'splitTransportAndWaybillDocLabels': self.split_transport_and_waybill_doc_labels,
            'allDocumentsInOneImage': self.all_documents_in_one_image,
            'splitDocumentsByPages': self.split_documents_by_pages,
            'splitInvoiceAndReceipt': self.split_invoice_and_receipt,
        }


class DHLShipment:
    """
    A class for creating a shipment.

    For detailed list of all available service codes "added_services" for your prospect shipment use service.get_rates.
    For instance:
    "PT" if you do not know when they will be entrusted to DHL, they must be managed with the datastaging service.
    "WY" (Paper Less Trade) in case of non-EEC countries because the declaration of free export and the invoice must also be loaded.
    "PK" (Deferred Image Acquisition o Deferred Paperless) as WY but if documents are uploaded after the shipment.
    "DD" (DTP service) commonly referred to as Duties and Taxes Paid (DTP) indicates that the shipper or account holder incurs the full costs of the shipment, including any duties or taxes that might be incurred from customs.
    "DU" (IOR service) the official importer of the shipment, meaning that duties, taxes, or any other payments will go through the IOR, but the end destination of the shipment will go to the receiver, who doesn’t have to pay for a thing.

    The "request_pickup" parameter must be set to false every time it is not necessary to notify the courier to pass,
    so when you already have a notice for the same address, when you have a fixed agreement for which it passes every day
    at a specific time or if the package is brought to a DHL service point / office.
    If false it is not necessary to call the pickup service.
    """
    def __init__(self, sender_contact, sender_address, receiver_contact, receiver_address, ship_datetime,
                 product_code, added_services, content, output_format, accounts,
                 customer_references=None, sender_registration_numbers=None,
                 request_pickup=False, pickup_close_time=None, pickup_location=None):
        self.sender_contact = sender_contact
        self.sender_address = sender_address
        self.sender_registration_numbers = sender_registration_numbers
        self.receiver_contact = receiver_contact
        self.receiver_address = receiver_address
        self.ship_datetime = ship_datetime
        self.product_code = product_code
        self.added_services = added_services
        self.content = content
        self.request_pickup = request_pickup
        self.pickup_close_time = pickup_close_time
        self.pickup_location = pickup_location
        self.accounts = accounts
        self.output_format = output_format
        self.customer_references = customer_references


class DHLPickup:
    def __init__(self, sender_contact, sender_address, receiver_contact, receiver_address, pickup_datetime,
                 content, accounts, sender_registration_numbers=None):
        self.sender_contact = sender_contact
        self.sender_address = sender_address
        self.sender_registration_numbers = sender_registration_numbers
        self.receiver_contact = receiver_contact
        self.receiver_address = receiver_address
        self.pickup_datetime = pickup_datetime
        self.content = content
        self.accounts = accounts


class DHLDocumentImage:
    def __init__(self, type_code, image_format, content):
        self.type_code = type_code
        self.image_format = image_format
        self.content = content

    def to_dict(self):
        return {
            'typeCode': self.type_code,
            'imageFormat': self.image_format.upper(),
            'content': self.content
        }


class DHLDocument:
    def __init__(self, tracking_number, original_planned_shipping_date, product_code, document_images, accounts):
        self.tracking_number = tracking_number
        self.original_planned_shipping_date = original_planned_shipping_date
        self.product_code = product_code
        self.document_images = document_images
        self.accounts = accounts
