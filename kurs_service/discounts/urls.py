from django.urls import path
from . import views


app_name = "discounts"


urlpatterns = [
    path('', views.discounts, name='discounts'),
]