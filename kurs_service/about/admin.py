from django.contrib import admin
from about.models import DescriptionCompany, Training


@admin.register(DescriptionCompany)
class DescriptionCompanyAdmin(admin.ModelAdmin):
	pass


@admin.register(Training)
class TrainingAdmin(admin.ModelAdmin):
	pass
