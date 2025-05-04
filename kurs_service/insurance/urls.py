from django.urls import path
from . import views


app_name = "insurance"


urlpatterns = [
    path('', views.insurance, name='insurance'),
    path('add-insurance', views.add_insurance, name='add_insurance'),
]