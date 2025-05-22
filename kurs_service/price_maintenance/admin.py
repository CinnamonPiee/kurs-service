from django.contrib import admin
from .models import (
	PriceMaintenanceCategory,
	PriceMaintenancePrice,
)


@admin.register(PriceMaintenanceCategory)
class PriceMaintenanceCategoryAdmin(admin.ModelAdmin):
	pass


@admin.register(PriceMaintenancePrice)
class PriceMaintenancePriceAdmin(admin.ModelAdmin):
	pass
