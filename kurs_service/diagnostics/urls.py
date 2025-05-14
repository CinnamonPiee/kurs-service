from django.urls import path
from . import views


app_name = "diagnostics"


urlpatterns = [
    path('', views.diagnostics, name='diagnostics'),
]