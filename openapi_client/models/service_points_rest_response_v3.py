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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from openapi_client.models.geo_location import GeoLocation
from openapi_client.models.promotion import Promotion
from openapi_client.models.rest_response_status import RestResponseStatus
from openapi_client.models.service_point import ServicePoint
from openapi_client.models.translations import Translations
from typing import Optional, Set
from typing_extensions import Self

class ServicePointsRestResponseV3(BaseModel):
    """
    ServicePointsRestResponseV3
    """ # noqa: E501
    status: Optional[RestResponseStatus] = None
    search_address: Optional[StrictStr] = Field(default=None, description="The address used for the search (value of request parameter 'address')", alias="searchAddress")
    search_location: Optional[GeoLocation] = Field(default=None, alias="searchLocation")
    map_culture: Optional[StrictStr] = Field(default=None, description="The culture parameter for Bing Maps API (derived from the country parameter in the request)", alias="mapCulture")
    map_language: Optional[StrictStr] = Field(default=None, description="Map Culture Used for Third party Maps", alias="mapLanguage")
    service_points: Optional[List[ServicePoint]] = Field(default=None, description="Array of the found Service Points. Each Service Point entity contains details about the service point.", alias="servicePoints")
    messages: Optional[List[StrictStr]] = Field(default=None, description="Array of strings. Contains information messages  - e.g. required language is not available, result was filtered due to incoming holidays.")
    translations: Optional[Translations] = None
    lite_mode: Optional[StrictBool] = Field(default=None, description="Indicates whether lite mode is acitvated or not.", alias="liteMode")
    promotion: Optional[Promotion] = None
    __properties: ClassVar[List[str]] = ["status", "searchAddress", "searchLocation", "mapCulture", "mapLanguage", "servicePoints", "messages", "translations", "liteMode", "promotion"]

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
        """Create an instance of ServicePointsRestResponseV3 from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of status
        if self.status:
            _dict['status'] = self.status.to_dict()
        # override the default output from pydantic by calling `to_dict()` of search_location
        if self.search_location:
            _dict['searchLocation'] = self.search_location.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in service_points (list)
        _items = []
        if self.service_points:
            for _item in self.service_points:
                if _item:
                    _items.append(_item.to_dict())
            _dict['servicePoints'] = _items
        # override the default output from pydantic by calling `to_dict()` of translations
        if self.translations:
            _dict['translations'] = self.translations.to_dict()
        # override the default output from pydantic by calling `to_dict()` of promotion
        if self.promotion:
            _dict['promotion'] = self.promotion.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ServicePointsRestResponseV3 from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "status": RestResponseStatus.from_dict(obj["status"]) if obj.get("status") is not None else None,
            "searchAddress": obj.get("searchAddress"),
            "searchLocation": GeoLocation.from_dict(obj["searchLocation"]) if obj.get("searchLocation") is not None else None,
            "mapCulture": obj.get("mapCulture"),
            "mapLanguage": obj.get("mapLanguage"),
            "servicePoints": [ServicePoint.from_dict(_item) for _item in obj["servicePoints"]] if obj.get("servicePoints") is not None else None,
            "messages": obj.get("messages"),
            "translations": Translations.from_dict(obj["translations"]) if obj.get("translations") is not None else None,
            "liteMode": obj.get("liteMode"),
            "promotion": Promotion.from_dict(obj["promotion"]) if obj.get("promotion") is not None else None
        })
        return _obj

