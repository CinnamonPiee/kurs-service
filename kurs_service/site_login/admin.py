from django.contrib import admin
from site_login.models import (
	SiteLoginText,
	SiteLoginTitles,
)


@admin.register(SiteLoginText)
class SiteLoginTextAdmin(admin.ModelAdmin):
	pass


@admin.register(SiteLoginTitles)
class SiteLoginTitlesAdmin(admin.ModelAdmin):
	pass
