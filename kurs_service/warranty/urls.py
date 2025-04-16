from django.urls import path
from warranty import views


app_name = "warranty"


urlpatterns = [
    path('', views.warranty, name='warranty'),
]