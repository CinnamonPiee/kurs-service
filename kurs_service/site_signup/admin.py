from django.contrib import admin
from site_signup.models import (
	SiteSignupText,
	SiteSignupTitles,
)


@admin.register(SiteSignupText)
class SiteSignupTextAdmin(admin.ModelAdmin):
	pass


@admin.register(SiteSignupTitles)
class SiteSignupTitlesAdmin(admin.ModelAdmin):
	pass