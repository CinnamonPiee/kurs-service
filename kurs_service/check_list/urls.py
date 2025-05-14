from django.urls import path
from . import views


app_name = "check_list"


urlpatterns = [
    path('', views.check_list, name='check_list'),
]