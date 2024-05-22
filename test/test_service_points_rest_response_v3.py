# coding: utf-8

"""
    DHL Express APIs (MyDHL API)

    Welcome to the official DHL Express APIs (MyDHL API) below are the published API Documentation to fulfill your shipping needs with DHL Express.       Please follow the process described [here](https://developer.dhl.com/api-reference/dhl-express-mydhl-api#get-started-section/user-guide--get-access) to request access to the DHL Express - MyDHL API services   In case you already have DHL Express - MyDHL API Service credentials please ensure to use the endpoints/environments listed  [here](https://developer.dhl.com/api-reference/dhl-express-mydhl-api#get-started-section/user-guide--environments) 

    The version of the OpenAPI document: 2.11.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.service_points_rest_response_v3 import ServicePointsRestResponseV3

class TestServicePointsRestResponseV3(unittest.TestCase):
    """ServicePointsRestResponseV3 unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ServicePointsRestResponseV3:
        """Test ServicePointsRestResponseV3
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ServicePointsRestResponseV3`
        """
        model = ServicePointsRestResponseV3()
        if include_optional:
            return ServicePointsRestResponseV3(
                status = openapi_client.models.rest_response_status.RestResponseStatus(
                    status_code = 56, 
                    status_message = '', 
                    ok = True, 
                    warning = True, 
                    error_status = True, ),
                search_address = 'Chennai',
                search_location = openapi_client.models.geo_location.GeoLocation(
                    latitude = 1.337, 
                    longitude = 1.337, 
                    suggestion = openapi_client.models.suggestion.Suggestion(
                        label = '', 
                        value = '', 
                        latitude = 1.337, 
                        longitude = 1.337, 
                        country_code = '', 
                        place_id = '', 
                        provider_id = '', ), ),
                map_culture = '',
                map_language = '',
                service_points = [
                    openapi_client.models.service_point.ServicePoint(
                        id = 56, 
                        facility_id = '', 
                        facility_type_code = '', 
                        service_area_code = '', 
                        service_point_name = '', 
                        service_point_name_formatted = '', 
                        local_name = '', 
                        service_point_type = 'CITY', 
                        address = openapi_client.models.address.Address(
                            address_line1 = '', 
                            address_line2 = '', 
                            address_line3 = '', 
                            street = '', 
                            house_number = '', 
                            additional_info = '', 
                            city = '', 
                            zip_code = '', 
                            state = '', 
                            country = '', 
                            dhl_country = '', 
                            country_division_code = '', 
                            country_division_code_type = '', 
                            html = '', ), 
                        geo_location = openapi_client.models.geo_location.GeoLocation(
                            latitude = 1.337, 
                            longitude = 1.337, 
                            suggestion = openapi_client.models.suggestion.Suggestion(
                                label = '', 
                                value = '', 
                                latitude = 1.337, 
                                longitude = 1.337, 
                                country_code = '', 
                                place_id = '', 
                                provider_id = '', ), ), 
                        distance = '', 
                        shipping_cut_off_time = '', 
                        opening_hours = openapi_client.models.opening_hours.OpeningHours(
                            opening_hours = [
                                openapi_client.models.opening_time.OpeningTime(
                                    day_of_week = 'MONDAY', 
                                    opening_time = '', 
                                    closing_time = '', )
                                ], 
                            holiday_dates = [
                                datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date()
                                ], 
                            holidays_dates = {
                                'key' : [
                                    datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date()
                                    ]
                                }, 
                            html = '', 
                            holiday_opening_hours_html = '', 
                            holidays = openapi_client.models.holidays.Holidays(
                                open = [
                                    openapi_client.models.open_dates_time.OpenDatesTime(
                                        date = '', 
                                        from = '', 
                                        to = '', )
                                    ], 
                                closed = [
                                    openapi_client.models.closed_dates.ClosedDates(
                                        from = '', 
                                        to = '', )
                                    ], ), ), 
                        service_point_capabilities = openapi_client.models.service_point_capabilities.ServicePointCapabilities(
                            parking_available = True, 
                            disabled_access = True, 
                            shipment_drop_off = True, 
                            shipment_collection = True, 
                            international_shipping = True, 
                            domestic_shipping = True, 
                            account_shippers = True, 
                            label_printing = True, 
                            insurance = True, 
                            import_charges = True, 
                            packaging = True, 
                            receiver_paid = True, 
                            visa_program = True, 
                            pay_with_cash = True, 
                            pay_with_credit_card = True, 
                            pay_with_cheque = True, 
                            pay_with_mobile = True, 
                            pay_with_pay_pal = True, 
                            parking_title = '', 
                            disabled_access_title = '', 
                            piece_weight_limit = 1.337, 
                            piece_weight_limit_unit = '', 
                            piece_dimensions_limit = openapi_client.models.dimensions.Dimensions(
                                l = 1.337, 
                                w = 1.337, 
                                h = 1.337, ), 
                            piece_dimensions_limit_unit = '', 
                            piece_count_limit = 1.337, 
                            account_prepaid_shippers = True, 
                            prepaid_shippers = True, 
                            pre_print_return_label = True, 
                            label_free = True, 
                            ppc_list = [
                                ''
                                ], 
                            html = '', 
                            capability_codes = '', ), 
                        contact_details = openapi_client.models.contact_details.ContactDetails(
                            phone_number = '', 
                            email = '', 
                            link_uri = '', 
                            service_point_id = '', 
                            html = '', ), 
                        shipping_cut_off_time_html = '', 
                        distance_value = '', 
                        distance_metric = 1.337, 
                        language = openapi_client.models.language.Language(
                            language_code = '', 
                            language_script_code = '', 
                            language_country_code = '', 
                            language_ok = True, ), 
                        shipment_limitations = openapi_client.models.shipment_limitations.ShipmentLimitations(
                            max_number_of_pieces = openapi_client.models.value_unit.ValueUnit(
                                value = 1.337, 
                                uom = '', ), 
                            max_shipment_weight = openapi_client.models.value_unit.ValueUnit(
                                value = 1.337, 
                                uom = '', ), 
                            html = '', ), 
                        shipment_limitations_by_piece = openapi_client.models.shipment_limitations_by_piece.ShipmentLimitationsByPiece(
                            piece_size_limit1 = , 
                            piece_size_limit2 = , 
                            piece_size_limit3 = , 
                            max_piece_weight = , 
                            html = '', ), 
                        charge_code = '', 
                        partner = openapi_client.models.partner.Partner(
                            partner_id = '', 
                            partner_name = '', 
                            partner_type_code = '', 
                            promotion = openapi_client.models.promotion.Promotion(
                                id = 56, 
                                country_code = '', 
                                partner_type_code = '', 
                                service_point_id = '', 
                                client_id = '', 
                                capability = '', 
                                start_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                                end_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                                day_of_week = '', 
                                text = '', 
                                button_text = '', 
                                language_code1 = '', 
                                text1 = '', 
                                button_text1 = '', 
                                language_code2 = '', 
                                text2 = '', 
                                button_text2 = '', 
                                language_code3 = '', 
                                text3 = '', 
                                button_text3 = '', 
                                hyperlink = '', 
                                created = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), ), ), 
                        promotion = openapi_client.models.promotion.Promotion(
                            id = 56, 
                            country_code = '', 
                            partner_type_code = '', 
                            service_point_id = '', 
                            client_id = '', 
                            capability = '', 
                            start_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                            end_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                            day_of_week = '', 
                            text = '', 
                            button_text = '', 
                            language_code1 = '', 
                            text1 = '', 
                            button_text1 = '', 
                            language_code2 = '', 
                            text2 = '', 
                            button_text2 = '', 
                            language_code3 = '', 
                            text3 = '', 
                            button_text3 = '', 
                            hyperlink = '', 
                            created = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), ), 
                        capacity_status = openapi_client.models.capacity_status.CapacityStatus(
                            sev = '', 
                            msg_clg = '', 
                            msg_c_igd = '', 
                            dsc = '', 
                            dtl_dsc = '', ), 
                        svp_status = '', 
                        work_week_start = 56, 
                        located_at = '', 
                        time_zone = openapi_client.models.date_time_zone.DateTimeZone(
                            id = '', 
                            fixed = True, ), )
                    ],
                messages = [
                    ''
                    ],
                translations = openapi_client.models.translations.Translations(
                    map = {'some-key': 'some-value'}, ),
                lite_mode = True,
                promotion = openapi_client.models.promotion.Promotion(
                    id = 56, 
                    country_code = '', 
                    partner_type_code = '', 
                    service_point_id = '', 
                    client_id = '', 
                    capability = '', 
                    start_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    end_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    day_of_week = '', 
                    text = '', 
                    button_text = '', 
                    language_code1 = '', 
                    text1 = '', 
                    button_text1 = '', 
                    language_code2 = '', 
                    text2 = '', 
                    button_text2 = '', 
                    language_code3 = '', 
                    text3 = '', 
                    button_text3 = '', 
                    hyperlink = '', 
                    created = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), )
            )
        else:
            return ServicePointsRestResponseV3(
        )
        """

    def testServicePointsRestResponseV3(self):
        """Test ServicePointsRestResponseV3"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
