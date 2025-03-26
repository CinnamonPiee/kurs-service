from django.urls import path

from discounts import views


app_name = 'discounts'


urlpatterns = [
    path('', views.discounts, name='discounts'),
]