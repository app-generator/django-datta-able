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

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from openapi_client.models.value_unit import ValueUnit
from typing import Optional, Set
from typing_extensions import Self

class ShipmentLimitationsByPiece(BaseModel):
    """
    Shipment Piece Limitations in this Service Point.
    """ # noqa: E501
    piece_size_limit1: Optional[ValueUnit] = Field(default=None, alias="pieceSizeLimit1")
    piece_size_limit2: Optional[ValueUnit] = Field(default=None, alias="pieceSizeLimit2")
    piece_size_limit3: Optional[ValueUnit] = Field(default=None, alias="pieceSizeLimit3")
    max_piece_weight: Optional[ValueUnit] = Field(default=None, alias="maxPieceWeight")
    html: Optional[StrictStr] = Field(default=None, description="Obsolete. This is planned to be removed in future releases.")
    __properties: ClassVar[List[str]] = ["pieceSizeLimit1", "pieceSizeLimit2", "pieceSizeLimit3", "maxPieceWeight", "html"]

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
        """Create an instance of ShipmentLimitationsByPiece from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of piece_size_limit1
        if self.piece_size_limit1:
            _dict['pieceSizeLimit1'] = self.piece_size_limit1.to_dict()
        # override the default output from pydantic by calling `to_dict()` of piece_size_limit2
        if self.piece_size_limit2:
            _dict['pieceSizeLimit2'] = self.piece_size_limit2.to_dict()
        # override the default output from pydantic by calling `to_dict()` of piece_size_limit3
        if self.piece_size_limit3:
            _dict['pieceSizeLimit3'] = self.piece_size_limit3.to_dict()
        # override the default output from pydantic by calling `to_dict()` of max_piece_weight
        if self.max_piece_weight:
            _dict['maxPieceWeight'] = self.max_piece_weight.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ShipmentLimitationsByPiece from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "pieceSizeLimit1": ValueUnit.from_dict(obj["pieceSizeLimit1"]) if obj.get("pieceSizeLimit1") is not None else None,
            "pieceSizeLimit2": ValueUnit.from_dict(obj["pieceSizeLimit2"]) if obj.get("pieceSizeLimit2") is not None else None,
            "pieceSizeLimit3": ValueUnit.from_dict(obj["pieceSizeLimit3"]) if obj.get("pieceSizeLimit3") is not None else None,
            "maxPieceWeight": ValueUnit.from_dict(obj["maxPieceWeight"]) if obj.get("maxPieceWeight") is not None else None,
            "html": obj.get("html")
        })
        return _obj

