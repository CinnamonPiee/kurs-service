from django.contrib import admin
from rules_personal_data.models import (
    PersonalDataHeaders,
    PersonalDataText,
    PersonalDataTitle,
)


@admin.register(PersonalDataHeaders)
class PersonalDataHeadersAdmin(admin.ModelAdmin):
	pass


@admin.register(PersonalDataText)
class PersonalDataTextAdmin(admin.ModelAdmin):
	pass


@admin.register(PersonalDataTitle)
class PersonalDataTitleAdmin(admin.ModelAdmin):
	pass
