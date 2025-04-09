from django.contrib import admin
from main_page.models import (
	MainPageSlider,
	MainPageDirectionOfActivity,
	MainPageAlwaysInStock,
	MainPageAdditionalPowerEquipmentAMTH,
	MainPageAdditionalPowerEquipment,
	MainPageOurAdvantages,
	MainPageOurAdvantagesVideo,
	MainPageQuestions,
	MainPageEverythingToBoBest,
	MainPageProfessionalEquipment,
	MainPageTitles,
)


@admin.register(MainPageSlider)
class MainPageSliderAdmin(admin.ModelAdmin):
	pass


@admin.register(MainPageDirectionOfActivity)
class MainPageDirectionOfActivityAdmin(admin.ModelAdmin):
	pass


@admin.register(MainPageAlwaysInStock)
class MainPageAlwaysInStockAdmin(admin.ModelAdmin):
	pass


@admin.register(MainPageAdditionalPowerEquipmentAMTH)
class MMainPageAdditionalPowerEquipmentAMTHAdmin(admin.ModelAdmin):
	pass


@admin.register(MainPageAdditionalPowerEquipment)
class MainPageAdditionalPowerEquipmentAdmin(admin.ModelAdmin):
	pass


@admin.register(MainPageOurAdvantages)
class MainPageOurAdvantagesAdmin(admin.ModelAdmin):
	pass


@admin.register(MainPageOurAdvantagesVideo)
class MainPageOurAdvantagesVideoAdmin(admin.ModelAdmin):
	pass


@admin.register(MainPageQuestions)
class MainPageQuestionsAdmin(admin.ModelAdmin):
	pass


@admin.register(MainPageEverythingToBoBest)
class MainPageEverythingToBoBestAdmin(admin.ModelAdmin):
	pass


@admin.register(MainPageProfessionalEquipment)
class MainPageProfessionalEquipmentAdmin(admin.ModelAdmin):
	pass


@admin.register(MainPageTitles)
class MainPageTitlesAdmin(admin.ModelAdmin):
	pass
