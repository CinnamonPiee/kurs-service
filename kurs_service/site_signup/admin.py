from django.contrib import admin
from .models import SiteSignupTitles


@admin.register(SiteSignupTitles)
class SiteSignupTitlesAdmin(admin.ModelAdmin):
	pass

