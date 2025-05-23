from django.urls import path
from . import views


app_name = "price_maintenance"


urlpatterns = [
    path('', views.price_maintenance, name='price_maintenance'),
	path('<slug:category_slug>/', views.price_maintenance, name='price_maintenance_category'),
]