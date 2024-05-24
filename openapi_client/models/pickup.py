# coding: utf-8

"""
    DHL Express APIs (MyDHL API)

    Welcome to the official DHL Express APIs (MyDHL API) below are the published API Documentation to fulfill your shipping needs with DHL Express.       Please follow the process described [here](https://developer.dhl.com/api-reference/dhl-express-mydhl-api#get-started-section/user-guide--get-access) to request access to the DHL Express - MyDHL API services   In case you already have DHL Express - MyDHL API Service credentials please ensure to use the endpoints/environments listed  [here](https://developer.dhl.com/api-reference/dhl-express-mydhl-api#get-started-section/user-guide--environments) 

    The version of the OpenAPI document: 2.11.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictBool, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from openapi_client.models.pickup_pickup_details import PickupPickupDetails
from openapi_client.models.pickup_pickup_requestor_details import PickupPickupRequestorDetails
from openapi_client.models.pickup_special_instructions_inner import PickupSpecialInstructionsInner
from typing import Optional, Set
from typing_extensions import Self

class Pickup(BaseModel):
    """
    Pickup
    """ # noqa: E501
    is_requested: StrictBool = Field(description="Please advise if a pickup is needed for this shipment", alias="isRequested")
    close_time: Optional[Annotated[str, Field(strict=True, max_length=5)]] = Field(default=None, description="The latest time the location premises is available to dispatch the DHL Express shipment. (HH:MM) ", alias="closeTime")
    location: Optional[Annotated[str, Field(strict=True, max_length=80)]] = Field(default=None, description="Provides information on where the package should be picked up by DHL courier.")
    special_instructions: Optional[Annotated[List[PickupSpecialInstructionsInner], Field(max_length=1)]] = Field(default=None, description="Details special pickup instructions you may wish to send to the DHL Courier.", alias="specialInstructions")
    pickup_details: Optional[PickupPickupDetails] = Field(default=None, alias="pickupDetails")
    pickup_requestor_details: Optional[PickupPickupRequestorDetails] = Field(default=None, alias="pickupRequestorDetails")
    __properties: ClassVar[List[str]] = ["isRequested", "closeTime", "location", "specialInstructions", "pickupDetails", "pickupRequestorDetails"]

    @field_validator('close_time')
    def close_time_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if value is None:
            return value

        if not re.match(r"([0-1][0-9]|2[0-3]):([0-5][0-9])", value):
            raise ValueError(r"must validate the regular expression /([0-1][0-9]|2[0-3]):([0-5][0-9])/")
        return value

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of Pickup from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of each item in special_instructions (list)
        _items = []
        if self.special_instructions:
            for _item in self.special_instructions:
                if _item:
                    _items.append(_item.to_dict())
            _dict['specialInstructions'] = _items
        # override the default output from pydantic by calling `to_dict()` of pickup_details
        if self.pickup_details:
            _dict['pickupDetails'] = self.pickup_details.to_dict()
        # override the default output from pydantic by calling `to_dict()` of pickup_requestor_details
        if self.pickup_requestor_details:
            _dict['pickupRequestorDetails'] = self.pickup_requestor_details.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of Pickup from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "isRequested": obj.get("isRequested") if obj.get("isRequested") is not None else False,
            "closeTime": obj.get("closeTime"),
            "location": obj.get("location"),
            "specialInstructions": [PickupSpecialInstructionsInner.from_dict(_item) for _item in obj["specialInstructions"]] if obj.get("specialInstructions") is not None else None,
            "pickupDetails": PickupPickupDetails.from_dict(obj["pickupDetails"]) if obj.get("pickupDetails") is not None else None,
            "pickupRequestorDetails": PickupPickupRequestorDetails.from_dict(obj["pickupRequestorDetails"]) if obj.get("pickupRequestorDetails") is not None else None
        })
        return _obj

