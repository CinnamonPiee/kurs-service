from django.contrib import admin
from contacts.models import (
    ContactsImages,
    ContactsWorkingTime,
    ContactsCompanyData,
    ContactsCompanyDetails,
    ContactsDirectionSchema,
	ContactsMapSchema,
    ContactsTitles,
)


@admin.register(ContactsImages)
class ContactsImagesAdmin(admin.ModelAdmin):
	pass


@admin.register(ContactsWorkingTime)
class ContactsWorkingTimeAdmin(admin.ModelAdmin):
	pass


@admin.register(ContactsCompanyData)
class ContactsCompanyDataAdmin(admin.ModelAdmin):
	pass


@admin.register(ContactsCompanyDetails)
class ContactsCompanyDetailsAdmin(admin.ModelAdmin):
	pass


@admin.register(ContactsDirectionSchema)
class ContactsDirectionSchemaAdmin(admin.ModelAdmin):
	pass


@admin.register(ContactsMapSchema)
class ContactsMapSchemaAdmin(admin.ModelAdmin):
	pass


@admin.register(ContactsTitles)
class ContactsTitlesAdmin(admin.ModelAdmin):
	pass
