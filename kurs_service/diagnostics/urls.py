from django.urls import path

from diagnostics import views


app_name = 'diagnostics'


urlpatterns = [
    path('', views.diagnostics, name='diagnostics'),
]