from django.contrib import admin
from .models import (
	EvacuationSliderImages,
	EvacuationForm,
	EvacuationCarType,
	EvacuationFree,
	EvacuationPricesInCaseOfRefusalToRepairThead,
	EvacuationPricesInCaseOfRefusalToRepairTbody,
	EvacuationPricesForAdditionalEvacuationServicesThead,
	EvacuationPricesForAdditionalEvacuationServicesTbody,
	EvacuationTitles,
)


@admin.register(EvacuationSliderImages)
class EvacuationSliderImagesAdmin(admin.ModelAdmin):
	pass 


@admin.register(EvacuationForm)
class EvacuationFormAdmin(admin.ModelAdmin):
	pass


@admin.register(EvacuationCarType)
class EvacuationCarTypeAdmin(admin.ModelAdmin):
	pass


@admin.register(EvacuationFree)
class EvacuationFreeAdmin(admin.ModelAdmin):
	pass


@admin.register(EvacuationPricesInCaseOfRefusalToRepairThead)
class EvacuationPricesInCaseOfRefusalToRepairTheadAdmin(admin.ModelAdmin):
	pass


@admin.register(EvacuationPricesInCaseOfRefusalToRepairTbody)
class EvacuationPricesInCaseOfRefusalToRepairTbodyAdmin(admin.ModelAdmin):
	pass


@admin.register(EvacuationPricesForAdditionalEvacuationServicesThead)
class EvacuationPricesForAdditionalEvacuationServicesTheadAdmin(admin.ModelAdmin):
	pass


@admin.register(EvacuationPricesForAdditionalEvacuationServicesTbody)
class EvacuationPricesForAdditionalEvacuationServicesTbodyAdmin(admin.ModelAdmin):
	pass


@admin.register(EvacuationTitles)
class EvacuationTitlesAdmin(admin.ModelAdmin):
	pass
