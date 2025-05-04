from django import forms
from base_page.models import SiteVisitor


class SiteVisitorSignupForm(forms.ModelForm):
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={"class": "form-control", "placeholder": "Пароль"}),
        label="Пароль"
    )
    confirm_password = forms.CharField(
        widget=forms.PasswordInput(attrs={"class": "form-control", "placeholder": "Повторите пароль"}),
        label="Повторите пароль"
    )

    class Meta:
        model = SiteVisitor
        fields = ["first_name", "email"]
        widgets = {
            "first_name": forms.TextInput(attrs={"class": "form-control", "placeholder": "Ваше имя"}),
            "email": forms.EmailInput(attrs={"class": "form-control", "placeholder": "Адрес электронной почты"}),
        }
        labels = {
            "first_name": "Ваше имя",
            "email": "Адрес электронной почты",
        }
        error_messages = {
            "email": {
                "unique": "Пользователь с таким адресом электронной почты уже зарегистрирован.",
            },
        }

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password != confirm_password:
            raise forms.ValidationError("Пароли не совпадают.")

        return cleaned_data