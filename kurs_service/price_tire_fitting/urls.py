from django.urls import path

from price_tire_fitting import views


app_name = 'price_tire_fitting'


urlpatterns = [
    path('', views.price_tire_fitting, name='price_tire_fitting'),
]