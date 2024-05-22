from enum import Enum


class DHLAddress:
    """
    Saves all the address data.
    """

    def __init__(self, street_line1, city, postal_code, country_code, province_code=None,
                 county_name=None, street_line2=None, street_line3=None):
        self.street_line1 = street_line1
        self.city = city
        self.postal_code = postal_code
        self.province_code = province_code
        self.country_code = country_code
        self.county_name = county_name
        self.street_line2 = street_line2
        self.street_line3 = street_line3


class DHLContactInformation:
    """
    A class for creating the shipper and the recipient in the DHLShipment.
    """

    def __init__(self, full_name, phone, contact_type, company_name=None, mobile_phone=None, email=None):
        self.company_name = company_name
        self.full_name = full_name
        self.phone = phone
        self.contact_type = contact_type
        self.mobile_phone = mobile_phone
        self.email = email

    def to_dict(self):
        dict = {
            'companyName': self.company_name if self.company_name else self.full_name,
            'fullName': self.full_name,
            'phone': self.phone,
        }
        if self.mobile_phone:
            dict['mobilePhone'] = self.mobile_phone
        if self.email:
            dict['email'] = self.email
        return dict


class DHLPostalAddress(DHLAddress):
    """
    A class for creating a company instead of a person for use in DHLShipment.
    # DHL requires the company name, so we use person name
    """

    def __init__(self, street_line1, city_name, postal_code, country_code, province_code=None,
                 county_name=None, street_line2=None, street_line3=None):
        DHLAddress.__init__(self, street_line1, city_name, postal_code, country_code, province_code, county_name, street_line2, street_line3)

    def to_dict(self):
        dict = {
            'addressLine1': self.street_line1,
            'cityName': self.city,
            'postalCode': self.postal_code,
            'countryCode': self.country_code,
        }
        if self.province_code:
            dict['provinceCode'] = self.province_code
        if self.county_name:
            dict['countyName'] = self.county_name
        if self.street_line2:
            dict['addressLine2'] = self.street_line2
        if self.street_line3:
            dict['addressLine3'] = self.street_line3
        return dict


class DHLRegistrationNumber:
    def __init__(self, type_code, number, issuer_country_code):
        self.type_code = type_code
        self.number = number
        self.issuer_country_code = issuer_country_code

    def to_dict(self):
        return {
            "typeCode": self.type_code,
            "number": self.number,
            "issuerCountryCode": self.issuer_country_code
        }