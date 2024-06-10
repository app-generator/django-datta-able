from __future__ import annotations
from django.db import models
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from typing import Optional, Set
from typing_extensions import Self

class Shipment(models.Model):
    bill_to_account = models.CharField(max_length=12)
    contents = models.CharField(max_length=100)
    destination_airport_code = models.CharField(max_length=3)
    facility_id = models.CharField(max_length=10)
    licence_plate_no = models.CharField(max_length=20)
    outbound_mail_sort_code = models.CharField(max_length=10)
    plt = models.BooleanField()
    product_abbreviation = models.CharField(max_length=10, null=True, blank=True)
    receiver_address1 = models.CharField(max_length=100, null=True, blank=True)
    receiver_address2 = models.CharField(max_length=100, null=True, blank=True)
    receiver_address3 = models.CharField(max_length=100, null=True, blank=True)
    receiver_attention = models.CharField(max_length=50, null=True, blank=True)
    receiver_city = models.CharField(max_length=50, null=True, blank=True)
    receiver_company_name = models.CharField(max_length=100, null=True, blank=True)
    receiver_country = models.CharField(max_length=50, null=True, blank=True)
    receiver_country_code = models.CharField(max_length=2, null=True, blank=True)
    receiver_postcode = models.CharField(max_length=12, null=True, blank=True)
    receiver_telephone = models.CharField(max_length=20, null=True, blank=True)
    shipment_date = models.DateTimeField(null=True, blank=True)
    shipment_declared_value = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    shipment_id = models.CharField(max_length=20, null=True, blank=True)
    shipment_pieces = models.IntegerField(null=True, blank=True)
    shipment_reference = models.CharField(max_length=20, null=True, blank=True)
    shipment_weight = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    shipper_account_number = models.CharField(max_length=12, null=True, blank=True)
    shipper_address1 = models.CharField(max_length=100, null=True, blank=True)
    shipper_address2 = models.CharField(max_length=100, null=True, blank=True)
    shipper_address3 = models.CharField(max_length=100, null=True, blank=True)
    shipper_airport_code = models.CharField(max_length=3,null=True, blank=True)
    shipper_city = models.CharField(max_length=50, null=True, blank=True)
    shipper_company_name = models.CharField(max_length=100, null=True, blank=True)
    shipper_country = models.CharField(max_length=50, null=True, blank=True)
    shipper_name = models.CharField(max_length=50, null=True, blank=True)
    shipper_phone = models.CharField(max_length=20, null=True, blank=True)
    shipper_postcode = models.CharField(max_length=12, null=True, blank=True)
    weight_rounded = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)

    def __str__(self):
        return self.shipment_id




