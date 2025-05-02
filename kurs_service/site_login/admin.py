from django.contrib import admin
from .models import SiteLoginTitles


@admin.register(SiteLoginTitles)
class SiteLoginTitlesAdmin(admin.ModelAdmin):
	pass
