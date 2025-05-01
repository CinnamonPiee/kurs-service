from django.contrib import admin
from .models import SiteVisitor


@admin.register(SiteVisitor)
class SiteVisitorAdmin(admin.ModelAdmin):
	pass
