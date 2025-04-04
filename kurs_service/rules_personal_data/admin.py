from django.contrib import admin
from rules_personal_data.models import (
	RulesPersonalDataImages,
	RulesPersonalDataObligations,
	RulesPersonalDataTitles,
)


@admin.register(RulesPersonalDataImages)
class RulesPersonalDataImagesAdmin(admin.ModelAdmin):
	pass


@admin.register(RulesPersonalDataObligations)
class RulesPersonalDataObligationsAdmin(admin.ModelAdmin):
	pass


@admin.register(RulesPersonalDataTitles)
class RulesPersonalDataTitlesAdmin(admin.ModelAdmin):
	pass
