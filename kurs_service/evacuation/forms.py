from django import forms
from .models import EvacuationForm

class EvacuationFormModelForm(forms.ModelForm):
    class Meta:
        model = EvacuationForm
        fields = ['name_user', 'call_number', 'email', 'data_time_order', 'car_body', 'comment_user']
        widgets = {
            'name_user': forms.TextInput(attrs={
                'class': 'form-control',
                'id': 'order-evacuation-form-name_user',
                'aria-required': 'true',
            }),
            'call_number': forms.TextInput(attrs={
                'class': 'form-control',
                'id': 'order-evacuation-form-call_number',
                'aria-required': 'true',
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'id': 'order-evacuation-form-email',
                'aria-required': 'true',
            }),
            'data_time_order': forms.DateTimeInput(attrs={
                'class': 'form-control',
                'id': 'datetimepicker-51',
                'aria-required': 'true',
                'type': 'datetime-local',
            }),
            'car_body': forms.TextInput(attrs={
                'class': 'form-control',
                'id': 'order-evacuation-form-car_body',
            }),
            'comment_user': forms.Textarea(attrs={
                'class': 'form-control',
                'id': 'order-evacuation-form-comment_user',
                'rows': 2,
                'style': 'resize: none;',
            }),
        }