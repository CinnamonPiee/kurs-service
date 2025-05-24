from django.contrib import admin
from .models import (
	PriceTireFittingCategory,
	PriceTireFittingPrice,
)


@admin.register(PriceTireFittingCategory)
class PricePriceTireFittingCategoryAdmin(admin.ModelAdmin):
	pass


@admin.register(PriceTireFittingPrice)
class PricePriceTireFittingPriceAdmin(admin.ModelAdmin):
	pass
