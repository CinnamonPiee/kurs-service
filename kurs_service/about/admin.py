from django.contrib import admin
from about.models import (
	AboutAccuratelyInTime,
	AboutBestInBusiness,
	AboutContacts,
	AboutHowWeTrainingStaff,
	AboutLetsAcquainted,
	AboutOurAdvantages,
	AboutTitles,
)


@admin.register(AboutAccuratelyInTime)
class AboutAccuratelyInTimeAdmin(admin.ModelAdmin):
	pass


@admin.register(AboutBestInBusiness)
class AboutBestInBusinessAdmin(admin.ModelAdmin):
	pass


@admin.register(AboutContacts)
class AboutContactsAdmin(admin.ModelAdmin):
	pass


@admin.register(AboutHowWeTrainingStaff)
class AboutHowWeTrainingStaffAdmin(admin.ModelAdmin):
	pass


@admin.register(AboutLetsAcquainted)
class AboutLetsAcquaintedAdmin(admin.ModelAdmin):
	pass


@admin.register(AboutOurAdvantages)
class AboutOurAdvantagesAdmin(admin.ModelAdmin):
	pass


@admin.register(AboutTitles)
class AboutTitlesAdmin(admin.ModelAdmin):
	pass
