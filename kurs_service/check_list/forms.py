from django import forms
from .models import CheckListOrder
from base_page.models import (
	CarMark,
    CarModel,
    CarModification,
)


class CheckListOrderForm(forms.ModelForm):
    car_mark = forms.ModelChoiceField(
		queryset=CarMark.objects.all(),
		empty_label="Выберите марку",
		widget=forms.Select(attrs={'class': 'form-control', 'id': 'form-order-check-list-car_mark', 'aria-required': 'true'})
	)
    car_model = forms.ModelChoiceField(
        queryset=CarModification.objects.none(),
        required=False,
        widget=forms.Select(attrs={'class': 'form-control', 'id': 'form-order-check-list-car_model', 'disabled': 'disabled', 'style': 'background: #eee;'})
    )
    car_modification = forms.ModelChoiceField(
        queryset=CarModification.objects.none(),
        required=False,
        widget=forms.Select(attrs={'class': 'form-control', 'id': 'form-order-check-list-car_modification', 'disabled': 'disabled', 'style': 'background: #eee;'})
    )
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'car_mark' in self.data:
            try:
                mark_id = int(self.data.get('car_mark'))
                self.fields['car_model'].queryset = CarModel.objects.filter(mark_id=mark_id)
            except (ValueError, TypeError):
                pass
        if 'car_model' in self.data:
            try:
                model_id = int(self.data.get('car_model'))
                self.fields['car_modification'].queryset = CarModification.objects.filter(model_id=model_id)
            except (ValueError, TypeError):
                pass
    
    class Meta:
        model = CheckListOrder
        fields = [
            "name", "number", "email",
            "car_mark", "car_model", "car_modification",
            "created_at", "comment_user", "quantity"
        ]
        widgets = {
            "created_at": forms.DateTimeInput(attrs={"type": "datetime-local"}),
        }
