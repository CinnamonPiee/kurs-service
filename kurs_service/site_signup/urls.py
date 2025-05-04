from django.urls import path
from . import views


app_name = "site_signup"


urlpatterns = [
    path('', views.site_signup, name='site_signup'),
]