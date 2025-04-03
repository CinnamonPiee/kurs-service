from django.contrib import admin
from contacts.models import (
    SupportHelp,
    WorkingTime,
    ContactsData,
    ContactsAndDetails,
    DirectionScheme,
    ContactsHeaders,
)


@admin.register(SupportHelp)
class SupportHelpAdmin(admin.ModelAdmin):
	pass


@admin.register(WorkingTime)
class WorkingTimeAdmin(admin.ModelAdmin):
	pass


@admin.register(ContactsData)
class ContactsDataAdmin(admin.ModelAdmin):
	pass


@admin.register(ContactsAndDetails)
class ContactsAndDetailsAdmin(admin.ModelAdmin):
	pass


@admin.register(DirectionScheme)
class DirectionSchemeAdmin(admin.ModelAdmin):
	pass


@admin.register(ContactsHeaders)
class ContactsHeadersAdmin(admin.ModelAdmin):
	pass
