from django.contrib import admin
from about.models import (
	AboutImages,
    AboutDescriptionCompany,
    AboutAdvantages,
    AboutContacts,
    AboutTrainingStaff,
	AboutTitles,
)


@admin.register(AboutImages)
class AboutImagesAdmin(admin.ModelAdmin):
	pass


@admin.register(AboutDescriptionCompany)
class AboutDescriptionCompanyAdmin(admin.ModelAdmin):
	pass


@admin.register(AboutAdvantages)
class AboutAdvantagesAdmin(admin.ModelAdmin):
	pass


@admin.register(AboutContacts)
class AboutContactsAdmin(admin.ModelAdmin):
	pass


@admin.register(AboutTrainingStaff)
class AboutTrainingStaffAdmin(admin.ModelAdmin):
	pass


@admin.register(AboutTitles)
class AboutTitlesAdmin(admin.ModelAdmin):
	pass
