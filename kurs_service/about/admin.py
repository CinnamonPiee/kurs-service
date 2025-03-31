from django.contrib import admin
from about.models import (
	DescriptionCompany,
    Advantages,
    BestInBusiness,
    Contacts,
    AccuratelyTime,
	Training,
    AboutHeaders,
)


@admin.register(DescriptionCompany)
class DescriptionCompanyAdmin(admin.ModelAdmin):
	pass


@admin.register(Advantages)
class AdvantagesAdmin(admin.ModelAdmin):
	pass


@admin.register(BestInBusiness)
class BestInBusinessAdmin(admin.ModelAdmin):
	pass


@admin.register(Contacts)
class ContactsAdmin(admin.ModelAdmin):
	pass


@admin.register(AccuratelyTime)
class AccuratelyTimeAdmin(admin.ModelAdmin):
	pass


@admin.register(Training)
class TrainingAdmin(admin.ModelAdmin):
	pass


@admin.register(AboutHeaders)
class AboutHeadersAdmin(admin.ModelAdmin):
	pass
