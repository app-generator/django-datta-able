from datetime import timedelta, datetime
from enum import Enum


class MeasurementUnit(Enum):
    METRIC = 'metric'
    IMPERIAL = 'imperial'


class ShipmentType(Enum):
    DELIVERY = 'delivery'
    PICKUP = 'pickup'


class AccountType(Enum):
    """
    shipper: your account code, who is requesting the shipment
    payer: an account code different from yours if the shipment is paid by someone different (for example the recipient)
    duties-taxes: an account code if the customs duties are paid by someone different from the recipient
    """
    SHIPPER = 'shipper'
    PAYER = 'payer'
    DUTIES_TAXES = 'duties-taxes'


class ShipperType(Enum):
    BUSINESS = 'business'
    DIRECT_CONSUMER = 'direct_consumer'
    GOVERNMENT = 'government'
    OTHER = 'other'
    PRIVATE = 'private'
    RESELLER = 'reseller'


class TypeCode(Enum):
    VAT = 'Value-Added tax'
    EIN = 'Employer Identification Number'
    GST = 'Goods and Service Tax'
    SSN = 'Social Security Number'
    EOR = 'European Union Registration and Identification'
    DUN = 'Data Universal Numbering System'
    FED = 'Federal Tax ID'
    STA = 'State Tax ID'
    CNP = 'Brazil CNPJ/CPF Federal Tax'
    IE = 'Brazil type IE/RG Federal Tax'
    INN = 'Russia bank details section - INN'
    KPP = 'Russia bank details section - KPP'
    OGR = 'Russia bank details section - OGRN'
    OKP = 'Russia bank details section - OKPO'
    SDT = 'Overseas Registered Supplier or AUSid GST Registration or VAT on E-Commerce'
    FTZ = 'Free Trade Zone ID'
    DAN = 'Deferment Account Duties Only'
    TAN = 'Deferment Account Tax Only'
    DTF = 'Deferment Account Duties, Taxes and Fees Only'
    RGP = 'EU Registered Exporters registration ID'
    DLI = 'Driver\'s License'
    NID = 'National Identity Card'
    PAS = 'Passport'
    MID = 'Manufacturer ID'


class DocumentType(Enum):
    INV = 'Invoice'
    PNV = 'Proforma'
    COO = 'Certificate of Origin'
    NAF = 'Nafta Certificate of Origin'
    CIN = 'Commercial Invoice'
    DCL = 'Custom Declaration'
    AWB = 'Air Waybill and Waybill Document'


class ProductCode(Enum):
    """
    Domestic shipment: DOM - N
    European shipment: ESU - W
    Switzerland and the UK: ESI - H
    USA, Canada, Japan and non-EEC countries: WPX - P
    """
    DOMESTIC = 'N'
    EUROPE = 'W'
    EXTRA_EU = 'H'
    OTHER = 'P'


class IncotermCode(Enum):
    EXW = 'ExWorks'
    FCA = 'Free Carrier'
    CPT = 'Carriage Paid To'
    CIP = 'Carriage and Insurance Paid To'
    DPU = 'Delivered at Place Unloaded'
    DAP = 'Delivered at Place'
    DDP = 'Delivered Duty Paid'
    FAS = 'Free Alongside Ship'
    FOB = 'Free on Board'
    CFR = 'Cost and Freight'
    CIF = 'Cost, Insurance and Freight'


def next_business_day():
    date_today = datetime.today()
    shift = 1 + ((date_today.weekday() // 4) * (6 - date_today.weekday()))
    return date_today + timedelta(shift)