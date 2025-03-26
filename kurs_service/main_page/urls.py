from django.urls import path

from main_page import views


app_name = 'main_page'


urlpatterns = [
    path('', views.main_page, name='main_page'),
]