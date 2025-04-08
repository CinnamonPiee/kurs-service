from django.contrib import admin
from discounts.models import (
	DiscountsContent,
	DiscountsTitles,
)


@admin.register(DiscountsContent)
class DiscountsContentAdmin(admin.ModelAdmin):
	pass


@admin.register(DiscountsTitles)
class DiscountsTitlesAdmin(admin.ModelAdmin):
	pass
