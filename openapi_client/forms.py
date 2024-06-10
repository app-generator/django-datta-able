from django import forms


class AddressValidateForm(forms.Form):
    type_ = forms.ChoiceField(required=True, choices=[('pickup', 'Pickup'), ('delivery', 'Delivery')])
    country_code = forms.CharField(required=True)
    postal_code = forms.CharField(required=False)
    city_name = forms.CharField(required=False)
    county_name = forms.CharField(required=False)
    strict_validation = forms.BooleanField(required=False)
    message_reference = forms.CharField(required=False)
    message_reference_date = forms.CharField(required=False)
    plugin_name = forms.CharField(required=False)
    plugin_version = forms.CharField(required=False)
    shipping_system_platform_name = forms.CharField(required=False)
    shipping_system_platform_version = forms.CharField(required=False)
    webstore_platform_name = forms.CharField(required=False)
    webstore_platform_version = forms.CharField(required=False)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Overriding form widgets to add "form-control" class (bootstrap class).
        # This way you can pass html attributes to the form fields.
        for field in self.fields:
            if field not in ['type_', 'strict_validation']:
                self.fields[field].widget.attrs.update({'class': 'form-control', 'autocomplete': 'off'})

        # This field is a "select"
        self.fields['type_'].widget.attrs.update({'class': 'form-select', 'autocomplete': 'off'})

        # This field is a "checkbox"
        self.fields['strict_validation'].widget.attrs.update({'class': 'form-check', 'autocomplete': 'off'})

    def clean_country_code(self):
        # An example of how to "clean" fields.
        # Let's assume the country_code must be one of the following list and if it's not
        # we return an error. You can customize this as you wish
        country_code = self.cleaned_data['country_code']


        # This is just for an example, you can just delete this method or modify it as per your needs.
        if country_code not in ['CZ', 'TR', 'AE', 'IR']:
            self.add_error('country_code', f'"{country_code}" is not a valid country code.')


        return country_code

    def clean_message_reference(self):
        message_reference = self.cleaned_data['message_reference']
        if len(message_reference) <= 28:
            return None
        else:
            return message_reference
