from django.contrib import admin
from .models import (
	MainPageSliderImages,
	MainPageTitles,
	MainPageDirectionOfActivity,
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
