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
from django.contrib.sitemaps.views import sitemap
from .sitemaps import StaticViewSitemap
from .views import robots_txt
from site_login.views import site_logout


sitemaps = {
    'static': StaticViewSitemap,
}

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main_page.urls', namespace='main_page')),
	path('photo-gallery/', include('photo_gallery.urls', namespace='photo_gallery')),
	path('warranty/', include('warranty.urls', namespace='warranty')),
	path('contacts/', include('contacts.urls', namespace='contacts')),
	path('rules-personal-data/', include('rules_personal_data.urls', namespace='rules_personal_data')),
	path('about/', include('about.urls', namespace='about')),
	path('site/login', include('site_login.urls', namespace='site_login')),
	path('site/signup', include('site_signup.urls', namespace='site_signup')),
	path('reviews/', include('reviews.urls', namespace='reviews')),
	path('discounts/', include('discounts.urls', namespace='discounts')),
	path('news/', include('news.urls', namespace='news')),
	path('insurance/', include('insurance.urls', namespace='insurance')),
	path('evacuation/', include('evacuation.urls', namespace='evacuation')),
	path('diagnostics/', include('diagnostics.urls', namespace='diagnostics')),
	path('online-appointment/', include('online_appointment.urls', namespace='online_appointment')),
	
	path("logout/", site_logout, name="site_logout"),

	path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
	path('robots.txt', robots_txt, name='robots_txt'),

]

if settings.DEBUG:
	urlpatterns += debug_toolbar_urls()
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
