from django import forms
from .models import OnlineAppointmentForm
from base_page.models import (
	CarService,
	CarMark,
)

class OnlineAppointmentFormModelForm(forms.ModelForm):
    title_services = forms.ModelChoiceField(
        queryset=CarService.objects.all(),
        empty_label="Выберите услугу",
        widget=forms.Select(attrs={'class': 'form-control', 'aria-required': 'true'})
    )
    car_mark = forms.ModelChoiceField(
		queryset=CarMark.objects.all(),
		empty_label="Выберите марку",
		widget=forms.Select(attrs={'class': 'form-control', 'id': 'form-order-check-list-car_mark', 'aria-required': 'true'})
	)
    car_model = forms.ChoiceField(
        choices=[],
        required=False,
        widget=forms.Select(attrs={'class': 'form-control', 'id': 'form-order-check-list-car_model', 'disabled': 'disabled', 'style': 'background: #eee;'})
    )
    car_modification = forms.ChoiceField(
        choices=[],
        required=False,
        widget=forms.Select(attrs={'class': 'form-control', 'id': 'form-order-check-list-car_modification', 'disabled': 'disabled', 'style': 'background: #eee;'})
    )
    
    class Meta:
        model = OnlineAppointmentForm
        fields = [
            'name_user', 'call_number', 'email', 'title_services',
            'car_mark', 'car_model', 'car_modification', 'car_body',
            'date_time_order', 'comment_user'
        ]
        widgets = {
            'name_user': forms.TextInput(attrs={'class': 'form-control', 'aria-required': 'true'}),
            'call_number': forms.TextInput(attrs={'class': 'form-control', 'aria-required': 'true'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'aria-required': 'true'}),
            'car_body': forms.TextInput(attrs={'class': 'form-control'}),
            'date_time_order': forms.DateTimeInput(attrs={'class': 'form-control', 'type': 'datetime-local', 'aria-required': 'true'}),
            'comment_user': forms.Textarea(attrs={'class': 'form-control', 'rows': 2, 'style': 'resize: none;'}),
        }