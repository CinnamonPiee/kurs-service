from django.urls import path

from insurance import views


app_name = 'insurance'


urlpatterns = [
    path('', views.insurance, name='insurance'),
]