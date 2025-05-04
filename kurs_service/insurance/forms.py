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
            "surname": forms.TextInput(attrs={"class": "form-control", "placeholder": "Фамилия"}),
            "name": forms.TextInput(attrs={"class": "form-control", "placeholder": "Имя"}),
            "patronymic": forms.TextInput(attrs={"class": "form-control", "placeholder": "Отчество"}),
            "birth_date": forms.DateInput(attrs={"class": "form-control", "type": "date"}),
            "driving_experience": forms.NumberInput(attrs={"class": "form-control", "placeholder": "Стаж вождения (лет)"}),
            "vin": forms.TextInput(attrs={"class": "form-control", "placeholder": "VIN"}),
            "car_make": forms.TextInput(attrs={"class": "form-control", "placeholder": "Марка автомобиля"}),
            "car_model": forms.TextInput(attrs={"class": "form-control", "placeholder": "Модель автомобиля"}),
            "engine_power": forms.NumberInput(attrs={"class": "form-control", "placeholder": "Мощность двигателя (л.с.)"}),
            "phone_number": forms.TextInput(attrs={"class": "form-control", "placeholder": "Номер телефона"}),
            "email": forms.EmailInput(attrs={"class": "form-control", "placeholder": "Электронная почта"}),
            "date_time": forms.DateTimeInput(attrs={"class": "form-control", "type": "datetime-local"}),
        }

        labels = {
            "surname": "Фамилия",
            "name": "Имя",
            "patronymic": "Отчество",
            "birth_date": "Дата рождения",
            "driving_experience": "Стаж вождения (лет)",
            "vin": "VIN",
            "car_make": "Марка автомобиля",
            "car_model": "Модель автомобиля",
            "engine_power": "Мощность двигателя (л.с.)",
            "phone_number": "Номер телефона",
            "email": "Электронная почта",
            "date_time": "Дата и время",
        }