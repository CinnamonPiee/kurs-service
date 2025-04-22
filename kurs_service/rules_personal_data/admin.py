from django.contrib import admin
from rules_personal_data.models import (
	RulesPersonalDataObligations,
	RulesPersonalDataMainObligation,
	RulesPersonalDataSliderImages,
	RulesPersonalDataTitles,
)


@admin.register(RulesPersonalDataObligations)
class RulesPersonalDataObligationsAdmin(admin.ModelAdmin):
	pass


@admin.register(RulesPersonalDataMainObligation)
class RulesPersonalDataMainObligationAdmin(admin.ModelAdmin):
	pass


@admin.register(RulesPersonalDataSliderImages)
class RulesPersonalDataSliderImagesAdmin(admin.ModelAdmin):
	pass


@admin.register(RulesPersonalDataTitles)
class RulesPersonalDataTitlesAdmin(admin.ModelAdmin):
	pass
