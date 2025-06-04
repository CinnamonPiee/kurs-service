from django import forms
from .models import BasePageAddOrderServiceModalForm


class OnlineAppointmentFormModelForm(forms.ModelForm):
    class Meta:
        model = BasePageAddOrderServiceModalForm
        fields = [
            'name', 'call_number', 'email', 'date_time_order'
        ]
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'aria-required': 'true'}),
            'call_number': forms.TextInput(attrs={'class': 'form-control', 'aria-required': 'true'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'aria-required': 'true'}),
            'date_time_order': forms.DateTimeInput(attrs={'class': 'form-control', 'type': 'datetime-local', 'aria-required': 'true'}),
        }