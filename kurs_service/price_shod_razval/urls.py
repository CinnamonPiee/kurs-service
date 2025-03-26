from django.urls import path

from price_shod_razval import views


app_name = 'price_shod_razval'


urlpatterns = [
    path('', views.price_shod_razval, name='price_shod_razval'),
]