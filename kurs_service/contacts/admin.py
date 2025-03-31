from django.contrib import admin
from contacts.models import DrivingDirection


@admin.register(DrivingDirection)
class DrivingDirectionAdmin(admin.ModelAdmin):
	pass
