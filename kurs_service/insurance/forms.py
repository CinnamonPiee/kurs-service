from django import forms
from .models import InsuranceForm


class InsuranceFormModelForm(forms.ModelForm):
    class Meta:
        model = InsuranceForm
        fields = [
            "surname", "name", "patronymic", "birth_date", "driving_experience",
            "vin", "car_make", "car_model", "engine_power", "phone_number", "email", "date_time",
        ]
        widgets = {
            "surname": forms.TextInput(attrs={"class": "form-control",}),
            "name": forms.TextInput(attrs={"class": "form-control",}),
            "patronymic": forms.TextInput(attrs={"class": "form-control",}),
            "birth_date": forms.DateInput(attrs={"class": "form-control", "type": "date"}),
            "driving_experience": forms.NumberInput(attrs={"class": "form-control",}),
            "vin": forms.TextInput(attrs={"class": "form-control",}),
            "car_make": forms.TextInput(attrs={"class": "form-control",}),
            "car_model": forms.TextInput(attrs={"class": "form-control",}),
            "engine_power": forms.NumberInput(attrs={"class": "form-control",}),
            "phone_number": forms.TextInput(attrs={"class": "form-control",}),
            "email": forms.EmailInput(attrs={"class": "form-control",}),
            "date_time": forms.DateTimeInput(attrs={"class": "form-control", "type": "datetime-local"}),
        }
