from django.contrib import admin
from .models import (
	DiscountsTitles,
	DiscountsDiscount,
)


@admin.register(DiscountsDiscount)
class DiscountsDiscountAdmin(admin.ModelAdmin):
	pass


@admin.register(DiscountsTitles)
class DiscountsTitlesAdmin(admin.ModelAdmin):
	pass
