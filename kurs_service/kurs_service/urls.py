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
from django.urls import include, path
from django.conf.urls.static import static
from django.conf import settings
from debug_toolbar.toolbar import debug_toolbar_urls


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main_page.urls', namespace='main_page')),
	path('about/', include('about.urls', namespace='about')),
	path('check-list/', include('check_list.urls', namespace='check_list')),
	path('contacts/', include('contacts.urls', namespace='contacts')),
	path('diagnostics/', include('diagnostics.urls', namespace='diagnostics')),
	path('discounts/', include('discounts.urls', namespace='discounts')),
	path('evacuation/', include('evacuation.urls', namespace='evacuation')),
	path('insurance/', include('insurance.urls', namespace='insurance')),
	path('news/', include('news.urls', namespace='news')),
	path('online-appointment/', include('online_appointment.urls', namespace='online_appointment')),
	path('photo-gallery', include('photo_gallery.urls', namespace='photo_gallery')),
	path('price-maintenance/', include('price_maintenance.urls', namespace='price_maintenance')),
	path('price-shod-razval/', include('price_shod_razval.urls', namespace='price_shod_razval')),
	path('price-tire-fitting/', include('price_tire_fitting.urls', namespace='price_tire_fitting')),
	path('reviews/', include('reviews.urls', namespace='reviews')),
	path('site/login/', include('site_login.urls', namespace='site_login')),
	path('site/signup/', include('site_signup.urls', namespace='site_signup')),
    path('warranty/', include('warranty.urls', namespace='warranty')),
]

if settings.DEBUG:
	urlpatterns += debug_toolbar_urls()
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
