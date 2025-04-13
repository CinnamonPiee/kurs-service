from django.urls import path
from photo_gallery import views


app_name = "photo_gallery"


urlpatterns = [
    path('', views.photo_gallery, name='photo_gallery'),
]
