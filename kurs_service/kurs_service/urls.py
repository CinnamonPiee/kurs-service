"""
URL configuration for kurs_service project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from about.views import about
from check_list.views import check_list
from contacts.views import contacts
from diagnostics.views import diagnostics
from discounts.views import discounts
from evacuation.views import evacuation
from insurance.views import insurance
from main_page.views import main_page
from news.views import news
from online_appointment.views import online_appointment
from photo_gallery.views import photo_gallery
from price_maintenance.views import price_maintenance
from price_shod_razval.views import price_shod_razval
from price_tire_fitting.views import price_tire_fitting
from reviews.views import reviews
from site_login.views import site_login
from site_signup.views import site_signup
from warranty.views import warranty


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', main_page, name='main_page'),
    path('about/', about, name='about'),
    path('check-list/', check_list, name='check_list'),
    path('contacts/', contacts, name='contacts'),
    path('diagnostics/', diagnostics, name='diagnostics'),
    path('discounts/', discounts, name='discounts'),
    path('evacuation/', evacuation, name='evacuation'),
    path('insurance/', insurance, name='insurance'),
    path('news/', news, name='news'),
    path('online-appointment/', online_appointment, name='online_appointment'),
    path('photo-gallery', photo_gallery, name='photo_gallery'),
    path('price-maintenance/', price_maintenance, name='price_maintenance'),
    path('price-shod-razval/', price_shod_razval, name='price_shod_razval'),
    path('price-tire-fitting/', price_tire_fitting, name='price_tire_fitting'),
    path('reviews/', reviews, name='reviews'),
    path('site/login/', site_login, name='site_login'),
    path('site/signup/', site_signup, name='site_signup'),
    path('warranty/', warranty, name='warranty'),
]
