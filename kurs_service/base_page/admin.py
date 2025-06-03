from unittest.mock import Base
from django.contrib import admin
from .models import (
	SiteVisitor,
	CarBody,
	CarMark,
	CarModel,
	CarModification,
	CarService,
	BasePageSideMenu,
	BasePageFooterImage,
	BasePageFooter,
	BasePageSocialImages,
	BasePageHeader,
	BasePageNotification,
	BasePageAddOrderServiceModal,
	BasePageAddOrderServiceModalForm,
)


@admin.register(SiteVisitor)
class SiteVisitorAdmin(admin.ModelAdmin):
	pass


@admin.register(CarBody)
class CarBodyAdmin(admin.ModelAdmin):
	pass


@admin.register(CarMark)
class CarMarkAdmin(admin.ModelAdmin):
	pass


@admin.register(CarModel)
class CarModelAdmin(admin.ModelAdmin):
	pass


@admin.register(CarModification)
class CarModificationAdmin(admin.ModelAdmin):
	pass


@admin.register(CarService)
class CarServiceAdmin(admin.ModelAdmin):
	pass


@admin.register(BasePageSideMenu)
class BasePageSideMenuAdmin(admin.ModelAdmin):
	pass


@admin.register(BasePageAddOrderServiceModal)
class BasePageAddOrderServiceModalAdmin(admin.ModelAdmin):
	pass


@admin.register(BasePageAddOrderServiceModalForm)
class BasePageAddOrderServiceModalFormAdmin(admin.ModelAdmin):
	pass


@admin.register(BasePageHeader)
class BasePageHeaderAdmin(admin.ModelAdmin):
	pass


@admin.register(BasePageFooterImage)
class BasePageFooterImageAdmin(admin.ModelAdmin):
	pass


@admin.register(BasePageSocialImages)
class BasePageSocialImagesAdmin(admin.ModelAdmin):
	pass


@admin.register(BasePageFooter)
class BasePageFooterAdmin(admin.ModelAdmin):
	pass


@admin.register(BasePageNotification)
class BasePageNotificationAdmin(admin.ModelAdmin):
	pass
