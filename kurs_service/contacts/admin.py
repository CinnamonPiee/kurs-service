from django.contrib import admin
from contacts.models import (
	ContactsDataContacts,
	ContactsDetailsAndContacts,
	ContactsSchemeAndDetails,
	ContactsSchemeImage,
	ContactsSliderImages,
	ContactsTitles,
	ContactsWeekdayWorkingTime,
)


@admin.register(ContactsDataContacts)
class ContactsDataContactsAdmin(admin.ModelAdmin):
	pass


@admin.register(ContactsDetailsAndContacts)
class ContactsDetailsAndContactsAdmin(admin.ModelAdmin):
	pass


@admin.register(ContactsSchemeAndDetails)
class ContactsSchemeAndDetailsAdmin(admin.ModelAdmin):
	pass


@admin.register(ContactsSchemeImage)
class ContactsSchemeImageAdmin(admin.ModelAdmin):
	pass


@admin.register(ContactsSliderImages)
class ContactsSliderImagesAdmin(admin.ModelAdmin):
	pass


@admin.register(ContactsTitles)
class ContactsTitlesAdmin(admin.ModelAdmin):
	pass


@admin.register(ContactsWeekdayWorkingTime)
class ContactsWeekdayWorkingTimeAdmin(admin.ModelAdmin):
	pass