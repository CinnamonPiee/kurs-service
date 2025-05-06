from django.contrib import admin
from .models import (
	SiteVisitor,
	BasePageFooter,
)


@admin.register(SiteVisitor)
class SiteVisitorAdmin(admin.ModelAdmin):
	pass


@admin.register(BasePageFooter)
class BasePageFooterAdmin(admin.ModelAdmin):
	pass
