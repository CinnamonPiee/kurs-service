from django.contrib import admin
from warranty.models import (
	WarrantyObligations,
	WarrantyHeaders,
	Warranty180,
)


@admin.register(WarrantyObligations)
class WarrantyObligationsAdmin(admin.ModelAdmin):
	pass


@admin.register(WarrantyHeaders)
class WarrantyHeadersAdmin(admin.ModelAdmin):
	pass


@admin.register(Warranty180)
class Warranty180Admin(admin.ModelAdmin):
	pass
