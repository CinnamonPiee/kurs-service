from django.contrib import admin
from warranty.models import (
	WarrantySliderImages,
	WarrantyObligations,
	WarrantyTitles,
)


@admin.register(WarrantySliderImages)
class WarrantySliderImagesAdmin(admin.ModelAdmin):
	pass


@admin.register(WarrantyObligations)
class WarrantyObligationsAdmin(admin.ModelAdmin):
	pass


@admin.register(WarrantyTitles)
class WarrantyTitlesAdmin(admin.ModelAdmin):
	pass
