from django import forms
from .models import ReviewsReview


class ReviewForm(forms.ModelForm):
    class Meta:
        model = ReviewsReview
        fields = ["content", "image"]
        widgets = {
            "content": forms.Textarea(attrs={"class": "form-control", "placeholder": "Введите ваш отзыв"}),
            "image": forms.FileInput(attrs={"class": "form-control"}),
        }
        labels = {
            "content": "Введите ваш отзыв",
            "image": "Загрузите фото (необязательно)",
        }