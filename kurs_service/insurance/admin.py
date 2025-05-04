from django.contrib import admin
from .models import (
	InsuranceSliderImages,
	InsuranceForm,
	InsuranceBenefitsOfInsuringWithUs,
	InsuranceFrequentlyAskedQuestions,
	InsuranceTitles,
)


@admin.register(InsuranceTitles)
class InsuranceTitlesAdmin(admin.ModelAdmin):
	pass


@admin.register(InsuranceFrequentlyAskedQuestions)
class InsuranceFrequentlyAskedQuestionsAdmin(admin.ModelAdmin):
	pass


@admin.register(InsuranceBenefitsOfInsuringWithUs)
class InsuranceBenefitsOfInsuringWithUsAdmin(admin.ModelAdmin):
	pass


@admin.register(InsuranceForm)
class InsuranceFormAdmin(admin.ModelAdmin):
	pass


@admin.register(InsuranceSliderImages)
class InsuranceSliderImagesAdmin(admin.ModelAdmin):
	pass