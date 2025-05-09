from django.contrib import admin
from .models import (
	MainPageSliderImages,
	MainPageTitles,
	MainPageDirectionOfActivity,
	MainPageAlwaysInStock,
	MainPageAdditionalPowerEquipmentAMZ,
	MainPageAdditionalPowerEquipment,
	MainPageEverythingToBeConsideredTheBest,
	MainPageFrequentlyAskedQuestions,
	MainPageOurAdvantages,
	MainPageProfessionalEquipment
)


@admin.register(MainPageSliderImages)
class MainPageSliderImagesAdmin(admin.ModelAdmin):
	pass


@admin.register(MainPageDirectionOfActivity)
class MainPageDirectionOfActivityAdmin(admin.ModelAdmin):
	pass


@admin.register(MainPageTitles)
class MainPageTitlesAdmin(admin.ModelAdmin):
	pass


@admin.register(MainPageAlwaysInStock)
class MainPageAlwaysInStockAdmin(admin.ModelAdmin):
	pass


@admin.register(MainPageAdditionalPowerEquipmentAMZ)
class MainPageAdditionalPowerEquipmentAMZAdmin(admin.ModelAdmin):
	pass


@admin.register(MainPageAdditionalPowerEquipment)
class MainPageAdditionalPowerEquipmentAdmin(admin.ModelAdmin):
	pass


@admin.register(MainPageEverythingToBeConsideredTheBest)
class MainPageEverythingToBeConsideredTheBestAdmin(admin.ModelAdmin):
	pass


@admin.register(MainPageFrequentlyAskedQuestions)
class MainPageFrequentlyAskedQuestionsAdmin(admin.ModelAdmin):
	pass


@admin.register(MainPageOurAdvantages)
class MainPageOurAdvantagesAdmin(admin.ModelAdmin):
	pass


@admin.register(MainPageProfessionalEquipment)
class MainPageProfessionalEquipmentAdmin(admin.ModelAdmin):
	pass
