from django.urls import path
from . import views

app_name = 'base_page'

urlpatterns = [
    path('order-service/add-modal', views.add_order_service_modal, name='add_order_service_modal'),
]