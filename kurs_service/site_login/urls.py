from django.urls import path
from site_login import views


app_name = "site_login"


urlpatterns = [
    path('', views.site_login, name='site_login'),
]