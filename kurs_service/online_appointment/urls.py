from django.urls import path
from . import views


app_name = "online_appointment"


urlpatterns = [
    path('', views.online_appointment, name='online_appointment'),
	path('ajax/get-car-models/', views.get_car_models, name='get_car_models'),
    path('ajax/get-car-modifications/', views.get_car_modifications, name='get_car_modifications'),
]
