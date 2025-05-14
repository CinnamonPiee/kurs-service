from django.urls import path
from . import views


app_name = "price_tire_fitting"


urlpatterns = [
    path('', views.price_tire_fitting, name='price_tire_fitting'),
]