# coding: utf-8

"""
    DHL Express APIs (MyDHL API)

    Welcome to the official DHL Express APIs (MyDHL API) below are the published API Documentation to fulfill your shipping needs with DHL Express.       Please follow the process described [here](https://developer.dhl.com/api-reference/dhl-express-mydhl-api#get-started-section/user-guide--get-access) to request access to the DHL Express - MyDHL API services   In case you already have DHL Express - MyDHL API Service credentials please ensure to use the endpoints/environments listed  [here](https://developer.dhl.com/api-reference/dhl-express-mydhl-api#get-started-section/user-guide--environments) 

    The version of the OpenAPI document: 2.11.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501

import warnings
from pydantic import validate_call, Field, StrictFloat, StrictStr, StrictInt
from typing import Any, Dict, List, Optional, Tuple, Union
from typing_extensions import Annotated

from pydantic import Field, StrictBool, StrictStr, field_validator
from typing import Optional
from typing_extensions import Annotated
from openapi_client.models.supermodel_io_logistics_express_address_validate_response import SupermodelIoLogisticsExpressAddressValidateResponse

from openapi_client.api_client import ApiClient, RequestSerialized
from openapi_client.api_response import ApiResponse
from openapi_client.rest import RESTResponseType


class AddressApi:
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None) -> None:
        if api_client is None:
            api_client = ApiClient.get_default()
        self.api_client = api_client


    @validate_call
    def exp_api_address_validate(
        self,
        type: StrictStr,
        country_code: Annotated[str, Field(min_length=2, strict=True, max_length=2, description="A short text string code (see values defined in ISO 3166) specifying the shipment origin country. https://gs1.org/voc/Country, Alpha-2 Code")],
        postal_code: Annotated[Optional[Annotated[str, Field(min_length=0, strict=True, max_length=12)]], Field(description="Text specifying the postal code for an address. https://gs1.org/voc/postalCode")] = None,
        city_name: Annotated[Optional[Annotated[str, Field(min_length=0, strict=True, max_length=45)]], Field(description="Text specifying the city name")] = None,
        county_name: Annotated[Optional[Annotated[str, Field(min_length=0, strict=True, max_length=45)]], Field(description="Text specifying the county name")] = None,
        strict_validation: Annotated[Optional[StrictBool], Field(description="If set to true service will return no records when exact valid match not found")] = None,
        message_reference: Annotated[Optional[Annotated[str, Field(min_length=28, strict=True, max_length=36)]], Field(description="Please provide message reference ")] = None,
        message_reference_date: Annotated[Optional[StrictStr], Field(description="Optional reference date in the  HTTP-date format https://tools.ietf.org/html/rfc7231#section-7.1.1.2")] = None,
        plugin_name: Annotated[Optional[Annotated[str, Field(strict=True, max_length=20)]], Field(description="Please provide name of the plugin (applicable to 3PV only) ")] = None,
        plugin_version: Annotated[Optional[Annotated[str, Field(strict=True, max_length=15)]], Field(description="Please provide version of the plugin (applicable to 3PV only) ")] = None,
        shipping_system_platform_name: Annotated[Optional[Annotated[str, Field(strict=True, max_length=20)]], Field(description="Please provide name of the shipping platform(applicable to 3PV only) ")] = None,
        shipping_system_platform_version: Annotated[Optional[Annotated[str, Field(strict=True, max_length=15)]], Field(description="Please provide version of the shipping platform (applicable to 3PV only) ")] = None,
        webstore_platform_name: Annotated[Optional[Annotated[str, Field(strict=True, max_length=20)]], Field(description="Please provide name of the webstore platform (applicable to 3PV only) ")] = None,
        webstore_platform_version: Annotated[Optional[Annotated[str, Field(strict=True, max_length=15)]], Field(description="Please provide version of the webstore platform (applicable to 3PV only) ")] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> SupermodelIoLogisticsExpressAddressValidateResponse:
        """Validate DHL Express pickup/delivery capabilities at origin/destination

        Validates if DHL Express has got pickup/delivery capabilities at origin/destination 

        :param type: (required)
        :type type: str
        :param country_code: A short text string code (see values defined in ISO 3166) specifying the shipment origin country. https://gs1.org/voc/Country, Alpha-2 Code (required)
        :type country_code: str
        :param postal_code: Text specifying the postal code for an address. https://gs1.org/voc/postalCode
        :type postal_code: str
        :param city_name: Text specifying the city name
        :type city_name: str
        :param county_name: Text specifying the county name
        :type county_name: str
        :param strict_validation: If set to true service will return no records when exact valid match not found
        :type strict_validation: bool
        :param message_reference: Please provide message reference 
        :type message_reference: str
        :param message_reference_date: Optional reference date in the  HTTP-date format https://tools.ietf.org/html/rfc7231#section-7.1.1.2
        :type message_reference_date: str
        :param plugin_name: Please provide name of the plugin (applicable to 3PV only) 
        :type plugin_name: str
        :param plugin_version: Please provide version of the plugin (applicable to 3PV only) 
        :type plugin_version: str
        :param shipping_system_platform_name: Please provide name of the shipping platform(applicable to 3PV only) 
        :type shipping_system_platform_name: str
        :param shipping_system_platform_version: Please provide version of the shipping platform (applicable to 3PV only) 
        :type shipping_system_platform_version: str
        :param webstore_platform_name: Please provide name of the webstore platform (applicable to 3PV only) 
        :type webstore_platform_name: str
        :param webstore_platform_version: Please provide version of the webstore platform (applicable to 3PV only) 
        :type webstore_platform_version: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._exp_api_address_validate_serialize(
            type=type,
            country_code=country_code,
            postal_code=postal_code,
            city_name=city_name,
            county_name=county_name,
            strict_validation=strict_validation,
            message_reference=message_reference,
            message_reference_date=message_reference_date,
            plugin_name=plugin_name,
            plugin_version=plugin_version,
            shipping_system_platform_name=shipping_system_platform_name,
            shipping_system_platform_version=shipping_system_platform_version,
            webstore_platform_name=webstore_platform_name,
            webstore_platform_version=webstore_platform_version,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "SupermodelIoLogisticsExpressAddressValidateResponse",
            '400': "SupermodelIoLogisticsExpressErrorResponse",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        ).data


    @validate_call
    def exp_api_address_validate_with_http_info(
        self,
        type: StrictStr,
        country_code: Annotated[str, Field(min_length=2, strict=True, max_length=2, description="A short text string code (see values defined in ISO 3166) specifying the shipment origin country. https://gs1.org/voc/Country, Alpha-2 Code")],
        postal_code: Annotated[Optional[Annotated[str, Field(min_length=0, strict=True, max_length=12)]], Field(description="Text specifying the postal code for an address. https://gs1.org/voc/postalCode")] = None,
        city_name: Annotated[Optional[Annotated[str, Field(min_length=0, strict=True, max_length=45)]], Field(description="Text specifying the city name")] = None,
        county_name: Annotated[Optional[Annotated[str, Field(min_length=0, strict=True, max_length=45)]], Field(description="Text specifying the county name")] = None,
        strict_validation: Annotated[Optional[StrictBool], Field(description="If set to true service will return no records when exact valid match not found")] = None,
        message_reference: Annotated[Optional[Annotated[str, Field(min_length=28, strict=True, max_length=36)]], Field(description="Please provide message reference ")] = None,
        message_reference_date: Annotated[Optional[StrictStr], Field(description="Optional reference date in the  HTTP-date format https://tools.ietf.org/html/rfc7231#section-7.1.1.2")] = None,
        plugin_name: Annotated[Optional[Annotated[str, Field(strict=True, max_length=20)]], Field(description="Please provide name of the plugin (applicable to 3PV only) ")] = None,
        plugin_version: Annotated[Optional[Annotated[str, Field(strict=True, max_length=15)]], Field(description="Please provide version of the plugin (applicable to 3PV only) ")] = None,
        shipping_system_platform_name: Annotated[Optional[Annotated[str, Field(strict=True, max_length=20)]], Field(description="Please provide name of the shipping platform(applicable to 3PV only) ")] = None,
        shipping_system_platform_version: Annotated[Optional[Annotated[str, Field(strict=True, max_length=15)]], Field(description="Please provide version of the shipping platform (applicable to 3PV only) ")] = None,
        webstore_platform_name: Annotated[Optional[Annotated[str, Field(strict=True, max_length=20)]], Field(description="Please provide name of the webstore platform (applicable to 3PV only) ")] = None,
        webstore_platform_version: Annotated[Optional[Annotated[str, Field(strict=True, max_length=15)]], Field(description="Please provide version of the webstore platform (applicable to 3PV only) ")] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> ApiResponse[SupermodelIoLogisticsExpressAddressValidateResponse]:
        """Validate DHL Express pickup/delivery capabilities at origin/destination

        Validates if DHL Express has got pickup/delivery capabilities at origin/destination 

        :param type: (required)
        :type type: str
        :param country_code: A short text string code (see values defined in ISO 3166) specifying the shipment origin country. https://gs1.org/voc/Country, Alpha-2 Code (required)
        :type country_code: str
        :param postal_code: Text specifying the postal code for an address. https://gs1.org/voc/postalCode
        :type postal_code: str
        :param city_name: Text specifying the city name
        :type city_name: str
        :param county_name: Text specifying the county name
        :type county_name: str
        :param strict_validation: If set to true service will return no records when exact valid match not found
        :type strict_validation: bool
        :param message_reference: Please provide message reference 
        :type message_reference: str
        :param message_reference_date: Optional reference date in the  HTTP-date format https://tools.ietf.org/html/rfc7231#section-7.1.1.2
        :type message_reference_date: str
        :param plugin_name: Please provide name of the plugin (applicable to 3PV only) 
        :type plugin_name: str
        :param plugin_version: Please provide version of the plugin (applicable to 3PV only) 
        :type plugin_version: str
        :param shipping_system_platform_name: Please provide name of the shipping platform(applicable to 3PV only) 
        :type shipping_system_platform_name: str
        :param shipping_system_platform_version: Please provide version of the shipping platform (applicable to 3PV only) 
        :type shipping_system_platform_version: str
        :param webstore_platform_name: Please provide name of the webstore platform (applicable to 3PV only) 
        :type webstore_platform_name: str
        :param webstore_platform_version: Please provide version of the webstore platform (applicable to 3PV only) 
        :type webstore_platform_version: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._exp_api_address_validate_serialize(
            type=type,
            country_code=country_code,
            postal_code=postal_code,
            city_name=city_name,
            county_name=county_name,
            strict_validation=strict_validation,
            message_reference=message_reference,
            message_reference_date=message_reference_date,
            plugin_name=plugin_name,
            plugin_version=plugin_version,
            shipping_system_platform_name=shipping_system_platform_name,
            shipping_system_platform_version=shipping_system_platform_version,
            webstore_platform_name=webstore_platform_name,
            webstore_platform_version=webstore_platform_version,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "SupermodelIoLogisticsExpressAddressValidateResponse",
            '400': "SupermodelIoLogisticsExpressErrorResponse",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        )


    @validate_call
    def exp_api_address_validate_without_preload_content(
        self,
        type: StrictStr,
        country_code: Annotated[str, Field(min_length=2, strict=True, max_length=2, description="A short text string code (see values defined in ISO 3166) specifying the shipment origin country. https://gs1.org/voc/Country, Alpha-2 Code")],
        postal_code: Annotated[Optional[Annotated[str, Field(min_length=0, strict=True, max_length=12)]], Field(description="Text specifying the postal code for an address. https://gs1.org/voc/postalCode")] = None,
        city_name: Annotated[Optional[Annotated[str, Field(min_length=0, strict=True, max_length=45)]], Field(description="Text specifying the city name")] = None,
        county_name: Annotated[Optional[Annotated[str, Field(min_length=0, strict=True, max_length=45)]], Field(description="Text specifying the county name")] = None,
        strict_validation: Annotated[Optional[StrictBool], Field(description="If set to true service will return no records when exact valid match not found")] = None,
        message_reference: Annotated[Optional[Annotated[str, Field(min_length=28, strict=True, max_length=36)]], Field(description="Please provide message reference ")] = None,
        message_reference_date: Annotated[Optional[StrictStr], Field(description="Optional reference date in the  HTTP-date format https://tools.ietf.org/html/rfc7231#section-7.1.1.2")] = None,
        plugin_name: Annotated[Optional[Annotated[str, Field(strict=True, max_length=20)]], Field(description="Please provide name of the plugin (applicable to 3PV only) ")] = None,
        plugin_version: Annotated[Optional[Annotated[str, Field(strict=True, max_length=15)]], Field(description="Please provide version of the plugin (applicable to 3PV only) ")] = None,
        shipping_system_platform_name: Annotated[Optional[Annotated[str, Field(strict=True, max_length=20)]], Field(description="Please provide name of the shipping platform(applicable to 3PV only) ")] = None,
        shipping_system_platform_version: Annotated[Optional[Annotated[str, Field(strict=True, max_length=15)]], Field(description="Please provide version of the shipping platform (applicable to 3PV only) ")] = None,
        webstore_platform_name: Annotated[Optional[Annotated[str, Field(strict=True, max_length=20)]], Field(description="Please provide name of the webstore platform (applicable to 3PV only) ")] = None,
        webstore_platform_version: Annotated[Optional[Annotated[str, Field(strict=True, max_length=15)]], Field(description="Please provide version of the webstore platform (applicable to 3PV only) ")] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> RESTResponseType:
        """Validate DHL Express pickup/delivery capabilities at origin/destination

        Validates if DHL Express has got pickup/delivery capabilities at origin/destination 

        :param type: (required)
        :type type: str
        :param country_code: A short text string code (see values defined in ISO 3166) specifying the shipment origin country. https://gs1.org/voc/Country, Alpha-2 Code (required)
        :type country_code: str
        :param postal_code: Text specifying the postal code for an address. https://gs1.org/voc/postalCode
        :type postal_code: str
        :param city_name: Text specifying the city name
        :type city_name: str
        :param county_name: Text specifying the county name
        :type county_name: str
        :param strict_validation: If set to true service will return no records when exact valid match not found
        :type strict_validation: bool
        :param message_reference: Please provide message reference 
        :type message_reference: str
        :param message_reference_date: Optional reference date in the  HTTP-date format https://tools.ietf.org/html/rfc7231#section-7.1.1.2
        :type message_reference_date: str
        :param plugin_name: Please provide name of the plugin (applicable to 3PV only) 
        :type plugin_name: str
        :param plugin_version: Please provide version of the plugin (applicable to 3PV only) 
        :type plugin_version: str
        :param shipping_system_platform_name: Please provide name of the shipping platform(applicable to 3PV only) 
        :type shipping_system_platform_name: str
        :param shipping_system_platform_version: Please provide version of the shipping platform (applicable to 3PV only) 
        :type shipping_system_platform_version: str
        :param webstore_platform_name: Please provide name of the webstore platform (applicable to 3PV only) 
        :type webstore_platform_name: str
        :param webstore_platform_version: Please provide version of the webstore platform (applicable to 3PV only) 
        :type webstore_platform_version: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._exp_api_address_validate_serialize(
            type=type,
            country_code=country_code,
            postal_code=postal_code,
            city_name=city_name,
            county_name=county_name,
            strict_validation=strict_validation,
            message_reference=message_reference,
            message_reference_date=message_reference_date,
            plugin_name=plugin_name,
            plugin_version=plugin_version,
            shipping_system_platform_name=shipping_system_platform_name,
            shipping_system_platform_version=shipping_system_platform_version,
            webstore_platform_name=webstore_platform_name,
            webstore_platform_version=webstore_platform_version,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "SupermodelIoLogisticsExpressAddressValidateResponse",
            '400': "SupermodelIoLogisticsExpressErrorResponse",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        return response_data.response


    def _exp_api_address_validate_serialize(
        self,
        type,
        country_code,
        postal_code,
        city_name,
        county_name,
        strict_validation,
        message_reference,
        message_reference_date,
        plugin_name,
        plugin_version,
        shipping_system_platform_name,
        shipping_system_platform_version,
        webstore_platform_name,
        webstore_platform_version,
        _request_auth,
        _content_type,
        _headers,
        _host_index,
    ) -> RequestSerialized:

        _host = None

        _collection_formats: Dict[str, str] = {
        }

        _path_params: Dict[str, str] = {}
        _query_params: List[Tuple[str, str]] = []
        _header_params: Dict[str, Optional[str]] = _headers or {}
        _form_params: List[Tuple[str, str]] = []
        _files: Dict[str, Union[str, bytes]] = {}
        _body_params: Optional[bytes] = None

        # process the path parameters
        # process the query parameters
        if type is not None:
            
            _query_params.append(('type', type))
            
        if country_code is not None:
            
            _query_params.append(('countryCode', country_code))
            
        if postal_code is not None:
            
            _query_params.append(('postalCode', postal_code))
            
        if city_name is not None:
            
            _query_params.append(('cityName', city_name))
            
        if county_name is not None:
            
            _query_params.append(('countyName', county_name))
            
        if strict_validation is not None:
            
            _query_params.append(('strictValidation', strict_validation))
            
        # process the header parameters
        if message_reference is not None:
            _header_params['Message-Reference'] = message_reference
        if message_reference_date is not None:
            _header_params['Message-Reference-Date'] = message_reference_date
        if plugin_name is not None:
            _header_params['Plugin-Name'] = plugin_name
        if plugin_version is not None:
            _header_params['Plugin-Version'] = plugin_version
        if shipping_system_platform_name is not None:
            _header_params['Shipping-System-Platform-Name'] = shipping_system_platform_name
        if shipping_system_platform_version is not None:
            _header_params['Shipping-System-Platform-Version'] = shipping_system_platform_version
        if webstore_platform_name is not None:
            _header_params['Webstore-Platform-Name'] = webstore_platform_name
        if webstore_platform_version is not None:
            _header_params['Webstore-Platform-Version'] = webstore_platform_version
        # process the form parameters
        # process the body parameter


        # set the HTTP header `Accept`
        _header_params['Accept'] = self.api_client.select_header_accept(
            [
                'application/json'
            ]
        )


        # authentication setting
        _auth_settings: List[str] = [
            'basicAuth'
        ]

        return self.api_client.param_serialize(
            method='GET',
            resource_path='/address-validate',
            path_params=_path_params,
            query_params=_query_params,
            header_params=_header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            auth_settings=_auth_settings,
            collection_formats=_collection_formats,
            _host=_host,
            _request_auth=_request_auth
        )


