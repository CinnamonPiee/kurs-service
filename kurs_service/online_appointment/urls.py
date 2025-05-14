from django.urls import path
from . import views


app_name = "online_appointment"


urlpatterns = [
    path('', views.online_appointment, name='online_appointment'),
]