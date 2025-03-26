from django.urls import path

from check_list import views


app_name = 'check_list'


urlpatterns = [
    path('', views.check_list, name='check_list'),
]