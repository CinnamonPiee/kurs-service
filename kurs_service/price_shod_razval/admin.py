from django.contrib import admin
from .models import (
	PriceShodRazvalCategory,
	PriceShodRazvalPrice,
)


@admin.register(PriceShodRazvalCategory)
class PriceShodRazvalCategoryAdmin(admin.ModelAdmin):
	pass


@admin.register(PriceShodRazvalPrice)
class PriceShodRazvalPriceAdmin(admin.ModelAdmin):
	pass
