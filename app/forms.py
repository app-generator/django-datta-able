from django import forms
from .models import Shipment

class ShipmentForm(forms.ModelForm):
    class Meta:
        model = Shipment
        fields = [
            'message_reference', 'message_reference_date', 'plugin_name',
            'plugin_version', 'shipping_system_platform_name',
            'shipping_system_platform_version', 'webstore_platform_name',
            'webstore_platform_version', 'strict_validation', 'bypass_plt_error',
            'validate_data_only'
        ]
        widgets = {
            'message_reference_date': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }
