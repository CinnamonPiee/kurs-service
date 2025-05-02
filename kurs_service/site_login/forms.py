from django import forms
from base_page.models import SiteVisitor


class SiteVisitorLoginForm(forms.Form):
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={"class": "form-control", "placeholder": "Адрес электронной почты"}),
        label="Адрес электронной почты"
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={"class": "form-control", "placeholder": "Пароль"}),
        label="Пароль"
    )

    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data.get("email")
        password = cleaned_data.get("password")

        try:
            visitor = SiteVisitor.objects.get(email=email)
        except SiteVisitor.DoesNotExist:
            raise forms.ValidationError("Неверный логин или пароль.")

        if not visitor.check_password(password):
            raise forms.ValidationError("Неверный логин или пароль.")

        cleaned_data["visitor"] = visitor
        return cleaned_data
    