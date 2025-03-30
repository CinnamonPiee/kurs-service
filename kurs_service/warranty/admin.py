from django.contrib import admin
from warranty.models import WarrantyObligations


@admin.register(WarrantyObligations)
class WarrantyObligationsAdmin(admin.ModelAdmin):
	pass
