from django.urls import path
from . import views


app_name = "evacuation"


urlpatterns = [
    path('', views.evacuation, name='evacuation'),
]