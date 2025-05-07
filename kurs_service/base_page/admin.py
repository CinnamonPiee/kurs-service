from django.contrib import admin
from .models import (
	SiteVisitor,
	BasePageSideMenu,
	BasePageFooterImage,
	BasePageFooter,
	BasePageSocialImages,
	BasePageHeader,
)


@admin.register(SiteVisitor)
class SiteVisitorAdmin(admin.ModelAdmin):
	pass


@admin.register(BasePageSideMenu)
class BasePageSideMenuAdmin(admin.ModelAdmin):
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
