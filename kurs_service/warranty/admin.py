from django.contrib import admin
from warranty.models import (
	WarrantyObligations,
	WarrantyTitles,
	WarrantyImages,
)


@admin.register(WarrantyImages)
class WarrantyImagesAdmin(admin.ModelAdmin):
	pass


@admin.register(WarrantyObligations)
class WarrantyObligationsAdmin(admin.ModelAdmin):
	pass


@admin.register(WarrantyTitles)
class WarrantyTitlesAdmin(admin.ModelAdmin):
	pass
