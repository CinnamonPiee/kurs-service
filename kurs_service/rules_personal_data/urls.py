from django.urls import path
from rules_personal_data import views


app_name = "rules_personal_data"


urlpatterns = [
    path('', views.rules_personal_data, name='rules_personal_data'),
]