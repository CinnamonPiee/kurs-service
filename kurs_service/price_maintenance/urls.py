from django.urls import path

from price_maintenance import views


app_name = 'price_maintenance'


urlpatterns = [
    path('', views.price_maintenance, name='price_maintenance'),
]